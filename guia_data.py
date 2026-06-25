# -*- coding: utf-8 -*-

GLOSARIO = {
    "Lead / Prospecto": "Cualquier persona o empresa que nos contacta por primera vez a través de nuestros canales digitales.",
    "Embudo (Pipeline)": "El proceso de ventas estructurado en etapas secuenciales por el que transita un prospecto.",
    "Etapa (Estatus)": "La fase específica de negociación en la que se encuentra el cliente dentro de un embudo.",
    "Bot / Automatización": "Secuencia de mensajes y acciones lógicas ejecutadas por el sistema sin intervención humana.",
    "Etiqueta (Tag)": "Marcas de color añadidas a la tarjeta del cliente para filtrado rápido, campañas o disparar automatizaciones.",
    "Webhook": "Una solicitud HTTP automática enviada por el bot para conectarse con microservicios externos (ej. cotizadores automáticos).",
    "Ventana de 24h": "Regla de Meta que limita el envío de mensajes libres a 24 horas desde la última interacción del usuario.",
    "Mensaje rápido": "Plantillas de texto predefinidas en el chat de Kommo que se invocan con la tecla '/' para agilizar la comunicación.",
    "Casa Habitación": "Etiqueta y filtro aplicado por el bot para descartar y cerrar solicitudes residenciales no cubiertas en servicios especiales."
}

