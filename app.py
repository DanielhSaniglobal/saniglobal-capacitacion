# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from guia_data import EMBUDOS_INFO, MENSAJES_RAPIDOS, ETAPAS_BANOS, ETAPAS_FOSAS, ETAPAS_TRAMPAS
import re
import os

# Helper function to render markdown text and extract image tags to display them inline via st.image
def render_markdown_with_images(md_text):
    if not md_text:
        return
    pattern = r'!\[(.*?)\]\((.*?)\)'
    parts = re.split(pattern, md_text)
    i = 0
    script_dir = os.path.dirname(os.path.abspath(__file__))
    while i < len(parts):
        text_block = parts[i]
        if text_block.strip():
            st.markdown(text_block)
        if i + 2 < len(parts):
            caption = parts[i+1]
            img_path = parts[i+2]
            # Resolve image path relative to the script directory if it is relative
            if not os.path.isabs(img_path):
                full_img_path = os.path.normpath(os.path.join(script_dir, img_path))
            else:
                full_img_path = img_path
            
            if os.path.exists(full_img_path):
                st.image(full_img_path, caption=caption, use_container_width=True)
            else:
                st.warning(f"Imagen no encontrada: {img_path} (ruta resuelta: {full_img_path})")
            i += 3
        else:
            i += 1

