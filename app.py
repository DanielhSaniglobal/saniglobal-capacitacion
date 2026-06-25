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
    st.session_state.theme = "dark"

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
                3. Guarda la tarjeta. El sistema se encarga de reasignar tareas pendientes y mandar alertas automáticas.
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
                
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Interactive Bot Simulator
    st.markdown("#### 🤖 Simulador de Calificación (Bot de Renta)")
    st.markdown("Prueba el cuestionario interactivo que realiza el bot al cliente para cotizar de forma automática:")
    
    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        tipo_uso = st.radio("¿Para obra de construcción o evento?", ["Construcción", "Evento"])
        cant_baños = st.number_input("¿Cuántos baños necesita?", min_value=1, max_value=10, value=1)
        tipo_ban = st.selectbox("¿Qué tipo de baño?", ["Sencillo", "Con lavamanos"])
    with col_sim2:
        tiempo = st.selectbox("¿Por cuánto tiempo?", ["Por mes", "Por quincena", "Por día (Eventos)", "Por semana"])
        ubicacion = st.radio("¿Ubicación del servicio?", ["ZM Guadalajara / ZM San Luis Potosí", "Otro Municipio/Estado"])
    
    if st.button("Procesar Simulación (Calificar Lead)"):
        st.markdown("##### Resultado del Filtro del Bot:")
        if cant_baños >= 3:
            st.markdown(f'<div class="badge badge-amber">ASIGNAR A ASESOR</div>', unsafe_allow_html=True)
            st.write("⚠️ El bot no cotiza de forma automática a partir de 3 baños. Se crea una tarea urgente para **Daniel Herrera** para cotizar manualmente.")
        elif ubicacion == "Otro Municipio/Estado":
            st.markdown(f'<div class="badge badge-red">NO VIABLE (CERRADO)</div>', unsafe_allow_html=True)
            st.write("❌ Fuera de nuestra zona de cobertura. El bot colocará la etiqueta correspondente y moverá el lead a la etapa **Cerrado** automáticamente.")
        else:
            st.markdown(f'<div class="badge badge-green">COTIZAR AUTOMÁTICAMENTE</div>', unsafe_allow_html=True)
            st.write("✅ Los datos son viables. El bot dispara el webhook, envía la cotización en PDF y mueve el lead a la etapa de **Cotización**.")
            st.write("💡 *Recuerda: si por alguna razón la cotizas manual, debes darle clic al botón 'Cotización realizada' en Kommo.*")

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
                
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Simulator of Casa Habitación Filter
    st.markdown("#### 🏠 Simulador de Filtro Crítico de Exclusión Residencial")
    st.markdown("Simula qué sucede cuando ingresa un lead a este embudo y responde a la pregunta de tipo de propiedad:")
    
    es_residencial = st.radio("¿Es para una casa habitacional o residencial?", ["Sí", "No"], index=1)
    
    if st.button("Verificar Tipo de Propiedad"):
        if es_residencial == "Sí":
            st.markdown(f"""
            <div class="custom-card red-border-card">
                <span class="badge badge-red">Lead Excluido</span>
                <p style="margin-top: 0.5rem; font-size: 0.85rem;">
                    <strong>Acción Automática:</strong> El bot pone el tag <code>CASA HABITACIÓN</code> y manda el mensaje:<br>
                    <i>'Una disculpa, por el momento no estamos brindando servicios para casa habitación ni domicilios particulares...'</i><br>
                    <strong>Destino:</strong> El lead se mueve automáticamente a <strong>Cerrado</strong>.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="custom-card accent-border-card">
                <span class="badge badge-green">Lead Viable</span>
                <p style="margin-top: 0.5rem; font-size: 0.85rem;">
                    <strong>Acción Automática:</strong> El bot continúa solicitando información técnica (ej. metros de manguera, acceso de camión) para proceder a la cotización o visita de diagnóstico por parte de <strong>Livier Mora</strong>.
                </p>
            </div>
            """, unsafe_allow_html=True)

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
                
    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    
    # Auto vs Manual Simulator for Trampas
    st.markdown("#### ⚙️ Simulador de Cotización de Trampas")
    st.markdown("Establece las condiciones del servicio para verificar si se cotiza de forma automática:")
    
    num_trampas = st.selectbox("Número de trampas a limpiar:", ["1 trampa", "2 trampas", "3 o más trampas"])
    capacidad_trampa = st.selectbox("Capacidad promedio de las trampas:", ["200 LTS (estándar)", "De 250 a 500 LTS", "Más de 500 LTS"])
    
    if st.button("Verificar Tipo de Cotización"):
        if num_trampas in ["1 trampa", "2 trampas"] and capacidad_trampa == "200 LTS (estándar)":
            st.markdown(f"""
            <div class="custom-card accent-border-card">
                <span class="badge badge-green">🤖 Cotización Automática</span>
                <p style="margin-top: 0.5rem; font-size: 0.85rem;">
                    El bot procesa el webhook de forma automática, genera el enlace y le entrega la cotización al cliente al instante. El lead se mueve a <strong>Cotización</strong> solo.
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="custom-card amber-border-card">
                <span class="badge badge-amber">👤 Cotización Manual</span>
                <p style="margin-top: 0.5rem; font-size: 0.85rem;">
                    Las condiciones superan el estándar automático. El asesor debe cotizar manualmente por fuera y presionar el botón <strong>'Cotización de trampas de grasa manual'</strong> en Kommo CRM para que el lead se mueva a la etapa de Cotización y se active el seguimiento.
                </p>
            </div>
            """, unsafe_allow_html=True)

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
            # copy button (Streamlit has st.code which has built-in copy helper, let's use that as well)
            st.code(tmpl["texto"], language="text")
            st.markdown("<br>", unsafe_allow_html=True)
            
    if not filtered_templates:
        st.info("No se encontraron plantillas con ese criterio de búsqueda.")

    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 🔗 Enlaces y Herramientas Oficiales de Kommo")
    st.markdown("Consulta la documentación y herramientas oficiales de Kommo CRM para resolver dudas adicionales de la plataforma:")
    
    col_link1, col_link2 = st.columns(2)
    with col_link1:
        st.markdown(f"""
        <div class="custom-card accent-border-card" style="margin-bottom: 1rem;">
            <strong>📚 Base de Conocimientos de Kommo</strong>
            <p style="font-size: 0.8rem; margin-top: 0.5rem; color: {text_muted};">Manuales, guías paso a paso de configuración, facturación, cuentas y canales.</p>
            <a href="https://www.kommo.com/es/recursos/" target="_blank" style="font-size: 0.85rem; font-weight: bold; color: {accent_color}; text-decoration: none;">Visitar Documentación ↗</a>
        </div>
        <div class="custom-card accent-border-card" style="margin-bottom: 1rem;">
            <strong>📲 Generador de Enlaces de WhatsApp</strong>
            <p style="font-size: 0.8rem; margin-top: 0.5rem; color: {text_muted};">Crea enlaces de WhatsApp (wa.me) y códigos QR personalizados para tus campañas de recontacto comercial.</p>
            <a href="https://www.kommo.com/es/como-crear-un-enlace-de-whatsapp/" target="_blank" style="font-size: 0.85rem; font-weight: bold; color: {accent_color}; text-decoration: none;">Crear Enlace ↗</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col_link2:
        st.markdown(f"""
        <div class="custom-card accent-border-card" style="margin-bottom: 1rem;">
            <strong>💰 Calculadora de Precios de WhatsApp</strong>
            <p style="font-size: 0.8rem; margin-top: 0.5rem; color: {text_muted};">Calcula el costo exacto de tus mensajes y conversaciones de WhatsApp Business por país.</p>
            <a href="https://www.kommo.com/es/calculadora-precios-whatsapp/" target="_blank" style="font-size: 0.85rem; font-weight: bold; color: {accent_color}; text-decoration: none;">Calcular Costos ↗</a>
        </div>
        <div class="custom-card accent-border-card" style="margin-bottom: 1rem;">
            <strong>🤖 Automatización de Ventas (Salesbot)</strong>
            <p style="font-size: 0.8rem; margin-top: 0.5rem; color: {text_muted};">Aprende cómo funciona el Salesbot oficial de Kommo y cómo configurarlo paso a paso.</p>
            <a href="https://www.kommo.com/es/salesbot/" target="_blank" style="font-size: 0.85rem; font-weight: bold; color: {accent_color}; text-decoration: none;">Ver Guía de Bots ↗</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='h-divider'></div>", unsafe_allow_html=True)
    st.markdown("### 📖 Guías Prácticas de Operación en Kommo")
    st.markdown("Sigue estas instrucciones para dominar las herramientas diarias del CRM:")

    with st.expander("⚡ 1. Cómo usar y crear Respuestas Rápidas (Mensajes Rápidos)"):
        st.markdown("""
        **¿Qué son?**  
        Son plantillas de texto predefinidas para responder preguntas comunes (números de cuenta, documentos, precios) en segundos.
        
        **Cómo usarlas en el chat:**  
        1. En el cuadro de chat de un lead, escribe una barra diagonal `/`.
        2. Escribe una palabra clave del título o texto de la plantilla (ej. `/pago` o `/requisitos`).
        3. El sistema te mostrará una lista de sugerencias. Presiona `Enter` para cargar el texto y envíalo.
        
        **Cómo crearlas o editarlas:**  
        1. Ve a **Ajustes** (icono de engranaje) → **Mensajes rápidos**.
        2. Haz clic en **Añadir plantilla**.
        3. Escribe un título y el cuerpo del mensaje.
        4. Puedes usar variables dinámicas (como `{{contact.name}}` para el nombre o `{{lead.id}}` para el ID del lead) para personalizar el texto automáticamente.
        """, unsafe_allow_html=True)

    with st.expander("🤖 2. Cómo usar y activar Respuestas Automáticas (Salesbot)"):
        st.markdown("""
        **¿Qué es?**  
        Es nuestro bot inteligente que califica leads, envía cotizaciones y asigna tareas.
        
        **Cómo activar un bot de forma manual:**  
        1. Si deseas que el bot recopile datos por ti o envíe una cotización a un cliente asignado, abre la tarjeta del lead.
        2. En el menú de la derecha, busca la sección **Salesbot**.
        3. Elige el flujo de bot deseado (ej. *De solicitud a cotizado* o *Apoyo humano*) y presiona **Ejecutar**.
        
        **Cómo evitar interferir con los bots:**  
        * Mientras estés chateando activamente con el cliente, el lead debe estar en la etapa de **Embudo Caliente** (aquí los bots están apagados).
        * Cuando termines de chatear y le envíes la propuesta, recuerda moverlo a la etapa **Cotización** y dar clic en el botón **Cotización realizada**. Esto activará correctamente los recordatorios automáticos de 21 horas.
        """, unsafe_allow_html=True)

    with st.expander("⏱️ 3. Cómo reabrir la Ventana de 24 horas de Meta (WhatsApp)"):
        st.markdown("""
        **¿Qué es la regla de las 24 horas?**  
        Meta (dueña de WhatsApp) prohíbe enviar mensajes libres a los clientes si han pasado más de 24 horas desde que ellos nos enviaron su último mensaje.
        
        **Cómo volver a contactar al cliente si la ventana se cerró:**  
        1. Abre el chat del lead en Kommo. Verás una alerta de que la ventana está cerrada.
        2. Haz clic en el botón de **Plantillas de WhatsApp (HSM)** en el chat.
        3. Selecciona una plantilla oficial aprobada (ej. de seguimiento o recordatorio de pago).
        4. Completa los campos dinámicos si se requiere y envíala.
        5. **Reapertura:** En cuanto el cliente responda a tu plantilla (presionando un botón o escribiendo algo), la ventana se abrirá y podrás chatear libremente de nuevo por otras 24 horas.
        """, unsafe_allow_html=True)

    with st.expander("📅 4. Gestión de Tareas y Alertas (Regla de Oro)"):
        st.markdown("""
        **La Regla de Oro:**  
        *“Ningún lead activo debe quedarse sin una tarea pendiente.”* Si un lead no tiene tarea, significa que se encuentra en el olvido y no recibirá seguimiento.
        
        **Cómo programar una tarea:**  
        1. En la parte inferior de la tarjeta del lead, haz clic en **Añadir tarea**.
        2. Selecciona la fecha y hora límite de tu recordatorio (ej. Mañana a las 9:00 am).
        3. Escribe una nota clara de lo que debes hacer (ej. *'Llamar para confirmar dirección de entrega'* o *'Revisar si enviaron comprobante'*).
        4. Selecciona el tipo de tarea (`Llamada`, `Seguimiento`, `Reunión`).
        5. Guarda la tarea. Kommo te enviará notificaciones visuales y sonoras en el navegador y en la app móvil.
        """, unsafe_allow_html=True)

    with st.expander("🗂️ 5. Cómo usar Tareas, Notas y Siguientes para tu beneficio"):
        st.markdown("""
        **El trío dinámico de Kommo: Organiza tu día y vende más**
        
        ### 📅 A. Las Tareas (Tasks)
        * **Qué son:** Recordatorios de acciones comerciales con fecha, hora y responsable.
        * **Cómo te benefician:** 
          - Al iniciar el día, ve a la sección de **Tareas** para ver tu lista diaria ordenada por hora. 
          - Libera espacio mental: en lugar de intentar recordar a quién llamar, agenda la tarea y deja que el CRM te notifique.
          - Si una tarea vence, se pondrá en rojo en tu tablero comercial. Mantener tareas en rojo indica un mal seguimiento de leads.
        
        ### ✍️ B. Las Notas (Notes)
        * **Qué son:** Comentarios estáticos escritos en el historial del lead.
        * **Qué debes registrar en las Notas:**
          - Acuerdos especiales de precio, requerimientos especiales del sitio (ej. *'Calle angosta, se requiere camión chico'*).
          - Datos de contacto secundarios (ej. *'Nombre de la secretaria: Patricia'*).
          - Historial de llamadas breves (ej. *'Se marcó pero mandó a buzón, reintentar tarde'*).
        * **Cómo te benefician:** 
          - Todo tu equipo tendrá acceso al mismo historial. Si sales de vacaciones, un compañero puede retomar el lead leyendo las notas sin molestar al cliente.
          - Generas confianza en el cliente al recordar detalles específicos de llamadas anteriores.
        
        ### 🔄 C. El "Siguiente" (Siguiente Paso)
        * **Qué es:** La regla operativa de programar la próxima acción inmediatamente al terminar la actual. Al marcar una tarea como 'Completada', Kommo te preguntará automáticamente: *¿Cuál es el siguiente paso?*.
        * **Cómo te beneficia:** 
          - Evita que los leads se queden estancados. Cada interacción con el cliente debe tener una consecuencia en el tiempo para mover el lead hacia la etapa de **Ganados**.
        """, unsafe_allow_html=True)

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