EMBUDOS_INFO = {
    "baños": {
        "responsable": "Daniel Herrera",
        "descripcion": "Embudo enfocado en la renta de sanitarios portátiles para obras y eventos.",
        "etapas": [
            {
                "nombre": "📥 Solicitud de Cotización",
                "descripcion": "El lead entra aquí al seleccionar 'Rentar baños'. El bot recopila de forma automática: uso (obra o evento), cantidad de baños (hasta 3), tipo de baño (sencillo o con lavamanos), duración y dirección física.",
                "detalles": "Si el cliente solicita 3 o más baños o envía un pin de ubicación inválido repetidamente, se asigna directamente a Daniel Herrera para seguimiento humano."
            },
            {
                "nombre": "🌡️ Embudo Caliente",
                "descripcion": "El cliente está respondiendo activamente en el chat.",
                "detalles": "Regla crítica: El bot no envía mensajes automatizados de seguimiento aquí para no entorpecer ni empalmarse con la conversación en vivo del asesor."
            },
            {
                "nombre": "ℹ️ Solicitud de Información",
                "descripcion": "Paso intermedio de validación de datos del cliente antes de cotizar."
            },
            {
                "nombre": "💰 Cotización",
                "descripcion": "El bot (por webhook) o el asesor envían la cotización en PDF y ponen el tag 'Propuesta enviada'.",
                "detalles": "¡Importante! Si la cotización es manual, debes dar clic al botón 'Cotización realizada'. Si no responde en 2h, se activa el bot de descuento automático del 5%."
            },
            {
                "nombre": "📞 En Seguimiento",
                "descripcion": "A las 21 horas post-cotización sin respuesta, el sistema manda un mensaje de seguimiento preguntando si están evaluando opciones, desean contratar o cancelan.",
                "detalles": "Si cancelan por precio alto, el bot envía un cupón de 10% de descuento como último recurso y pone el tag 'Perdido por precio'."
            },
            {
                "nombre": "📅 Programado",
                "descripcion": "Venta ganada en espera de la fecha acordada para que el equipo de operaciones entregue el baño."
            },
            {
                "nombre": "🚪 Baño Entregado",
                "descripcion": "El baño se entregó físicamente. El asesor debe dar clic en el botón 'Baño entregado'.",
                "detalles": "Al dar clic, se activa la encuesta post-servicio con emojis (☹️, 😐, 😄) y se prepara al cliente para recibir un cupón de reactivación del 10% cuando finalice la renta."
            },
            {
                "nombre": "⏸️ Pausado",
                "descripcion": "Prospectos viables pero que requieren el servicio hasta dentro de 1 mes o más."
            },
            {
                "nombre": "🔴 Perdido Reactivable",
                "descripcion": "El lead no cerró por precio o agenda, pero es cliente ideal. Se guarda para campañas de promociones futuras."
            },
            {
                "nombre": "❌ Perdidos",
                "descripcion": "Clientes que completaron un servicio eventual que ya terminó, o que contrataron con la competencia."
            },
            {
                "nombre": "🚫 Cerrado",
                "descripcion": "Prospectos que no aplican (fuera de zona de cobertura, proveedores, spam, solicitudes de empleo)."
            }
        ]
    },
    "fosas": {
        "responsable": "Livier Mora",
        "descripcion": "Limpieza de fosas sépticas, lodos estables, pozos de absorción y residuos líquidos industriales.",
        "etapas": [
            {
                "nombre": "📥 Solicitud de Cotización",
                "descripcion": "El bot pregunta por tipo de residuo, estado del material (líquido, lodo, sólido), almacenamiento (fosa, cisterna, tambo, sobre terreno) y volumen (hasta 5,000L, 5k-10k, más de 10k).",
                "detalles": "Se envía la presentación de Saniglobal en PDF."
            },
            {
                "nombre": "🏠 Filtro de Casa Habitación (Exclusión)",
                "descripcion": "El bot pregunta obligatoriamente: ¿Es para una casa habitacional o residencial?",
                "detalles": "Si es 'Sí', el bot pone la etiqueta 'CASA HABITACIÓN', envía un mensaje de disculpa y lo mueve automáticamente a Cerrado. Saniglobal solo atiende sector comercial o industrial para estos servicios."
            },
            {
                "nombre": "🔎 Visita de Diagnóstico",
                "descripcion": "Paso para proyectos complejos donde Livier programa una visita técnica en sitio antes de cotizar."
            },
            {
                "nombre": "💰 Cotización",
                "descripcion": "La cotización en este embudo siempre se elabora de manera manual.",
                "detalles": "Es obligatorio que el asesor presione el botón 'Cotización realizada' al enviar la propuesta para que se dispare el bot de seguimiento de 21h."
            },
            {
                "nombre": "📞 En Seguimiento",
                "descripcion": "A las 21 horas se envía mensaje de seguimiento. Si la objeción es precio, el bot ofrece un 5% de descuento máximo y etiqueta como 'Perdido por precio'."
            },
            {
                "nombre": "⏸️ Pausado",
                "descripcion": "Clientes comerciales que sí quieren el servicio pero lo necesitan dentro de más de 1 mes.",
                "detalles": "Se mueven aquí para mantener limpio el tablero diario."
            },
            {
                "nombre": "🔴 Perdido Reactivable",
                "descripcion": "Prospectos ideales que no cerraron por precio o agenda. Se guardan para futuras campañas de reactivación comercial."
            },
            {
                "nombre": "❌ Perdidos",
                "descripcion": "Servicios eventuales concluidos, o clientes que contrataron con la competencia."
            },
            {
                "nombre": "🚫 Cerrado",
                "descripcion": "Prospectos no viables (fuera de zona, proveedores, spam, empleos, o casas habitación filtradas)."
            },
            {
                "nombre": "🔄 Reactivación (Cliente Actual)",
                "descripcion": "Si un cliente en 'Ganados' vuelve a escribir, el bot 'Ganados el cliente reactiva fosas' lo mueve a esta etapa (Cliente Actual) y le muestra un menú interactivo.",
                "detalles": "El menú ofrece: 'Solicitar servicio', 'Reportes y quejas' o 'Dudas del servicio'. Las tres opciones crean una tarea y notifican a Livier. Si es una queja, NO se manda a otro embudo; se debe etiquetar manualmente como 'Queja' y resolverse en esta misma etapa."
            }
        ]
    },
    "trampas": {
        "responsable": "Asesor de Trampas de Grasa",
        "descripcion": "Limpieza y mantenimiento de trampas de grasa para cocinas comerciales, restaurantes e industrias.",
        "etapas": [
            {
                "nombre": "📥 Solicitud de Cotización",
                "descripcion": "El bot realiza preguntas de calificación: número de trampas (1, 2, o 3+), capacidad (200L estándar, 250-500L, 500L+), material de la trampa, tipo de acceso, distancia de manguera necesaria y si cuenta con rampas.",
                "detalles": "Además, se le solicita fotos/videos de la trampa."
            },
            {
                "nombre": "💰 Cotización (Automática vs. Manual)",
                "descripcion": "Si es 1 o 2 trampas estándar de 200 LTS y se completaron los datos, se calcula y envía la propuesta automáticamente por un microservicio externo.",
                "detalles": "Si no cumple estas condiciones (ej. más capacidad o trampas), el asesor cotiza manualmente y presiona el botón 'Cotización de trampas de grasa manual' para continuar el flujo."
            },
            {
                "nombre": "📞 En Seguimiento",
                "descripcion": "Seguimiento automático a las 21 horas. Si hay objeción de precio, ofrece cupón del 5% y asigna el tag 'Perdido por precio'."
            },
            {
                "nombre": "⏸️ Pausado",
                "descripcion": "Servicios viables que se programarán a más de 1 mes en el futuro."
            },
            {
                "nombre": "🔴 Perdido Reactivable",
                "descripcion": "Prospectos ideales que no cerraron por precio o agenda. Se guardan para futuras campañas y promociones."
            },
            {
                "nombre": "❌ Perdidos",
                "descripcion": "Servicios eventuales que ya terminaron o que contrataron con competidores."
            },
            {
                "nombre": "🚫 Cerrado",
                "descripcion": "Solicitudes no viables (fuera de zona, proveedores, spam, empleos)."
            },
            {
                "nombre": "😤 Quejas y Soporte (Regla Especial)",
                "descripcion": "Cualquier inconformidad del cliente sobre el servicio de limpieza de trampas.",
                "detalles": "Regla de oro: No se transfieren a otro embudo. El asesor de trampas debe etiquetar el lead como 'Queja' y darle resolución directamente en la etapa en que se encuentre."
            }
        ]
    }
}