# 1. Page Configuration
st.set_page_config(
    page_title="Capacitación Saniglobal",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Theme Toggle State (Light mode by default)
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

IS_DARK = st.session_state.theme == "dark"

# 3. Security (Password Protection)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def check_password():
    if st.session_state.login_pass == "Saniglobal2026@":
        st.session_state.authenticated = True
        st.session_state.password_error = False
    else:
        st.session_state.authenticated = False
        st.session_state.password_error = True

if not st.session_state.authenticated:
    bg_color = "#09090b" if IS_DARK else "#f9fafb"
    card_bg = "#0c0c0f" if IS_DARK else "#ffffff"
    border_color = "#1e1e24" if IS_DARK else "#e4e4e7"
    text_color = "#fafafa" if IS_DARK else "#09090b"
    text_muted = "#71717a"
    
    st.markdown(f"""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .main, .block-container {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
        font-family: 'DM Sans', sans-serif !important;
    }}
    .login-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 3rem 2rem;
        background: {card_bg};
        border: 1px solid {border_color};
        border-radius: 12px;
        max-width: 450px;
        margin: 5% auto 0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
    }}
    .login-title {{
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: {text_color};
    }}
    .login-subtitle {{
        font-size: 0.85rem;
        color: {text_muted};
        margin-bottom: 2rem;
        text-align: center;
    }}
    .error-msg {{
        color: #ef4444;
        font-size: 0.8rem;
        margin-top: 0.5rem;
    }}
    header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{
        display: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="login-container">
        <div class="login-title">🔐 Acceso a Capacitación</div>
        <div class="login-subtitle">Introduce la clave corporativa de Saniglobal para ingresar al módulo interactivo de embudos y procesos de venta en Kommo CRM.</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.text_input("Contraseña:", type="password", key="login_pass", on_change=check_password)
        if st.session_state.get("password_error", False):
            st.markdown('<div class="error-msg" style="text-align: center;">⚠️ Contraseña incorrecta. Inténtalo de nuevo.</div>', unsafe_allow_html=True)
        st.stop()

# 4. Premium Injected CSS Design System (Authenticated App)
bg_color = "#09090b" if IS_DARK else "#ffffff"
bg_subtle = "#0c0c0f" if IS_DARK else "#f9fafb"
card_bg = "#0c0c0f" if IS_DARK else "#ffffff"
card_hover = "#131316" if IS_DARK else "#f4f4f5"
border_color = "#1e1e24" if IS_DARK else "#e4e4e7"
border_subtle = "#16161a" if IS_DARK else "#f0f0f2"
text_color = "#fafafa" if IS_DARK else "#09090b"
text_muted = "#71717a"
text_dim = "#52525b" if IS_DARK else "#a1a1aa"
accent_color = "#2563eb"
green_color = "#22c55e" if IS_DARK else "#16a34a"
green_bg = "rgba(34,197,94,0.12)" if IS_DARK else "rgba(22,163,74,0.08)"
red_color = "#ef4444" if IS_DARK else "#dc2626"
red_bg = "rgba(239,68,68,0.12)" if IS_DARK else "rgba(220,38,38,0.08)"
amber_color = "#f59e0b" if IS_DARK else "#d97706"
amber_bg = "rgba(245,158,11,0.12)" if IS_DARK else "rgba(217,119,6,0.08)"
shadow_val = "none" if IS_DARK else "0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.03)"

st.markdown(f"""
<style>
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"], .stDeployButton,
div[data-testid="stSidebarCollapsedControl"] {{
    display: none !important;
}}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .main, .block-container, section[data-testid="stMain"] {{
    background-color: {bg_color} !important;
    color: {text_color} !important;
    font-family: 'DM Sans', -apple-system, sans-serif !important;
}}
.block-container {{
    padding: 1.5rem 2.5rem 3rem !important;
    max-width: 1360px !important;
    margin: 0 auto !important;
}}

[data-testid="stHorizontalBlock"] {{
    gap: 1.25rem !important;
}}

.custom-card {{
    background: {card_bg};
    border: 1px solid {border_color};
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    box-shadow: {shadow_val};
    margin-bottom: 1.25rem;
}}
.custom-card:hover {{
    border-color: {accent_color};
    background: {card_hover};
    transition: all 0.2s ease-in-out;
}}

.metric-card {{
    background: {card_bg};
    border: 1px solid {border_color};
    border-radius: 10px;
    padding: 1.25rem 1.4rem;
    box-shadow: {shadow_val};
}}
.metric-label {{
    font-size: 0.78rem;
    color: {text_muted};
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}}
.metric-value {{
    font-size: 1.65rem;
    font-weight: 700;
    color: {text_color};
    letter-spacing: -0.03em;
    margin-top: 0.2rem;
}}
.metric-subtitle {{
    font-size: 0.72rem;
    color: {text_dim};
    margin-top: 0.3rem;
}}

button[data-baseweb="tab"] {{
    background: transparent !important;
    color: {text_muted} !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 0.55rem 1.2rem !important;
    border: 1px solid transparent !important;
    border-radius: 7px !important;
    margin-right: 5px !important;
}}
button[data-baseweb="tab"][aria-selected="true"] {{
    color: {text_color} !important;
    background: {card_bg} !important;
    border-color: {border_color} !important;
}}
[data-baseweb="tab-highlight"], [data-baseweb="tab-border"] {{
    display: none !important;
}}
[data-baseweb="tab-list"] {{
    gap: 4px !important;
    background: {bg_subtle} !important;
    border: 1px solid {border_color} !important;
    border-radius: 10px !important;
    padding: 4px !important;
}}

.badge {{
    display: inline-block;
    padding: 2px 9px;
    border-radius: 6px;
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
}}
.badge-green {{ color: {green_color}; background: {green_bg}; }}
.badge-red {{ color: {red_color}; background: {red_bg}; }}
.badge-amber {{ color: {amber_color}; background: {amber_bg}; }}
.badge-blue {{ color: {accent_color}; background: rgba(37,99,235,0.1); }}

.brand {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 0.5rem;
}}
.brand-logo {{
    font-size: 1.5rem;
    font-weight: 800;
    color: {accent_color};
}}
.brand-name {{
    font-size: 1.25rem;
    font-weight: 700;
    color: {text_color};
    letter-spacing: -0.02em;
}}
.brand-badge {{
    font-size: 0.65rem;
    background: {accent_color};
    color: #ffffff;
    padding: 2px 6px;
    border-radius: 4px;
    text-transform: uppercase;
    font-weight: 700;
}}

.accent-border-card {{ border-left: 4px solid {accent_color} !important; }}
.amber-border-card {{ border-left: 4px solid {amber_color} !important; }}
.red-border-card {{ border-left: 4px solid {red_color} !important; }}

.h-divider {{
    border-top: 1px solid {border_color};
    margin: 1.5rem 0;
}}
</style>
""", unsafe_allow_html=True)

# 5. Header Component
head_left, head_right = st.columns([8, 1])
with head_left:
    st.markdown("""
    <div class="brand">
        <span class="brand-logo">◆</span>
        <span class="brand-name">Saniglobal</span>
        <span class="brand-badge">Capacitación Kommo CRM</span>
    </div>
    """, unsafe_allow_html=True)
with head_right:
    theme_label = "☀️ Claro" if IS_DARK else "🌙 Oscuro"
    st.button(theme_label, on_click=toggle_theme, use_container_width=True)

# 6. Load Guide Sections from Markdown
def load_guide_sections():
    sections = {}
    try:
        with open("Guia_Capacitacion_Embudos.md", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove raw HTML anchor tags to prevent them from showing in Streamlit expanders
        import re
        content = re.sub(r'<a\s+name="[^"]*">\s*</a>', '', content)
        
        headers = [
            ("glosario", "### 1. 📖 Glosario Rápido"),
            ("gpt_completo", "### 2. 🌟 El Embudo GPT Completo — El Origen de Todo"),
            ("reglas_diarias", "### 3. 🛠️ Reglas de Operación Diaria"),
            ("soporte_quejas", "### 4. 😤 Embudos de Soporte y Regla Especial de Quejas"),
            ("seccion_banos", "## 🚽 SECCIÓN II: RENTA DE BAÑOS PORTÁTILES"),
            ("gestion_ganados_banos", "### 📋 Gestión y Reactivación de Clientes Ganados (Tengan o no Baño Activo)"),
            ("seccion_fosas", "## 🌀 SECCIÓN III: SERVICIOS ESPECIALES Y FOSAS SÉPTICAS"),
            ("seccion_trampas", "## 🍳 SECCIÓN IV: TRAMPAS DE GRASA"),
            ("tabla_resumen", "## 📌 Tabla Resumen de Reglas, Cupones y Gestión de Quejas"),
            ("buenas_practicas", "## 🚀 Buenas Prácticas de Servicio (Uso de Kommo CRM)"),
            ("qa", "## ❓ Sección de Preguntas y Respuestas (Q&A) de la Guía de Ventas"),
            ("guias_operacion", "## 📖 Guías Prácticas de Operación en Kommo CRM para Vendedores")
        ]
        
        def find_header_start(content, header):
            idx = 0
            while True:
                pos = content.find(header, idx)
                if pos == -1:
                    return -1
                if pos > 0 and content[pos - 1] == '#':
                    idx = pos + len(header)
                    continue
                return pos
        
        positions = []
        for key, header in headers:
            pos = find_header_start(content, header)
            if pos != -1:
                positions.append((key, pos, header))
        
        positions.sort(key=lambda x: x[1])
        
        for i in range(len(positions)):
            key, start_idx, header = positions[i]
            if i < len(positions) - 1:
                content_end = positions[i+1][1]
            else:
                content_end = len(content)
            sections[key] = content[start_idx:content_end].strip()
            
    except Exception as e:
        print(f"Error loading guide sections: {e}")
    return sections

sections = load_guide_sections()

# Helper to render unified guides (dynamically filtered per tab)
def render_unified_guides_for_tab(tab_name, sections):
    st.markdown("### 📘 Guías de Operación y Reglas Generales")
    st.markdown("Consulta las bases del sistema comercial y directrices obligatorias en Kommo CRM:")
    
    # 1. Introducción a Kommo CRM
    with st.expander("🎬 1. Introducción: ¿Qué es Kommo CRM y cómo captamos clientes?"):
        st.markdown("""
        ### ¿Qué es Kommo CRM?
        Kommo es nuestra plataforma central de gestión de relaciones con clientes (CRM). Aunque para el cliente final la comunicación ocurre 100% en su chat familiar de **WhatsApp**, para nosotros, Kommo es el panel de control unificado que concentra todas estas conversaciones en una sola bandeja de entrada colaborativa y automatizada.
        
        ### Ventajas de Kommo vs. WhatsApp Tradicional (Celular)
        - **Colaboración Multiusuario:** Permite que todo nuestro equipo trabaje simultáneamente en la computadora o celular sin necesidad de vincular dispositivos físicos ni sufrir cierres de sesión.
        - **Asignación Inteligente:** Los prospectos se asignan de forma automática al vendedor especializado correspondiente (Baños a Daniel Herrera, Fosas a Livier Mora, Trampas a Asesor de Trampas) según lo que elijan al chatear.
        - **Control de Tareas y Tiempos:** El sistema obliga a programar una tarea a futuro (llamadas, cotizaciones, seguimientos) para cada lead comercial. Si una tarea se vence o no existe, el CRM colorea el prospecto de rojo para alertar sobre la desatención.
        - **Historial Permanente:** Se registran permanentemente notas internas, fechas de cotización y los cambios de etapa para que no se pierda nada de información del cliente.
        
        ### ¿Cómo llegan los prospectos a nuestro CRM?
        Nuestros clientes potenciales son atraídos mediante campañas de marketing digital integradas:
        1. **Meta Ads (Facebook & Instagram Ads):** Anuncios visuales en redes sociales diseñados bajo el formato *Click-to-WhatsApp*. Al hacer clic en el anuncio, se abre el chat directo y el mensaje entra al CRM.
        2. **Google Ads & Web Orgánica:** Los usuarios buscan activamente en Google (ej. *"renta de baños portátiles"*), ingresan a nuestro sitio web, y dan clic en nuestros botones flotantes de WhatsApp.
        En ambos casos, el lead entra de forma inmediata al CRM e inicia el **Bot GPT Completo** de bienvenida.
        
        ### ¿Por qué existen los embudos y cuál es el objetivo?
        Un embudo (o pipeline) divide el proceso de venta en etapas ordenadas y consecutivas para organizar el seguimiento según el nivel de interés del cliente.
        - **Por qué existen:** Para separar visualmente a los prospectos (no es igual de prioritario un lead que apenas saludó a uno al que ya le cotizamos y requiere cierre manual).
        - **El verdadero objetivo:** **Tener un control absoluto sobre nuestra base de clientes** (saber quiénes somos, qué servicios activos tenemos en sitio y cuándo corresponde recontactar para reactivación o retiro) para **optimizar las ventas y no dejar ir ninguna oportunidad de ingresos.**
        """)
        
    # 2. Glosario Rápido
    glosario_txt = sections.get("glosario", "")
    if tab_name != "fosas":
        lines = glosario_txt.split("\n")
        filtered_lines = [l for l in lines if "Casa Habitación" not in l]
        glosario_txt = "\n".join(filtered_lines)
    with st.expander("📖 2. Glosario Rápido"):
        render_markdown_with_images(glosario_txt)
        
    # 3. El Embudo GPT Completo (Filtrado)
    gpt_txt = sections.get("gpt_completo", "")
    if tab_name == "banos":
        gpt_txt = gpt_txt.replace("- 🔧 **Servicios especiales** → El bot lo mueve al **Embudo de Servicios Especiales (Fosas)** y lo asigna a Livier Mora.\n", "")
        gpt_txt = gpt_txt.replace("¿Te interesa rentar un baño portátil o buscas algún servicio especializado como limpieza de fosas sépticas, trampas de grasa, recolección de residuos?", "¿Te interesa rentar un baño portátil?")
    elif tab_name == "fosas":
        gpt_txt = gpt_txt.replace("- 🚽 **Rentar baños** → El bot lo mueve al **Embudo de Ventas (Baños)** y lo asigna a Daniel Herrera.\n", "")
        gpt_txt = gpt_txt.replace("¿Te interesa rentar un baño portátil o buscas algún servicio especializado como limpieza de fosas sépticas, trampas de grasa, recolección de residuos?", "¿Buscas algún servicio especializado como limpieza de fosas sépticas?")
    elif tab_name == "trampas":
        gpt_txt = gpt_txt.replace("- 🚽 **Rentar baños** → El bot lo mueve al **Embudo de Ventas (Baños)** y lo asigna a Daniel Herrera.\n", "")
        gpt_txt = gpt_txt.replace("¿Te interesa rentar un baño portátil o buscas algún servicio especializado como limpieza de fosas sépticas, trampas de grasa, recolección de residuos?", "¿Buscas algún servicio especializado como limpieza de trampas de grasa?")
    with st.expander("🌟 3. El Embudo GPT Completo — El Origen de Todo"):
        render_markdown_with_images(gpt_txt)
        
    # 4. Reglas de Operación Diaria (Filtrado)
    reglas_txt = sections.get("reglas_diarias", "")
    if tab_name == "banos":
        reglas_txt = reglas_txt.replace("Livier Mora (Usuario 13346199)", "Daniel Herrera").replace("Asesor de Trampas de Grasa", "Daniel Herrera")
        reglas_txt = reglas_txt.replace('"Cotización realizada", "Cotización de trampas de grasa manual", "Baño entregado"', '"Cotización realizada", "Baño entregado"')
        reglas_txt = reglas_txt.replace('"Cotización de trampas de grasa manual"', '"Cotización realizada"')
    elif tab_name == "fosas":
        for marker in ["#### 📬 Proceso Obligatorio de Programación", "#### Proceso Obligatorio de Programación", "Proceso Obligatorio de Programación"]:
            if marker in reglas_txt:
                reglas_txt = reglas_txt.split(marker)[0]
                reglas_txt = re.sub(r'####\s*📬?\s*$', '', reglas_txt).strip()
                break
        reglas_txt = reglas_txt.replace("Daniel Herrera (Usuario 12824423)", "Livier Mora").replace("Asesor de Trampas de Grasa", "Livier Mora")
        reglas_txt = reglas_txt.replace('"Cotización realizada", "Cotización de trampas de grasa manual", "Baño entregado"', '"Cotización realizada"')
        reglas_txt = reglas_txt.replace('"Cotización de trampas de grasa manual"', '"Cotización realizada"')
    elif tab_name == "trampas":
        for marker in ["#### 📬 Proceso Obligatorio de Programación", "#### Proceso Obligatorio de Programación", "Proceso Obligatorio de Programación"]:
            if marker in reglas_txt:
                reglas_txt = reglas_txt.split(marker)[0]
                reglas_txt = re.sub(r'####\s*📬?\s*$', '', reglas_txt).strip()
                break
        reglas_txt = reglas_txt.replace("Daniel Herrera (Usuario 12824423)", "Asesor de Trampas").replace("Livier Mora (Usuario 13346199)", "Asesor de Trampas")
        reglas_txt = reglas_txt.replace('"Cotización realizada", "Cotización de trampas de grasa manual", "Baño entregado"', '"Cotización de trampas de grasa manual"')
    with st.expander("🛠️ 4. Reglas de Operación Diaria"):
        render_markdown_with_images(reglas_txt)
        
    # 5. Embudos de Soporte y Regla Especial de Quejas (Filtrado)
    soporte_txt = sections.get("soporte_quejas", "")
    lines = soporte_txt.split("\n")
    filtered_soporte = []
    skip_mode = False
    
    if tab_name == "banos":
        for line in lines:
            if "#### 🌀 Fosas" in line or "#### 🍳 Trampas" in line:
                skip_mode = True
            elif "#### Embudo de Otros" in line or "#### 🚽 Renta de Baños" in line:
                skip_mode = False
            if not skip_mode:
                filtered_soporte.append(line)
    elif tab_name == "fosas":
        for line in lines:
            if "#### 🚽 Renta de Baños" in line or "#### 🍳 Trampas" in line:
                skip_mode = True
            elif "#### Embudo de Otros" in line or "#### 🌀 Fosas" in line:
                skip_mode = False
            if not skip_mode:
                clean_line = line.replace(" y 🍳 Trampas", "").replace(" o trampas de grasa", "")
                filtered_soporte.append(clean_line)
    elif tab_name == "trampas":
        for line in lines:
            if "#### 🚽 Renta de Baños" in line or "#### 🌀 Fosas" in line:
                skip_mode = True
            elif "#### Embudo de Otros" in line or "#### 🍳 Trampas" in line:
                skip_mode = False
            if not skip_mode:
                clean_line = line.replace("🌀 Fosas (Livier Mora) y ", "").replace("fosas sépticas o ", "")
                filtered_soporte.append(clean_line)
                
    with st.expander("😤 5. Embudos de Soporte y Regla de Quejas"):
        render_markdown_with_images("\n".join(filtered_soporte))
        
    # 6. Guías Prácticas de Operación (Filtrado)
    guias_txt = sections.get("guias_operacion", "")
    if tab_name == "banos":
        guias_txt = guias_txt.replace("Livier Mora", "Daniel Herrera").replace("Asesor de Trampas", "Daniel Herrera")
        guias_txt = guias_txt.replace("(ej. Casa Habitación en fosas)", "(ej. quejas en baños)")
        guias_txt = guias_txt.replace("Daniel Herrera o Livier Mora", "Daniel Herrera")
    elif tab_name == "fosas":
        guias_txt = guias_txt.replace("Daniel Herrera", "Livier Mora").replace("Asesor de Trampas", "Livier Mora")
        guias_txt = guias_txt.replace("Daniel Herrera o Livier Mora", "Livier Mora")
    elif tab_name == "trampas":
        guias_txt = guias_txt.replace("Daniel Herrera", "Asesor de Trampas").replace("Livier Mora", "Asesor de Trampas")
        guias_txt = guias_txt.replace("(ej. Casa Habitación en fosas)", "(ej. quejas de grasa)")
        guias_txt = guias_txt.replace("Daniel Herrera o Livier Mora", "Asesor de Trampas")
        guias_txt = guias_txt.replace("'La calle es estrecha, se requiere camión chico'", "'La trampa está en sótano, requiere manguera extra'")
    with st.expander("📖 6. Guías Prácticas de Operación en Kommo CRM"):
        render_markdown_with_images(guias_txt)
        
    # 7. Buenas Prácticas (Filtrado)
    bp_txt = sections.get("buenas_practicas", "")
    if tab_name == "banos":
        bp_txt = bp_txt.replace("(Baños, Fosas y Trampas)", "(Baños)")
        bp_txt = bp_txt.replace("`apoyo humano` en todos los embudos (Baños, Fosas y Trampas)", "la etapa de `apoyo humano` en el embudo de Baños")
    elif tab_name == "fosas":
        bp_txt = bp_txt.replace("(Baños, Fosas y Trampas)", "(Fosas)")
        bp_txt = bp_txt.replace("`apoyo humano` en todos los embudos (Baños, Fosas y Trampas)", "la etapa de `apoyo humano fosas` en el embudo de Fosas")
    elif tab_name == "trampas":
        bp_txt = bp_txt.replace("(Baños, Fosas y Trampas)", "(Trampas)")
        bp_txt = bp_txt.replace("`apoyo humano` en todos los embudos (Baños, Fosas y Trampas)", "la etapa de `APOYO HUMANO` en el embudo de Trampas")
    with st.expander("🚀 7. Buenas Prácticas de Servicio en Ventas"):
        render_markdown_with_images(bp_txt)
        
    # 8. Tabla Resumen (Filtrado)
    tabla_txt = sections.get("tabla_resumen", "")
    lines = tabla_txt.split("\n")
    filtered_tabla = []
    header_count = 0
    for line in lines:
        if "|" in line:
            if header_count < 2:
                filtered_tabla.append(line)
                header_count += 1
            else:
                if tab_name == "banos" and "Baños" in line:
                    filtered_tabla.append(line)
                elif tab_name == "fosas" and "Fosas" in line:
                    filtered_tabla.append(line)
                elif tab_name == "trampas" and "Trampas" in line:
                    filtered_tabla.append(line)
        else:
            filtered_tabla.append(line)
    with st.expander("📌 8. Tabla Resumen de Reglas, Cupones y Gestión de Quejas"):
        render_markdown_with_images("\n".join(filtered_tabla))

# Helper to render the Q&A filtered
def render_qa_for_tab(tab_name, sections):
    qa_txt = sections.get("qa", "")
    lines = qa_txt.split("\n")
    filtered_qa = []
    current_q_match = True
    
    for line in lines:
        if "*   **P" in line or "### P" in line:
            if "P2" in line or "P7" in line or "P8" in line:
                current_q_match = (tab_name == "banos")
            elif "P3" in line:
                current_q_match = (tab_name == "fosas")
            elif "P4" in line:
                current_q_match = (tab_name == "trampas")
            elif "P5" in line:
                current_q_match = True
            else:
                current_q_match = True
        
        if "P5:" in line or "Pregunta 5" in line:
            filtered_qa.append(line)
            continue
            
        if current_q_match:
            if "P5" in line and tab_name == "banos" and ("Fosas" in line or "Trampas" in line):
                continue
            if "P5" in line and tab_name == "fosas" and ("Baños" in line or "Trampas" in line):
                continue
            if "P5" in line and tab_name == "trampas" and ("Baños" in line or "Fosas" in line):
                continue
            filtered_qa.append(line)
            
    with st.expander("❓ Preguntas y Respuestas (Q&A) de la Guía de Ventas"):
        render_markdown_with_images("\n".join(filtered_qa))

# Helper to render the stages grid
def render_pipeline_grid(etapas, pipeline_name=""):
    num_etapas = len(etapas)
    cols_per_row = 4
    
    for i in range(0, num_etapas, cols_per_row):
        row_etapas = etapas[i:i+cols_per_row]
        cols = st.columns(cols_per_row)
        for idx, col in enumerate(cols):
            if idx < len(row_etapas):
                etapa = row_etapas[idx]
                with col:
                    is_lead_entrante = (pipeline_name == "baños" and etapa['num'] == 1)
                    title = f"**{etapa['num']}. {etapa['nombre']}**"
                    if is_lead_entrante:
                        title = f"🟢 **{etapa['num']}. {etapa['nombre']}**"
                    
                    with st.expander(title, expanded=False):
                        if is_lead_entrante:
                            st.markdown(f"""
                            <div style="background-color: {green_bg}; border: 1px solid {green_color}; border-radius: 8px; padding: 0.8rem; margin-bottom: 0.5rem;">
                                <span class="badge badge-green" style="margin-bottom: 0.5rem; background-color: {green_color}; color: #ffffff;">Etapa Inicial</span>
                                <p style="font-size:0.85rem; margin-bottom:0.4rem; line-height:1.4; color: {text_color};">
                                    <strong style="color: {green_color};">💡 Razón de ser / Secuencia lógica:</strong><br>
                                    {etapa['razon']}
                                </p>
                                <p style="font-size:0.85rem; margin-bottom:0.4rem; line-height:1.4; color: {text_color};">
                                    <strong style="color: {green_color};">🤖 Automatización:</strong><br>
                                    {etapa['automatizacion']}
                                </p>
                                <p style="font-size:0.85rem; margin-bottom:0px; line-height:1.4; color: {text_color};">
                                    <strong style="color: {green_color};">👤 Deber del vendedor:</strong><br>
                                    {etapa['deber_vendedor']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div style="padding: 0.1rem 0;">
                                <p style="font-size:0.85rem; margin-bottom:0.5rem; line-height:1.4;">
                                    <strong style="color: {accent_color};">💡 Razón de ser / Secuencia lógica:</strong><br>
                                    {etapa['razon']}
                                </p>
                                <p style="font-size:0.85rem; margin-bottom:0.5rem; line-height:1.4;">
                                    <strong style="color: {accent_color};">🤖 Automatización:</strong><br>
                                    {etapa['automatizacion']}
                                </p>
                                <p style="font-size:0.85rem; margin-bottom:0px; line-height:1.4;">
                                    <strong style="color: {accent_color};">👤 Deber del vendedor:</strong><br>
                                    {etapa['deber_vendedor']}
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
            else:
                col.empty()

# 7. Navigation Tabs
tab_banos, tab_fosas, tab_trampas, tab_recursos = st.tabs([
    "🚽 Renta de Baños", 
    "🌀 Fosas Sépticas", 
    "🍳 Trampas de Grasa",
    "📂 Recursos & Plantillas"
])

# ----------------------------------------------------
# TAB 1: RENTA DE BAÑOS
# ----------------------------------------------------
with tab_banos:
    st.markdown("### 🚽 Renta de Baños Portátiles")
    st.markdown(f'<div class="badge badge-blue">Vendedor Responsable: {EMBUDOS_INFO["baños"]["responsable"]}</div>', unsafe_allow_html=True)
    
    # KPIs Card Row
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">Asesor Comercial</div>
            <div class="metric-value">Daniel Herrera</div>
            <div class="metric-subtitle">Responsable del <strong>Embudo de ventas</strong> (debes tener este embudo seleccionado en la sección de Leads del menú de la barra izquierda que siempre está fija).</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">Canales Vinculados</div>
            <div class="metric-value">WhatsApp / Meta</div>
            <div class="metric-subtitle">Renta de sanitarios portátiles obra y eventos en ZM Guadalajara / SLP.</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Render Unified Guides
    render_unified_guides_for_tab("banos", sections)
    render_qa_for_tab("banos", sections)
    
    # Specific guide sections in accordions (Replacing the old raw index bullets)
    st.markdown("### 📋 Guía Específica de Renta de Baños")
    
    with st.expander("📋 1. Flujo y Etapas del Embudo de Ventas (Baños)"):
        render_markdown_with_images(sections.get("seccion_banos", ""))
        
    with st.expander("💬 2. Secuencia de Preguntas del Bot de Renta"):
        st.markdown("""
        El bot de renta de baños recopila de forma automática los siguientes datos para calificar al cliente y formular la cotización:
        1. **¿Obra o Evento?** (Recomienda la cantidad de sanitarios según el tipo de uso y número de personas).
        2. **¿Cuántos baños?** (Si el prospecto solicita 3 o más unidades, el bot se pausa automáticamente y lo turna a Daniel Herrera para atención y cotización manual).
        3. **¿Tipo de baño?** (Sencillo vs. Con Lavamanos. Muestra fotos comparativas de ambos).
        4. **¿Por cuánto tiempo?** (Renta por mes/quincena en obras, por día/semana en eventos).
        5. **¿Dirección de entrega?** (Valida que sea texto y no un pin de ubicación. Debe estar dentro de la Zona Metropolitana de Guadalajara o ZM San Luis Potosí).
        """)
        
    with st.expander("👥 3. Gestión de Clientes Activos (Ganados, Reactivaciones y Retiros)"):
        render_markdown_with_images(sections.get("gestion_ganados_banos", ""))
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📊 Tablero Visual de Etapas del Embudo (Renta de Baños)")
    st.markdown("El embudo se compone de **18 etapas** secuenciales en el orden exacto de tu CRM. Cada columna representa una etapa individual en orden de flujo comercial. Haz clic en cada tarjeta para ver su detalle:")
    
    etapas_banos = ETAPAS_BANOS
    
    render_pipeline_grid(etapas_banos, "baños")

# ----------------------------------------------------
# TAB 2: FOSAS SÉPTICAS
# ----------------------------------------------------
with tab_fosas:
    st.markdown("### 🌀 Servicios Especiales y Fosas Sépticas")
    st.markdown(f'<div class="badge badge-blue">Vendedora Responsable: {EMBUDOS_INFO["fosas"]["responsable"]}</div>', unsafe_allow_html=True)
    
    # KPIs Card Row
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">Asesora Comercial</div>
            <div class="metric-value">Livier Mora</div>
            <div class="metric-subtitle">Responsable del <strong>Embudo Fosas GDL</strong> (debes tener este embudo seleccionado en la sección de Leads del menú de la barra izquierda que siempre está fija).</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">Canales Vinculados</div>
            <div class="metric-value">WhatsApp / Meta</div>
            <div class="metric-subtitle">Sondeos, desazolves y disposición de lodos para el sector comercial e industrial.</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Render Unified Guides
    render_unified_guides_for_tab("fosas", sections)
    render_qa_for_tab("fosas", sections)
    
    # Specific guide sections in accordions (Replacing the old raw index bullets)
    st.markdown("### 📋 Guía Específica de Servicios Especiales y Fosas")
    
    with st.expander("📋 1. Flujo y Etapas del Embudo de Fosas"):
        render_markdown_with_images(sections.get("seccion_fosas", ""))
        
    with st.expander("💬 2. Secuencia de Preguntas del Bot de Fosas"):
        st.markdown("""
        El bot de fosas realiza de forma automática las siguientes preguntas de calificación técnica para que la asesora pueda cotizar:
        1. **¿Qué residuo es?** (Fosas sépticas, lodo biológico, aguas de proceso, vinazas, etc. Envía el PDF de presentación de Saniglobal).
        2. **¿Estado del material?** (Líquido, Lodo o pasta, Sólido o polvo).
        3. **¿Dónde está almacenado?** (Fosa/cisterna, Tambo/tolva/sacos, Sobre terreno).
        4. **¿Volumen o cantidad?** (Menos de 5,000 lt/kg, 5,000 a 10,000, Más de 10,000).
        """)
        
    with st.expander("🏠 3. Filtro Crítico de Casa Habitación (Exclusión)"):
        st.markdown("""
        **Regla de Exclusión:** Saniglobal no atiende domicilios residenciales o particulares en el servicio de fosas.
        - **Automatización:** El bot pregunta: *¿Es para una casa habitacional o residencial?* 
        - Si responde **"Sí"**, el bot le coloca la etiqueta **`CASA HABITACIÓN`**, envía el mensaje de rechazo cortés y mueve el lead a la etapa **Cerrado**.
        - Si responde **"No"**, continúa con el flujo normal comercial.
        """)
        
    with st.expander("🔎 4. Visita de Diagnóstico y Seguimiento"):
        st.markdown("""
        - **Visita de Diagnóstico:** Para proyectos complejos, es obligatorio programar una visita física antes de cotizar. El lead se mantiene en la etapa `Visita diagnóstico` hasta contar con el reporte de accesos y tipo de residuo.
        - **Seguimiento Automático (21 horas):** Tras enviar la cotización manual en PDF, la asesora debe presionar el botón "Cotización realizada". A las 21h sin respuesta, el bot de seguimiento se activa. Si la objeción es precio, ofrece 5% de descuento.
        """)
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📊 Tablero Visual de Etapas del Embudo (Fosas Sépticas)")
    st.markdown("El embudo se compone de **13 etapas** secuenciales en el orden exacto de tu CRM. Cada columna representa una etapa individual en orden de flujo comercial. Haz clic en cada tarjeta para ver su detalle:")
    
    etapas_fosas = ETAPAS_FOSAS
    render_pipeline_grid(etapas_fosas, "fosas")

# ----------------------------------------------------
# TAB 3: TRAMPAS DE GRASA
# ----------------------------------------------------
with tab_trampas:
    st.markdown("### 🍳 Trampas de Grasa")
    st.markdown(f'<div class="badge badge-blue">Vendedor Responsable: {EMBUDOS_INFO["trampas"]["responsable"]}</div>', unsafe_allow_html=True)
    
    # KPIs Card Row
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">Asesor Comercial</div>
            <div class="metric-value">Asesor Trampas</div>
            <div class="metric-subtitle">Responsable del <strong>Embudo de Trampas de grasa</strong> (debes tener este embudo seleccionado en la sección de Leads del menú de la barra izquierda que siempre está fija).</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">Canales Vinculados</div>
            <div class="metric-value">WhatsApp / Meta</div>
            <div class="metric-subtitle">Limpieza y desazolve de trampas para restaurantes, hoteles y comedores industriales.</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Render Unified Guides
    render_unified_guides_for_tab("trampas", sections)
    render_qa_for_tab("trampas", sections)
    
    # Specific guide sections in accordions (Replacing the old raw index bullets)
    st.markdown("### 📋 Guía Específica de Trampas de Grasa")
    
    with st.expander("📋 1. Flujo y Etapas del Embudo de Trampas"):
        render_markdown_with_images(sections.get("seccion_trampas", ""))
        
    with st.expander("💬 2. Secuencia de Preguntas del Bot de Trampas"):
        st.markdown("""
        El bot de trampas realiza las siguientes preguntas de calificación técnica antes de procesar la cotización:
        1. **¿Cuántas trampas de grasa?** (Solo 1, 2, o 3 o más. Si pide 3 o más, va a cotización manual).
        2. **¿Capacidad o tamaño promedio?** (200 LTS estándar, 250 a 500 LTS, Más de 500 LTS. Tamaños mayores a 200 LTS van a cotización manual).
        3. **¿De qué material son?** (Plástico/PVC, Acero inoxidable/Metal, Concreto/Obra civil).
        4. **¿Cómo es el acceso para la unidad?** (A pie de trampa, Acceso complicado, Requiere permisos).
        5. **¿Distancia del camión a la trampa?** (Corta 0-10m, Media 11-20m, Larga más de 21m).
        6. **¿Cuenta con rampas accesibles?** (Sí, No lo sé, No).
        7. **Fotos/Videos:** Solicita evidencia visual para verificar las condiciones físicas antes del servicio.
        """)
        
    with st.expander("💰 3. Cotización Automática vs. Cotización Manual"):
        st.markdown("""
        - **Cotización Automática:** Si el cliente solicita 1 o 2 trampas estándar de 200 LTS y responde todas las preguntas del bot, el sistema procesa el webhook y envía un enlace de cotización personalizado de forma automática, moviendo el lead a `COTIZACIÓN`.
        - **Cotización Manual:** Si el tamaño es mayor a 200 LTS, requiere permisos o son más de 3 trampas, el asesor formula la cotización manualmente. Al enviarla en PDF, **debe presionar obligatoriamente el botón "Cotización de trampas de grasa manual"** en la tarjeta para continuar con el flujo del bot.
        """)
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📊 Tablero Visual de Etapas del Embudo (Trampas de Grasa)")
    st.markdown("El embudo se compone de **11 etapas** secuenciales en el orden exacto de tu CRM. Cada columna representa una etapa individual en orden de flujo comercial. Haz clic en cada tarjeta para ver su detalle:")
    
    etapas_trampas = ETAPAS_TRAMPAS
    
    render_pipeline_grid(etapas_trampas, "trampas")

# ----------------------------------------------------
# TAB 4: RECURSOS & PLANTILLAS
# ----------------------------------------------------
with tab_recursos:
    st.markdown("### 📂 Recursos Compartidos y Plantillas")
    st.markdown("Buscador de mensajes rápidos y material de apoyo para interactuar con los clientes en Kommo CRM.")

    # Search bar for templates
    search_tmpl = st.text_input("Buscar plantilla por título o contenido:", placeholder="Escribe aquí para buscar...")
    
    filtered_templates = [t for t in MENSAJES_RAPIDOS if search_tmpl.lower() in t["titulo"].lower() or search_tmpl.lower() in t["texto"].lower()]

    for tmpl in filtered_templates:
        with st.container():
            st.markdown(f"""
            <div class="custom-card accent-border-card">
                <strong>⚡ {tmpl['titulo']}</strong>
                <p style="font-size: 0.85rem; background: {bg_subtle}; border: 1px solid {border_color}; border-radius: 6px; padding: 0.8rem; font-family: monospace; white-space: pre-wrap; margin-top: 0.5rem;">{tmpl['texto']}</p>
            </div>
            """, unsafe_allow_html=True)
