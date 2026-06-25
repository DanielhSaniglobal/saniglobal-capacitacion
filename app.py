# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from guia_data import GLOSARIO, EMBUDOS_INFO, QUIZ_QUESTIONS, MENSAJES_RAPIDOS

# 1. Page Configuration
st.set_page_config(
    page_title="Capacitación Saniglobal",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Theme Toggle State
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
    # Login Page Custom CSS (Clean & Premium Card Layout)
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
    /* Hide Streamlit components */
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
    
    # Input in columns to keep it centered
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
/* Hide Streamlit chrome */
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"], .stDeployButton,
div[data-testid="stSidebarCollapsedControl"] {{
    display: none !important;
}}

/* Global App Styling */
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

/* Grid spacing */
[data-testid="stHorizontalBlock"] {{
    gap: 1.25rem !important;
}}

/* Custom Cards */
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

/* Metric Card (KPI) */
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

/* Pill styled Tabs */
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

/* Badges */
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

/* Tables */
.data-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 0.82rem;
    margin-top: 0.5rem;
}}
.data-table th {{
    text-align: left;
    padding: 0.65rem 0.8rem;
    color: {text_muted};
    font-weight: 600;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    border-bottom: 1px solid {border_color};
}}
.data-table td {{
    padding: 0.7rem 0.8rem;
    color: {text_color};
    border-bottom: 1px solid {border_subtle};
}}
.data-table tr:last-child td {{
    border-bottom: none;
}}

/* Brand / Header */
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

/* Accent elements */
.accent-border-card {{
    border-left: 4px solid {accent_color} !important;
}}
.amber-border-card {{
    border-left: 4px solid {amber_color} !important;
}}
.red-border-card {{
    border-left: 4px solid {red_color} !important;
}}

/* Spacing and margins */
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