QUIZ_QUESTIONS = [
    {
        "question": "¿Quién es el usuario asignado por defecto para el embudo de renta de baños portátiles?",
        "options": ["Livier Mora", "Asesor de Trampas", "Daniel Herrera", "Cualquier usuario disponible"],
        "correct": 2,
        "explanation": "El sistema asigna automáticamente la renta de baños al usuario de Daniel Herrera (ID 12824423)."
    },
    {
        "question": "¿Qué ocurre automáticamente si un cliente cotizado en el embudo de baños no responde al bot en 2 horas?",
        "options": [
            "Se cierra la conversación por falta de respuesta.",
            "Se le ofrece un 5% de descuento automático y se agrega el tag '-5% descuento'.",
            "El sistema le hace una llamada telefónica por medio del bot.",
            "Se reasigna a otro vendedor disponible."
        ],
        "correct": 1,
        "explanation": "El bot 'De solicitud a cotizado' en baños está programado para enviar una oferta del 5% de descuento tras 2 horas de inactividad del cliente."
    },
    {
        "question": "Al enviar una cotización manual en Baños o Fosas, ¿por qué es obligatorio dar clic al botón 'Cotización realizada'?",
        "options": [
            "Para que el sistema facture el servicio de inmediato.",
            "Para marcar al cliente como ganado en el reporte de ventas.",
            "Para avisarle a operaciones que ya pueden entregar el baño.",
            "Para avisar al sistema que enviaste el precio, desactivar alertas de recordatorio y programar el bot de seguimiento de 21h."
        ],
        "correct": 3,
        "explanation": "Si no se presiona este botón, el CRM asume que nunca cotizaste, el cliente no recibirá seguimientos automáticos y se te asignará una tarea de alerta."
    },
    {
        "question": "¿Cuál es la política de Saniglobal respecto a la limpieza de fosas sépticas y desazolves en casas residenciales?",
        "options": [
            "Se cotiza con recargo del 50% por maniobra difícil.",
            "No se brinda servicio para casa habitación ni domicilios particulares en servicios especiales; el bot los rechaza de forma automática.",
            "Se atienden únicamente los fines de semana.",
            "Requiere aprobación por escrito del director comercial."
        ],
        "correct": 1,
        "explanation": "Saniglobal no realiza servicios residenciales para fosas o sondeo. El bot aplica la etiqueta 'CASA HABITACIÓN' y cierra el lead automáticamente."
    },
    {
        "question": "Si un cliente que estaba en estatus 'Ganados' (venta cerrada) vuelve a enviar un mensaje meses después, ¿qué ocurre?",
        "options": [
            "Se crea un lead duplicado en el embudo de solicitud de cotización.",
            "El mensaje es bloqueado por las políticas de Meta de 24 horas.",
            "El sistema lo mueve automáticamente a la etapa 'Cliente Actual' del embudo 'Ganados el cliente reactiva' para lanzarle el menú de opciones.",
            "Permanece en el estatus anterior y Daniel Herrera debe buscarlo manualmente."
        ],
        "correct": 2,
        "explanation": "El sistema tiene una pausa que se rompe cuando el cliente ganado escribe. Esto lo mueve al embudo de reactivación (tenga o no baño activo) para autogestionarse."
    },
    {
        "question": "¿De cuánto es el cupón de descuento que ofrece el bot de seguimiento en Fosas y Trampas si la objeción es el precio?",
        "options": ["5%", "10%", "15%", "No se ofrecen cupones en servicios especiales"],
        "correct": 0,
        "explanation": "A diferencia de baños (donde se ofrece 10%), en fosas y trampas el bot ofrece un cupón del 5% de descuento al detectar la objeción de precio."
    },
    {
        "question": "¿Bajo qué condiciones una trampa de grasa califica para cotización 100% automática por el bot?",
        "options": [
            "Siempre y cuando el cliente envíe fotos claras de la trampa.",
            "Únicamente si son 1 o 2 trampas con una capacidad estándar de 200 LTS.",
            "Cualquier trampa de hasta 1,000 LTS de capacidad en Jalisco.",
            "Todas las trampas se cotizan de forma automática en el sistema."
        ],
        "correct": 1,
        "explanation": "El microservicio solo cotiza automáticamente si son máximo 2 trampas de tamaño estándar (200 LTS). Tamaños mayores o más cantidad requieren cotización manual."
    }
]

