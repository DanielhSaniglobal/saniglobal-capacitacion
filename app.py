# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from guia_data import EMBUDOS_INFO, MENSAJES_RAPIDOS

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

# 6. Load Guide Sections from Markdown (and strip the internal TOC links)
def load_guide_sections():
    sections = {}
    try:
        with open("Guia_Capacitacion_Embudos.md", "r", encoding="utf-8") as f:
            content = f.read()
        
        headers = [
            ("general_parte1", "## ⚙️ PARTE I: BASES GENERALES (Para todo el equipo)"),
            ("seccion_banos", "## 🚽 SECCIÓN II: RENTA DE BAÑOS PORTÁTILES"),
            ("seccion_fosas", "## 🌀 SECCIÓN III: SERVICIOS ESPECIALES Y FOSAS SÉPTICAS"),
            ("seccion_trampas", "## 🍳 SECCIÓN IV: TRAMPAS DE GRASA"),
            ("tabla_resumen", "## 📌 Tabla Resumen de Reglas, Cupones y Gestión de Quejas"),
            ("buenas_practicas", "## 🚀 Buenas Prácticas de Servicio (Uso de Kommo CRM)"),
            ("qa", "## ❓ Sección de Preguntas y Respuestas (Q&A) de la Guía de Ventas"),
            ("guias_operacion", "## 📖 Guías Prácticas de Operación en Kommo CRM para Vendedores")
        ]
        
        positions = []
        for key, header in headers:
            pos = content.find(header)
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
            
        # Strip the redundant Table of Contents (TOC) with broken internal links
        if "general_parte1" in sections:
            part1_content = sections["general_parte1"]
            toc_start = part1_content.find("## 📌 Tabla de Contenidos")
            if toc_start != -1:
                glossary_start = part1_content.find("### 1. 📖 Glosario Rápido")
                if glossary_start != -1:
                    sections["general_parte1"] = part1_content[:toc_start] + part1_content[glossary_start:]
                    
    except Exception as e:
        print(f"Error loading guide sections: {e}")
    return sections

sections = load_guide_sections()

# Helper to render unified guides
def render_unified_guides(sections):
    st.markdown("### 📘 Guías de Operación y Reglas Generales")
    st.markdown("Consulta las bases del sistema comercial y directrices obligatorias para todo el equipo:")
    
    with st.expander("⚙️ 1. Bases Generales e Introducción"):
        st.markdown(sections.get("general_parte1", ""))
        
    with st.expander("📖 2. Guías Prácticas de Operación en Kommo CRM"):
        st.markdown(sections.get("guias_operacion", ""))
        
    with st.expander("🚀 3. Buenas Prácticas de Servicio en Ventas"):
        st.markdown(sections.get("buenas_practicas", ""))
        
    with st.expander("📌 4. Tabla Resumen de Reglas, Cupones y Gestión de Quejas"):
        st.markdown(sections.get("tabla_resumen", ""))