def render_kommo_guides():
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📖 Guías Prácticas de Operación en Kommo CRM")
    st.markdown("Instrucciones clave para dominar el CRM y mantener tu bandeja organizada:")

    with st.expander("⚡ 1. Respuestas Rápidas (Mensajes Rápidos)"):
        st.markdown("""
        **¿Qué son y cómo te ayudan?**  
        Son textos predefinidos (números de cuenta, requisitos de contratación, precios básicos) que evitan que escribas lo mismo una y otra vez.
        
        **Cómo usarlas en el chat:**  
        1. Escribe la barra diagonal `/` en la caja de chat de un lead.
        2. Escribe palabras clave del título (ej. `/pagos` o `/requisitos`).
        3. El sistema desplegará las opciones. Presiona `Enter` para cargar el texto y envíalo.
        
        **Cómo crearlas desde Ajustes:**  
        1. Ve a **Ajustes** (icono de engranaje) → **Mensajes rápidos**.
        2. Haz clic en **Añadir plantilla**, asígnale un nombre descriptivo y escribe el mensaje. Puedes usar variables dinámicas como `{{contact.name}}` para que el sistema inserte el nombre del cliente automáticamente.
        """)

    with st.expander("📅 2. Las Tareas y la Sección de Calendario"):
        st.markdown("""
        Las tareas en Kommo son compromisos en tu agenda vinculados a un cliente. Tienen fecha, hora y responsable.
        
        **Tipos de Tareas en Kommo:**  
        * **Seguimiento:** Para recordatorios de llamadas ordinarias o confirmaciones de lectura de propuestas.
        * **Reunión:** Para visitas técnicas programadas o videollamadas con empresas.
        * **Personalizadas:** Tareas creadas por ti o el sistema con descripciones específicas.
        
        **Reglas Lógicas y Buenas Prácticas:**  
        - **Monitorea tu Calendario:** Revisa constantemente la sección de **Calendario** en la barra lateral izquierda. Ahí verás tus tareas agendadas en la semana: las que están *en proceso* (futuras) y las *vencidas* (en rojo). Evita acumular tareas vencidas; habla de un mal seguimiento.
        - **Recordatorios Externos Obligatorios:** Las alertas de Kommo en el navegador pueden pasarse por alto si estás fuera de la computadora o chateando en tu celular personal. **Es obligatorio programar recordatorios externos** (ej. alarmas en tu celular o eventos en tu calendario de Google Calendar) para contactar a los clientes en la fecha y hora exacta acordadas.
        """)

    with st.expander("✍️ 3. Las Notas (Registro de Acuerdos Especiales)"):
        st.markdown("""
        Las notas son anotaciones permanentes en la tarjeta del lead que no se le envían al cliente.
        
        **Qué debes registrar en las Notas para tu beneficio:**  
        * **Precios acordados:** Si le diste una cotización especial o un descuento manual específico.
        * **Requerimientos del sitio de entrega:** Detalles críticos para el camión o la logística (ej. *'La calle es estrecha, se requiere camión pequeño'*, *'Hay cables de luz bajos'*, *'Hay acceso limitado por obra'*).
        * **Datos de facturación e información fiscal:** Si los proporcionó por teléfono o notas rápidas.
        * **Contactos secundarios:** Nombres de secretarias, jefes de obra, encargados de compras, etc.
        
        **Beneficio:** Todo queda guardado en la tarjeta. Si te vas de vacaciones o te enfermas, cualquier compañero podrá leer tus notas y dar soporte al cliente sin repetir preguntas molestas.
        """)

    with st.expander("💬 4. Bandeja de Chats Limpia y Filtros de Usuario"):
        st.markdown("""
        Para operar de manera ágil y no perder ventas, es fundamental mantener ordenada tu bandeja de chats.
        
        **¿Por qué debes tener limpia la sección de chats?**  
        Si dejas acumuladas conversaciones abiertas sin resolver o sin responder, los chats entrantes nuevos se irán apilando, se sepultarán hacia abajo de la bandeja y perderemos leads por no responder en su ventana de 24 horas.
        
        **¿Cuándo se debe 'Cerrar conversación' o 'Marcar como resuelto'?**  
        * **Marcar como resuelto:** Cuando el cliente ya fue atendido, se le envió la información solicitada y no hay ninguna acción inmediata pendiente de nuestra parte en el chat. Esto limpia el chat de tu bandeja activa.
        * **Marcar conversación cerrada / Cerrar:** En canales de chat, cuando el contacto fue transferido a otro embudo (como quejas en baños) o cuando el prospecto fue rechazado (como casas habitación en fosas).
        
        **Filtros de Chat por Usuario:**  
        Para no saturarte con los chats de tus compañeros, aplica un filtro rápido:
        1. Ve a la sección de **Chats**.
        2. Haz clic en la barra de búsqueda y filtros superior.
        3. En el campo **Responsable**, selecciona tu usuario (ej. Daniel Herrera o Livier Mora).
        4. Guarda el filtro. Ahora la pantalla te mostrará **únicamente** los chats asignados a ti, permitiéndote concentrarte al 100% en tu bandeja de leads.
        """)

# 6. Main Navigation Tabs
tab_general, tab_banos, tab_fosas, tab_trampas, tab_quiz, tab_recursos, tab_guia = st.tabs([
    "🏠 Inicio & General", 
    "🚽 Renta de Baños", 
    "🌀 Fosas Sépticas", 
    "🍳 Trampas de Grasa",
    "📝 Examen Interactivo",
    "📂 Recursos & Plantillas",
    "📖 Guía Completa"
])