MENSAJES_RAPIDOS = [
    {
        "titulo": "Saludo e Introducción General",
        "texto": "Mucho gusto, le saluda Saniglobal. ¿En qué le podemos servir hoy? ¿Busca renta de sanitarios portátiles o un servicio especializado (fosas, trampas de grasa, residuos)?"
    },
    {
        "titulo": "Pasos para Contratación (Baños)",
        "texto": "Para proceder a contratar requerimos:\n1. Constancia de Situación Fiscal (RFC)\n2. Comprobante de domicilio de entrega\n3. Identificación oficial del contratante\n4. Confirmación de pago inicial de renta y depósito en garantía."
    },
    {
        "titulo": "Formas de Pago Autorizadas",
        "texto": "Aceptamos las siguientes formas de pago:\n- Transferencia electrónica SPEI\n- Pago con tarjeta de crédito/débito vía CLIP\n- Depósito bancario en ventanilla\n- Retiro sin tarjeta en cajero BBVA."
    },
    {
        "titulo": "Rechazo de Servicio Residencial",
        "texto": "Una disculpa, por el momento no estamos brindando servicios para casa habitación ni domicilios particulares. Esperamos poder reactivar el servicio residencial pronto y nos pondremos en contacto. ¡Gracias por considerarnos!"
    },
    {
        "titulo": "Instrucciones de Solicitud de Retiro",
        "texto": "Para programar el retiro del equipo, por favor envíe un correo a operacionesgdl@saniglobal.com.mx detallando:\n- Nombre del cliente o razón social\n- Dirección exacta y fecha de retiro deseada\n- ID de servicio o folio de contrato."
    }
]