# Helper to render the stages grid
def render_pipeline_grid(etapas):
    num_etapas = len(etapas)
    cols_per_row = 4
    
    for i in range(0, num_etapas, cols_per_row):
        row_etapas = etapas[i:i+cols_per_row]
        cols = st.columns(cols_per_row)
        for idx, col in enumerate(cols):
            if idx < len(row_etapas):
                etapa = row_etapas[idx]
                with col:
                    with st.expander(f"**{etapa['num']}. {etapa['nombre']}**", expanded=False):
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
            <div class="metric-subtitle">Responsable del pipeline de sanitarios portátiles.</div>
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
    render_unified_guides(sections)
    
    with st.expander("❓ Preguntas y Respuestas (Q&A) de la Guía de Ventas"):
        st.markdown(sections.get("qa", ""))
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Specific guide section
    st.markdown(sections.get("seccion_banos", ""))
    
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📊 Tablero Visual de Etapas del Embudo (Renta de Baños)")
    st.markdown("El embudo se compone de **17 etapas** secuenciales en el orden exacto de Kommo CRM. Cada columna representa una etapa individual en orden de flujo comercial. Haz clic en cada tarjeta para ver su detalle:")
    
    etapas_banos = [
        {
            "num": 1,
            "nombre": "Solicitud de Cotización / Contacto",
            "razon": "Punto de entrada inicial del prospecto interesado al seleccionar 'Rentar baños'.",
            "automatizacion": "El bot recopila uso (obra o evento), cantidad, tipo de baño, duración y dirección de forma autogestionada. Si el cliente pide 3 o más baños, el bot se detiene.",
            "deber_vendedor": "Monitorear el chat. Si pide 3 o más baños, o falla la validación de dirección, debes cotizar manualmente."
        },
        {
            "num": 2,
            "nombre": "Apoyo Humano",
            "razon": "Casos donde el bot no califica datos o el cliente pide hablar con asesor.",
            "automatizacion": "Detiene el bot y genera una tarea urgente para Daniel Herrera.",
            "deber_vendedor": "Retomar el chat de inmediato para dar atención manual personalizada."
        },
        {
            "num": 3,
            "nombre": "Embudo Caliente",
            "razon": "El cliente está respondiendo activamente en el chat.",
            "automatizacion": "El bot no envía mensajes automatizados de seguimiento para evitar interrumpir o empalmarse con la conversación en vivo del asesor.",
            "deber_vendedor": "Dar atención manual e inmediata vía chat en vivo para empujar la venta."
        },
        {
            "num": 4,
            "nombre": "Solicitud de Información",
            "razon": "Validación de datos del cliente antes de enviar la propuesta.",
            "automatizacion": "Ninguna automatización de envío masivo activa.",
            "deber_vendedor": "Completar y validar los datos de entrega y fiscales en la tarjeta del lead."
        },
        {
            "num": 5,
            "nombre": "Cotizado / Cotización",
            "razon": "Propuesta comercial enviada y en espera de respuesta.",
            "automatizacion": "Si es cotización manual, debes dar clic a 'Cotización realizada' para programar el bot de seguimiento de 21h. Si no responde en 2h, se ofrece 5% de descuento.",
            "deber_vendedor": "Enviar propuesta en PDF y dar clic obligatoriamente al botón manual 'Cotización realizada'."
        },
        {
            "num": 6,
            "nombre": "Seguimiento Automático",
            "razon": "Etapa para prospectos inactivos tras 45 horas de silencio desde la cotización.",
            "automatizacion": "Envía recordatorio a las 21h. A las 24h más sin respuesta, el sistema lo mueve aquí y asigna tag 'Sin respuesta'.",
            "deber_vendedor": "Monitorear y realizar llamadas telefónicas para recuperar la venta."
        },
        {
            "num": 7,
            "nombre": "Campañas Frío",
            "razon": "Leads de campañas masivas que no respondieron o no mostraron interés.",
            "automatizacion": "Se mueven aquí de forma masiva si no interactúan con el recontacto.",
            "deber_vendedor": "Mantenerlos en esta etapa para futuras campañas de promociones masivas."
        },
        {
            "num": 8,
            "nombre": "Campañas Caliente",
            "razon": "Leads reactivados por campañas masivas que sí muestran interés.",
            "automatizacion": "Si responde el mensaje de campaña, el sistema lo mueve aquí automáticamente.",
            "deber_vendedor": "Dar atención prioritaria inmediata y enviar cotización para cerrar la venta."
        },
        {
            "num": 9,
            "nombre": "Programado",
            "razon": "Venta ganada en espera de la fecha de entrega del baño.",
            "automatizacion": "Detiene seguimientos en espera del clic de entrega física.",
            "deber_vendedor": "Asegurar cobro de garantía/renta y coordinar logística con operaciones."
        },
        {
            "num": 10,
            "nombre": "Baño Entregado / Ganados",
            "razon": "El baño ha sido entregado en el sitio del cliente.",
            "automatizacion": "Se debe usar preferentemente el botón 'Baño entregado y ganado' de la tarjeta porque activa más automatizaciones que el botón normal.",
            "deber_vendedor": "Mover el lead a Ganados y dar clic obligatoriamente al botón manual 'Baño entregado y ganado'."
        },
        {
            "num": 11,
            "nombre": "En Pausa / Pausado",
            "razon": "Leads viables que indicaron requerir el servicio dentro de 1 mes o más.",
            "automatizacion": "Detiene alertas y recordatorios automáticos.",
            "deber_vendedor": "Agendar tarea de seguimiento futuro en el calendario."
        },
        {
            "num": 12,
            "nombre": "Ganado cliente reactiva",
            "razon": "Etapa permanente de residencia para clientes ya ganados que se reactivaron por cualquier motivo.",
            "automatizacion": "Si el cliente ya en Ganados escribe de nuevo, al finalizar la conversación reactivada se le mueve a esta etapa para vivir de ahí en adelante.",
            "deber_vendedor": "Mover el lead a esta etapa al finalizar/resolver su conversación reactivada."
        },
        {
            "num": 13,
            "nombre": "Solicitud Retiro",
            "razon": "El cliente solicita el retiro físico del sanitario del sitio.",
            "automatizacion": "El bot da instrucciones de enviar correo a operaciones y envía la encuesta de emojis.",
            "deber_vendedor": "Validar correo de retiro y reportar a logística para recolección física."
        },
        {
            "num": 14,
            "nombre": "Quejas sin resolver",
            "razon": "Reportes e inconformidades de baños.",
            "automatizacion": "La conversación se traslada de inmediato al Embudo de Quejas Sanitarios (Pipeline 12717196) en 'INICIO QUEJA'.",
            "deber_vendedor": "Dar seguimiento urgente y reportar a soporte técnico para resolución inmediata."
        },
        {
            "num": 15,
            "nombre": "Perdido Reactivable",
            "razon": "Leads idóneos no cerrados, candidatos para futuras promociones.",
            "automatizacion": "Clasificación y guardado bajo etiquetas de archivado comercial.",
            "deber_vendedor": "Documentar la objeción en los campos de la tarjeta."
        },
        {
            "num": 16,
            "nombre": "Perdidos",
            "razon": "Servicios concluidos o clientes con competidores.",
            "automatizacion": "Finaliza el seguimiento del bot.",
            "deber_vendedor": "Archivar y registrar causa de pérdida."
        },
        {
            "num": 17,
            "nombre": "Cerrado",
            "razon": "Leads no potenciales (fuera de zona, proveedores, spam, empleos).",
            "automatizacion": "El bot archiva automáticamente prospectos inviables.",
            "deber_vendedor": "Monitorear descartes de forma ocasional."
        }
    ]
    
    render_pipeline_grid(etapas_banos)

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
            <div class="metric-subtitle">Responsable de fosas sépticas, lodos e industriales.</div>
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
    render_unified_guides(sections)
    
    with st.expander("❓ Preguntas y Respuestas (Q&A) de la Guía de Ventas"):
        st.markdown(sections.get("qa", ""))
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Specific guide section
    st.markdown(sections.get("seccion_fosas", ""))
    
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📊 Tablero Visual de Etapas del Embudo (Fosas Sépticas)")
    st.markdown("El embudo se compone de **13 etapas** secuenciales en el orden exacto de Kommo CRM. Cada columna representa una etapa individual en orden de flujo comercial. Haz clic en cada tarjeta para ver su detalle:")
    
    etapas_fosas = [
        {
            "num": 1,
            "nombre": "Contacto Inicial",
            "razon": "Primer contacto de prospectos que seleccionaron 'Servicios especiales' -> 'Fosas'.",
            "automatizacion": "El bot pregunta tipo de residuo, estado del material, almacenamiento y volumen. Envía el PDF de presentación de Saniglobal y lo asigna a Livier Mora.",
            "deber_vendedor": "Monitorear que el lead califique correctamente y no se trabe en el bot."
        },
        {
            "num": 2,
            "nombre": "CASA HABITACIÓN (Filtro Crítico)",
            "razon": "Filtro crítico de exclusión. Saniglobal no atiende domicilios residenciales/particulares en este embudo.",
            "automatizacion": "El bot pregunta si es casa residencial. Si es 'Sí', asigna el tag 'CASA HABITACIÓN', envía mensaje de rechazo cortés y lo mueve automáticamente a Cerrado.",
            "deber_vendedor": "Ninguno comercial (el bot descarta de forma automática)."
        },
        {
            "num": 3,
            "nombre": "Solicitud de Información",
            "razon": "Validación técnica de los datos del residuo e información fiscal antes de formular propuesta.",
            "automatizacion": "El bot solicita datos técnicos complementarios.",
            "deber_vendedor": "Validar los requerimientos de sitio, accesos de camión y manguera."
        },
        {
            "num": 4,
            "nombre": "Visita de Diagnóstico",
            "razon": "Proyectos complejos donde es necesario verificar físicamente el sitio antes de cotizar.",
            "automatizacion": "Pausa las automatizaciones mientras se realiza la visita.",
            "deber_vendedor": "Programar fecha y hora para que el personal técnico acuda al diagnóstico en sitio."
        },
        {
            "num": 5,
            "nombre": "Apoyo Humano Fosas",
            "razon": "Prospectos que requieren atención humana directa o donde el bot se detiene por respuestas no clasificadas.",
            "automatizacion": "Se detiene el bot y genera tarea urgente a Livier Mora.",
            "deber_vendedor": "Retomar la conversación de forma manual e inmediata."
        },
        {
            "num": 6,
            "nombre": "Cotización",
            "razon": "Propuesta formulada y enviada a revisión del cliente.",
            "automatizacion": "Cotización siempre manual. Es obligatorio presionar el botón 'Cotización realizada' para configurar el bot de seguimiento de 21h.",
            "deber_vendedor": "Enviar cotización en PDF y dar clic obligatoriamente en el botón manual 'Cotización realizada'."
        },
        {
            "num": 7,
            "nombre": "Seguimiento",
            "razon": "Seguimiento a propuestas no contestadas.",
            "automatizacion": "A las 21 horas envía seguimiento. Si la objeción es precio, el bot ofrece un cupón del 5% y etiqueta como 'Perdido por precio'.",
            "deber_vendedor": "Realizar llamada telefónica para empujar el cierre del servicio."
        },
        {
            "num": 8,
            "nombre": "En Pausa",
            "razon": "Clientes que sí quieren el servicio pero lo requieren dentro de 1 mes o más.",
            "automatizacion": "Detiene recordatorios de chat diarios.",
            "deber_vendedor": "Programar tarea de seguimiento en calendario para la fecha de interés."
        },
        {
            "num": 9,
            "nombre": "CLIENTE ACTUAL (Reactivación y Quejas)",
            "razon": "Reactivación y resolución local de inconformidades para clientes ganados que vuelven a escribir.",
            "automatizacion": "El bot despliega menú interactivo. REGLA CRÍTICA DE QUEJAS: En Fosas las quejas NO se mandan a otro embudo. Livier debe resolver de forma local en esta etapa agregando manualmente la etiqueta 'Queja'.",
            "deber_vendedor": "Atender requerimientos de servicios adicionales o gestionar soporte local de quejas con el tag 'Queja'."
        },
        {
            "num": 10,
            "nombre": "Clientes SLP",
            "razon": "Control geográfico interno para leads que corresponden a la zona de San Luis Potosí.",
            "automatizacion": "Separa el flujo comercial para operaciones de SLP.",
            "deber_vendedor": "Coordinar con el equipo regional de operaciones en SLP para logística y precios aplicables."
        },
        {
            "num": 11,
            "nombre": "GANADOS",
            "razon": "Servicio comercial ejecutado, facturado y cobrado con éxito.",
            "automatizacion": "Cierra ciclo de ventas inicial y programa ventana de reactivación.",
            "deber_vendedor": "Mover el lead a GANADOS y asegurar que se documente el pago."
        },
        {
            "num": 12,
            "nombre": "PERDIDOS",
            "razon": "Prospectos comerciales que decidieron contratar con la competencia o no procedieron.",
            "automatizacion": "Detiene flujos de seguimiento automático.",
            "deber_vendedor": "Registrar la causa de pérdida (objeción de precio, cobertura, etc.)."
        },
        {
            "num": 13,
            "nombre": "CERRADOS NO POTENCIAL",
            "razon": "Leads residenciales descartados o contactos no comerciales (proveedores, spam).",
            "automatizacion": "Mueve a cerrado a leads filtrados automáticamente por el bot.",
            "deber_vendedor": "Validar ocasionalmente que no haya leads comerciales válidos aquí."
        }
    ]
    
    render_pipeline_grid(etapas_fosas)

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
            <div class="metric-subtitle">Responsable del pipeline de mantenimiento y succión de grasas alimenticias.</div>
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
    render_unified_guides(sections)
    
    with st.expander("❓ Preguntas y Respuestas (Q&A) de la Guía de Ventas"):
        st.markdown(sections.get("qa", ""))
        
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Specific guide section
    st.markdown(sections.get("seccion_trampas", ""))
    
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📊 Tablero Visual de Etapas del Embudo (Trampas de Grasa)")
    st.markdown("El embudo se compone de **8 etapas** secuenciales en el orden exacto de Kommo CRM. Cada columna representa una etapa individual en orden de flujo comercial. Haz clic en cada tarjeta para ver su detalle:")
    
    etapas_trampas = [
        {
            "num": 1,
            "nombre": "Contacto Inicial",
            "razon": "Primer contacto para desazolve y limpieza de trampas de grasa en restaurantes y comedores.",
            "automatizacion": "El bot pregunta número de trampas, capacidad (lts), material, tipo de acceso, distancia de manguera y rampas. Solicita fotos/videos.",
            "deber_vendedor": "Monitorear que el cliente preocione los datos técnicos y multimedia solicitados."
        },
        {
            "num": 2,
            "nombre": "Apoyo Humano",
            "razon": "El cliente requiere asistencia directa del asesor o ingresó respuestas que el bot no pudo clasificar.",
            "automatizacion": "Detiene el bot y crea tarea comercial urgente al asesor de trampas.",
            "deber_vendedor": "Tomar la conversación en el chat de forma inmediata para resolver y cotizar."
        },
        {
            "num": 3,
            "nombre": "COTIZACIÓN (Auto vs Manual)",
            "razon": "Envío de propuesta de limpieza al cliente.",
            "automatizacion": "Si es 1 o 2 trampas estándar de 200 LTS, el bot cotiza automáticamente vía webhook. Si supera el estándar (más trampas o más litros), el asesor debe cotizar manualmente por fuera y presionar el botón 'Cotización de trampas de grasa manual'.",
            "deber_vendedor": "Si la cotización es manual, enviarla en PDF y hacer clic obligatoriamente en el botón 'Cotización de trampas de grasa manual'."
        },
        {
            "num": 4,
            "nombre": "En Seguimiento",
            "razon": "Seguimiento automático a las cotizaciones enviadas.",
            "automatizacion": "A las 21 horas envía mensaje. Si la objeción es precio, el bot ofrece descuento de 5% y etiqueta como 'Perdido por precio'. REGLA CRÍTICA DE QUEJAS: Las quejas de trampas NO se mandan a otro embudo. El asesor debe colocar manualmente la etiqueta 'Queja' y resolver directamente en la etapa actual.",
            "deber_vendedor": "Realizar llamada para negociar y cerrar el servicio."
        },
        {
            "num": 5,
            "nombre": "En Pausa",
            "razon": "Servicios viables proyectados a más de 1 mes de distancia.",
            "automatizacion": "Detiene flujos de seguimiento diario.",
            "deber_vendedor": "Agendar tarea de seguimiento en calendario para la fecha futura."
        },
        {
            "num": 6,
            "nombre": "Perdido Reactivable",
            "razon": "Prospectos idóneos no cerrados por precio o agenda, archivados para futuras campañas masivas.",
            "automatizacion": "Se clasifican comercialmente para campañas futuras.",
            "deber_vendedor": "Asegurar que los datos de contacto y objeciones queden registrados."
        },
        {
            "num": 7,
            "nombre": "Perdidos",
            "razon": "Servicios eventuales de limpieza concluidos con éxito o clientes con competidores.",
            "automatizacion": "Detiene seguimientos automáticos.",
            "deber_vendedor": "Archivar y registrar causa de pérdida."
        },
        {
            "num": 8,
            "nombre": "Cerrado",
            "razon": "Solicitudes inviables, spam, proveedores o vacantes de empleo.",
            "automatizacion": "El bot archiva automáticamente prospectos descartados.",
            "deber_vendedor": "Monitorear descartes ocasionalmente."
        }
    ]
    
    render_pipeline_grid(etapas_trampas)

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