# ----------------------------------------------------
# TAB 1: INICIO & GENERAL
# ----------------------------------------------------
with tab_general:
    st.markdown("### 🎓 Módulo de Entrenamiento Comercial")
    st.markdown("Bienvenido al centro interactivo de capacitación de Saniglobal. Aquí comprenderás los procesos comerciales y de atención al cliente automatizados e integrados en Kommo CRM.")
    
    # KPIs Row
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">🚽 Renta de Baños</div>
            <div class="metric-value">Daniel Herrera</div>
            <div class="metric-subtitle">Responsable del pipeline de sanitarios portátiles.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">🌀 Fosas y Especiales</div>
            <div class="metric-value">Livier Mora</div>
            <div class="metric-subtitle">Responsable de fosas sépticas, lodos e industriales.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="metric-card accent-border-card">
            <div class="metric-label">🍳 Trampas de Grasa</div>
            <div class="metric-value">Asesor Trampas</div>
            <div class="metric-subtitle">Responsable de grasas alimenticias y restaurantes.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)

    st.markdown("### 🌟 El Embudo GPT Completo: El Origen de Todo")
    st.markdown("Todos los mensajes entrantes (de WhatsApp, FB, Instagram) llegan a este embudo inicial. El Bot GPT Completo actúa como recepcionista virtual. Clasifica la intención del cliente en una de tres categorías mediante botones interactivos:")

    # Interactive flowchart of GPT Completo
    col_flow1, col_flow2, col_flow3 = st.columns(3)
    with col_flow1:
        st.markdown(f"""
        <div class="custom-card accent-border-card" style="text-align: center; height: 180px;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🚽</div>
            <strong style="color: {text_color};">Botón 'Rentar baños'</strong>
            <p style="font-size: 0.78rem; color: {text_muted}; margin-top: 0.4rem;">Canaliza al prospecto al <strong>Embudo de Ventas (Baños)</strong> y lo asigna automáticamente al usuario de <strong>Daniel Herrera</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_flow2:
        st.markdown(f"""
        <div class="custom-card accent-border-card" style="text-align: center; height: 180px;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🔧</div>
            <strong style="color: {text_color};">Botón 'Servicios especiales'</strong>
            <p style="font-size: 0.78rem; color: {text_muted}; margin-top: 0.4rem;">Canaliza al prospecto al <strong>Embudo de Servicios Especiales</strong> y lo asigna automáticamente a <strong>Livier Mora</strong>.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_flow3:
        st.markdown(f"""
        <div class="custom-card accent-border-card" style="text-align: center; height: 180px;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">💬</div>
            <strong style="color: {text_color};">Botón 'Otro asunto'</strong>
            <p style="font-size: 0.78rem; color: {text_muted}; margin-top: 0.4rem;">Canaliza al prospecto al <strong>Embudo de Otros Asuntos</strong> para clasificar en Recursos Humanos, Compras o Soporte.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)

    # Glosario Interactivo
    st.markdown("### 📖 Glosario Interactivo de Términos")
    st.markdown("Busca y consulta definiciones rápidas del sistema:")
    search_term = st.text_input("Filtrar términos (ej. Webhook, Etiqueta, Ventana...):", placeholder="Escribe aquí para buscar...")
    
    glosario_filtered = {k: v for k, v in GLOSARIO.items() if search_term.lower() in k.lower() or search_term.lower() in v.lower()}
    
    glosario_rows = ""
    for k, v in glosario_filtered.items():
        glosario_rows += f"<tr><td><strong>{k}</strong></td><td>{v}</td></tr>"
        
    st.markdown(f"""
    <table class="data-table">
        <thead>
            <tr><th style="width: 250px;">Término</th><th>Qué significa en Saniglobal</th></tr>
        </thead>
        <tbody>
            {glosario_rows if glosario_rows else '<tr><td colspan=\"2\" style=\"text-align: center;\">No se encontraron términos coincidentes.</td></tr>'}
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)

    # Reglas generales
    st.markdown("### 🛠️ Reglas Generales de Operación")
    col_reg1, col_reg2 = st.columns(2)
    with col_reg1:
        st.markdown(f"""
        <div class="custom-card amber-border-card" style="height: 100%;">
            <strong>⏱️ La Regla Crítica de 24 Horas de Meta</strong>
            <p style="font-size: 0.8rem; color: {text_muted}; margin-top: 0.5rem;">
                Meta prohíbe el envío de mensajes de texto libres después de pasadas 24 horas del último mensaje del cliente. 
                Nuestros bots de seguimiento automático están programados a las <strong>21 horas</strong> de inactividad para reaccionar dentro de la ventana.<br><br>
                <strong>Deber del asesor:</strong> Responde de inmediato. Si vence la ventana, tendrás que usar una plantilla HSM de costo para reactivar al cliente.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col_reg2:
        st.markdown(f"""
        <div class="custom-card amber-border-card" style="height: 100%;">
            <strong>👤 Transferencia de Prospectos (Asignación)</strong>
            <p style="font-size: 0.8rem; color: {text_muted}; margin-top: 0.5rem;">
                Cada lead tiene un asesor comercial responsable. Si necesitas reasignar a un compañero:<br>
                1. Abre la tarjeta del lead en Kommo CRM.<br>
                2. Cambia el campo de 'Responsable' al asesor correcto.<br>
                3. Guarda la tarjeta. El sistema se encarga de reasignar tareas pendientes y mandar alertas automáticas.<br>
                ⚠️ <strong>Regla de Oro de Asignación:</strong> Si reasignas una oportunidad a un compañero porque te llegó por error, <strong>es obligatorio agregar una nota interna</strong> en la tarjeta del lead detallando cualquier información extra, comentario o necesidad que el cliente ya te haya mencionado.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 2: RENTA DE BAÑOS
# ----------------------------------------------------
with tab_banos:
    st.markdown("### 🚽 Renta de Baños Portátiles")
    st.markdown("Información detallada para el flujo de sanitarios portátiles en eventos y obras de construcción.")
    
    # Responsible user
    st.markdown(f'<div class="badge badge-blue">Vendedor: {EMBUDOS_INFO["baños"]["responsable"]}</div>', unsafe_allow_html=True)
    
    st.markdown("#### Fases del Embudo")
    st.markdown("Haz clic en cualquier fase para ver las reglas de negocio y automatizaciones asociadas:")
    
    # Accordion stages for Baños
    for stage in EMBUDOS_INFO["baños"]["etapas"]:
        with st.expander(stage["nombre"]):
            st.markdown(f"**¿Qué ocurre en esta etapa?**\n{stage['descripcion']}")
            if "detalles" in stage:
                st.markdown(f"💡 **Regla de Operación:** {stage['detalles']}")
                
    render_kommo_guides()

# ----------------------------------------------------
# TAB 3: FOSAS SÉPTICAS
# ----------------------------------------------------
with tab_fosas:
    st.markdown("### 🌀 Servicios Especiales y Fosas Sépticas")
    st.markdown("Proceso comercial enfocado en servicios de limpieza de fosas sépticas, pozos de absorción, lodos y vinazas industriales.")
    
    st.markdown(f'<div class="badge badge-blue">Vendedora: {EMBUDOS_INFO["fosas"]["responsable"]}</div>', unsafe_allow_html=True)
    
    st.markdown("#### Fases del Embudo")
    for stage in EMBUDOS_INFO["fosas"]["etapas"]:
        with st.expander(stage["nombre"]):
            st.markdown(f"**¿Qué ocurre en esta etapa?**\n{stage['descripcion']}")
            if "detalles" in stage:
                st.markdown(f"💡 **Regla de Operación:** {stage['detalles']}")
                
    render_kommo_guides()

# ----------------------------------------------------
# TAB 4: TRAMPAS DE GRASA
# ----------------------------------------------------
with tab_trampas:
    st.markdown("### 🍳 Trampas de Grasa")
    st.markdown("Embudo especializado para limpieza y desazolve de grasas alimenticias en restaurantes y comedores industriales.")
    
    st.markdown(f'<div class="badge badge-blue">Vendedor: {EMBUDOS_INFO["trampas"]["responsable"]}</div>', unsafe_allow_html=True)
    
    st.markdown("#### Fases del Embudo")
    for stage in EMBUDOS_INFO["trampas"]["etapas"]:
        with st.expander(stage["nombre"]):
            st.markdown(f"**¿Qué ocurre en esta etapa?**\n{stage['descripcion']}")
            if "detalles" in stage:
                st.markdown(f"💡 **Regla de Operación:** {stage['detalles']}")
                
    render_kommo_guides()

# ----------------------------------------------------
# TAB 5: EXAMEN INTERACTIVO
# ----------------------------------------------------
with tab_quiz:
    st.markdown("### 📝 Examen de Capacitación Comercial")
    st.markdown("Responde las siguientes preguntas para evaluar tu comprensión de las reglas de negocio de Saniglobal en Kommo CRM.")

    # Initialize quiz state
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = [None] * len(QUIZ_QUESTIONS)
        st.session_state.quiz_submitted = False

    # Render questions
    for idx, item in enumerate(QUIZ_QUESTIONS):
        st.markdown(f"**Pregunta {idx+1}: {item['question']}**")
        # radio buttons
        selected = st.radio(
            f"Selecciona una opción para la pregunta {idx+1}:", 
            item["options"], 
            index=None,
            key=f"q_{idx}"
        )
        if selected is not None:
            st.session_state.quiz_answers[idx] = item["options"].index(selected)
        st.markdown("")

    # Submit Button
    if st.button("Enviar Examen para Calificación"):
        st.session_state.quiz_submitted = True
        
    if st.session_state.quiz_submitted:
        score = 0
        unanswered = False
        for idx, item in enumerate(QUIZ_QUESTIONS):
            ans = st.session_state.quiz_answers[idx]
            if ans is None:
                unanswered = True
            elif ans == item["correct"]:
                score += 1
                
        if unanswered:
            st.warning("⚠️ Hay preguntas sin contestar. Asegúrate de responder todas las preguntas antes de enviar.")
        
        st.markdown("#### Resultados del Examen:")
        final_score_pct = (score / len(QUIZ_QUESTIONS)) * 100
        
        if final_score_pct >= 80:
            st.success(f"🏆 ¡Felicidades! Calificación: {final_score_pct:.1f}% ({score}/{len(QUIZ_QUESTIONS)}) - Has aprobado el módulo de capacitación.")
        else:
            st.error(f"❌ Calificación: {final_score_pct:.1f}% ({score}/{len(QUIZ_QUESTIONS)}) - Necesitas repasar la guía y volver a intentarlo.")

        # Show explanations
        st.markdown("---")
        st.markdown("##### Retroalimentación:")
        for idx, item in enumerate(QUIZ_QUESTIONS):
            ans = st.session_state.quiz_answers[idx]
            st.markdown(f"**Pregunta {idx+1}: {item['question']}**")
            if ans is None:
                st.markdown("❌ *No contestada*")
            elif ans == item["correct"]:
                st.markdown(f"✅ Opción seleccionada correcta: *{item['options'][ans]}*")
            else:
                st.markdown(f"❌ Opción seleccionada incorrecta: *{item['options'][ans]}*")
                st.markdown(f"✔️ Opción correcta: **{item['options'][item['correct']]}**")
            st.markdown(f"💡 *Explicación:* {item['explanation']}")
            st.markdown("")

# ----------------------------------------------------
# TAB 6: RECURSOS & PLANTILLAS
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
            # copy button (Stream    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # 1. Buenas Prácticas de Servicio
    st.markdown("### 🚀 Buenas Prácticas de Servicio (Uso de Kommo CRM)")
    st.markdown("Para dar una atención excepcional y no perder ninguna oportunidad de venta, todo asesor debe seguir este listado obligatorio de buenas prácticas:")
    
    st.markdown(f"""
    <div class="custom-card accent-border-card" style="margin-bottom: 1.5rem;">
        <ul style="margin-bottom: 0; padding-left: 1.2rem; font-size: 0.9rem; line-height: 1.5;">
            <li><strong>⏱️ Revisar Kommo cada 5 minutos:</strong> Mantén el CRM abierto y revísalo de manera continua para reaccionar a cualquier mensaje entrante, actualización de chat o nueva tarea.</li>
            <li><strong>📥 Monitorear leads nuevos:</strong> Estate atento a las notificaciones de nuevos prospectos que ingresan al <em>Embudo GPT Completo</em> para verificar que el sistema los asigne correctamente.</li>
            <li><strong>🚨 Reportar anomalías al administrador:</strong> Si notas que un bot se detiene, no responde, o detectas fallos en la integración/webhooks, notifícalo de inmediato al administrador para corregirlo.</li>
            <li><strong>👤 Revisión constante de "Apoyo Humano":</strong> Consulta activamente la etapa de <em>Apoyo Humano</em> (en Baños, Fosas y Trampas). Estos leads requieren atención comercial prioritaria porque el bot no pudo resolver su duda o el cliente solicitó explícitamente hablar con un asesor.</li>
            <li><strong>📞 Seguimiento telefónico activo:</strong> ¡No dependas únicamente del chat! Si un cliente está en el <strong>Embudo Caliente</strong> o en estatus de <strong>Seguimiento</strong>, realiza una llamada telefónica para acelerar su decisión y cerrar la venta.</li>
            <li><strong>🏷️ Poner etiquetas (Tags) siempre:</strong> Asegúrate de agregar las etiquetas correctas a los leads (ej. <code>Queja</code>, <code>Propuesta enviada</code>, <code>-5% descuento</code>, <code>Sin respuesta</code>). Esto permite clasificar el inventario de prospectos y habilitar futuras campañas de recontacto masivo.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 2. Sección de Preguntas y Respuestas (Q&A)
    st.markdown("### ❓ Preguntas y Respuestas Frecuentes (Q&A)")
    st.markdown("Consulta respuestas directas a las dudas más comunes sobre la guía de ventas y operación del CRM:")

    qa_list = [
        {
            "q": "¿A dónde entran todos los leads que nos contactan por primera vez?",
            "a": "Todos los prospectos entran al **Embudo GPT Completo** en la etapa inicial. Un bot recepcionista virtual clasifica su interés dándoles a elegir entre: *Rentar baños* (se envía a Baños y asigna a Daniel Herrera), *Servicios especiales* (se envía a Fosas/Trampas y asigna a Livier/Asesor de trampas) u *Otros asuntos* (RH, proveedores, etc.)."
        },
        {
            "q": "¿Cómo funciona el Seguimiento Automático en el embudo de Renta de Baños?",
            "a": "Si cotizas un lead y el cliente no responde en **21 horas**, el bot le envía un recordatorio. Si pasan **24 horas más** (45h en total) y sigue sin responder, el sistema lo mueve automáticamente a *Seguimiento automático* con la etiqueta `Sin respuesta` para mantener limpia tu bandeja de chats."
        },
        {
            "q": "¿Qué pasa con las solicitudes residenciales en Fosas Sépticas?",
            "a": "Saniglobal **no realiza servicios residenciales** (casas habitación) en Servicios Especiales. El bot les pregunta si es propiedad residencial; si responden que 'Sí', les asigna la etiqueta `CASA HABITACIÓN`, envía una plantilla de rechazo cordial y los mueve automáticamente a **Cerrado** para no perder tiempo."
        },
        {
            "q": "¿Cómo califica una trampa de grasa para cotización automática?",
            "a": "Solo si son **1 o 2 trampas** y de tamaño estándar (**200 LTS**). Si son 3 o más trampas, de mayor tamaño o acceso complicado, el bot se detiene y se debe cotizar manualmente, tras lo cual debes hacer clic en el botón *'Cotización de trampas de grasa manual'* para activar los seguimientos."
        },
        {
            "q": "¿Cómo se manejan las quejas e inconformidades en cada embudo?",
            "a": "En **Baños**, la conversación se traslada de inmediato al **Embudo de Quejas Sanitarios** (Pipeline 12717196) en la etapa `INICIO QUEJA` para su resolución por soporte. En **Fosas y Trampas**, las quejas **no se envían a otro embudo**; se resuelven localmente en la etapa actual (o CLIENTE ACTUAL) agregando la etiqueta manual `Queja`."
        },
        {
            "q": "¿Cuál es la Regla de Oro de Asignación si recibo un lead por error?",
            "a": "Si reasignas a un compañero un lead que te llegó por error, **es obligatorio agregar una nota interna** detallando cualquier dato extra, comentario o necesidad que el cliente ya te haya expresado en el chat anterior para no perder el contexto."
        },
        {
            "q": "¿Cómo funciona el bot de descuento automático en baños?",
            "a": "Dos horas después de enviar una cotización (manual o automática), si el cliente no ha respondido, el bot envía automáticamente una oferta del **5% de descuento** y agrega el tag `-5% descuento` para incentivar el cierre."
        },
        {
            "q": "¿Qué pasa si un cliente ganado escribe de nuevo meses después?",
            "a": "El sistema rompe la pausa y lo mueve automáticamente a la etapa **Cliente Actual** del embudo de reactivación (*Ganados el cliente reactiva*), mostrándole un menú interactivo autogestionable (solicitar retiro de baños, cotizar otro servicio, registrar quejas, etc.)."
        }
    ]

    for item in qa_list:
        with st.expander(f"❓ {item['q']}"):
            st.markdown(item["a"])


# ----------------------------------------------------
# TAB 7: GUÍA COMPLETA
# ----------------------------------------------------
with tab_guia:
    st.markdown("### 📖 Guía de Capacitación Completa (Documento Oficial)")
    st.markdown("A continuación se muestra el documento de texto oficial con todas las explicaciones detalladas y reglas de negocio de Saniglobal.")
    
    try:
        with open("Guia_Capacitacion_Embudos.md", "r", encoding="utf-8") as f:
            guia_content = f.read()
        
        # Display the markdown content
        st.markdown(guia_content, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"No se pudo cargar el archivo de la guía: {e}")
