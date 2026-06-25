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
        "descripcion": "Embudo enfocado en la renta de sanitarios portátiles para obras y eventos (17 etapas en total).",
        "etapas": [
            {
                "nombre": "📥 Solicitud de Cotización / Contacto Inicial",
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
                "nombre": "💰 Cotizado / Cotización",
                "descripcion": "El bot (por webhook) o el asesor envían la cotización en PDF y ponen el tag 'Propuesta enviada'.",
                "detalles": "¡Importante! Si la cotización es manual, debes dar clic al botón 'Cotización realizada'. Si no responde en 2h, se activa el bot de descuento automático del 5%."
            },
            {
                "nombre": "🤖 Seguimiento Automático",
                "descripcion": "Los prospectos llegan a esta etapa de forma 100% automatizada.",
                "detalles": "Circunstancias de llegada: Cuando se envía una cotización, el bot espera 21 horas. Si el cliente no responde en ese lapso, el bot envía un mensaje automático de seguimiento. Si pasan otras 24 horas y el cliente sigue en silencio, el sistema lo mueve de forma automática a esta etapa y le asigna la etiqueta 'Sin respuesta'. Esto sirve para mantener limpio el estatus de 'Cotizado' de la bandeja del asesor."
            },
            {
                "nombre": "❄️ Campañas Frío",
                "descripcion": "Etapa diseñada para leads inactivos o antiguos a los que se les envía una campaña masiva de recontacto.",
                "detalles": "Se colocan aquí aquellos leads de campañas masivas que NO responden al mensaje enviado o no muestran interés."
            },
            {
                "nombre": "🔥 Campañas Caliente",
                "descripcion": "Leads reactivados mediante campañas que sí interactúan.",
                "detalles": "Si un lead al que se le envió el mensaje de campaña sí responde y muestra interés en contratar nuevamente, el sistema lo mueve automáticamente a esta etapa para que Daniel Herrera le brinde atención prioritaria para cerrar la venta."
            },
            {
                "nombre": "📅 Programado",
                "descripcion": "Venta ganada en espera de la fecha acordada para que el equipo de operaciones entregue el baño."
            },
            {
                "nombre": "🚪 Baño Entregado / Ganados",
                "descripcion": "El baño se entregó físicamente. El asesor debe dar clic en el botón 'Baño entregado'.",
                "detalles": "Al dar clic, se activa la encuesta post-servicio con emojis (☹️, 😐, 😄) y se prepara al cliente para recibir un cupón de reactivación del 10% cuando finalice la renta."
            },
            {
                "nombre": "👤 Apoyo Humano",
                "descripcion": "El lead requiere atención humana directa porque el bot no pudo clasificar su solicitud o el cliente solicitó hablar con un asesor.",
                "detalles": "Se crea una tarea urgente para Daniel Herrera y se notifica internamente."
            },
            {
                "nombre": "⏸️ En Pausa / Pausado",
                "descripcion": "Prospectos viables pero que requieren el servicio hasta dentro de 1 mes o más."
            },
            {
                "nombre": "🔄 Ganado cliente reactiva",
                "descripcion": "El cliente ganado vuelve a escribir meses después, rompiendo la pausa de espera.",
                "detalles": "El sistema detecta el mensaje y mueve el lead automáticamente a esta etapa (incluso si no tiene baño activo) para ofrecerle el menú autogestionable (solicitar retiros, quejas, rentar otro baño, consultar cobros, etc.)."
            },
            {
                "nombre": "🚚 Solicitud retiro",
                "descripcion": "El cliente ha solicitado formalmente el retiro de la unidad de baño.",
                "detalles": "Se le dan instrucciones de mandar correo a operacionesgdl@saniglobal.com.mx y se le envía la encuesta de emojis."
            },
            {
                "nombre": "😤 Quejas sin resolver",
                "descripcion": "Inconformidades del cliente que requieren atención humana.",
                "detalles": "En Baños, las quejas se transfieren a este estatus especializado para su resolución inmediata por parte del asesor, a diferencia de los otros embudos que lo manejan de forma local."
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
        "descripcion": "Limpieza de fosas sépticas, lodos estables, pozos de absorción y residuos líquidos industriales (13 etapas).",
        "etapas": [
            {
                "nombre": "📥 Contacto inicial",
                "descripcion": "El lead entra al seleccionar 'Servicios especiales' -> 'Fosas'. El bot pregunta por tipo de residuo, estado del material, almacenamiento y volumen.",
                "detalles": "Se envía la presentación de Saniglobal en PDF."
            },
            {
                "nombre": "🏠 CASA HABITACIÓN (Filtro Crítico)",
                "descripcion": "El bot pregunta obligatoriamente: ¿Es para una casa habitacional o residencial?",
                "detalles": "Si la respuesta es 'Sí', el bot le coloca la etiqueta 'CASA HABITACIÓN', envía el mensaje de rechazo cortés de que Saniglobal solo atiende sector comercial/industrial, y lo mueve automáticamente a Cerrado."
            },
            {
                "nombre": "ℹ️ Solicitud de información",
                "descripcion": "Validación técnica de los datos del residuo e información fiscal de la empresa antes de cotizar."
            },
            {
                "nombre": "🔎 Visita de Diagnóstico",
                "descripcion": "Paso para proyectos complejos donde Livier programa una visita técnica en sitio antes de cotizar."
            },
            {
                "nombre": "💰 Cotización",
                "descripcion": "La cotización en este embudo siempre se realiza de manera manual por Livier.",
                "detalles": "Es obligatorio presionar el botón 'Cotización realizada' para que el bot de seguimiento de 21h se configure correctamente."
            },
            {
                "nombre": "📞 Seguimiento",
                "descripcion": "A las 21 horas se envía mensaje de seguimiento automático. Si la objeción es precio, el bot ofrece un 5% de descuento máximo y etiqueta como 'Perdido por precio'."
            },
            {
                "nombre": "⏸️ En pausa",
                "descripcion": "Clientes comerciales que sí quieren el servicio pero lo necesitan dentro de más de 1 mes."
            },
            {
                "nombre": "🔄 CLIENTE ACTUAL (Reactivación y Quejas)",
                "descripcion": "Si un cliente en 'Ganados' vuelve a escribir, el bot de reactivación lo mueve a esta etapa y le muestra el menú interactivo (Solicitar servicio, reportes y quejas, dudas).",
                "detalles": "Regla Crítica para Quejas: En Fosas, las quejas NO se mandan a otro embudo. El asesor debe mantener el lead en esta etapa de CLIENTE ACTUAL, colocarle la etiqueta 'Queja' y darle resolución directamente aquí."
            },
            {
                "nombre": "📍 CLIENTES SLP",
                "descripcion": "Etapa de control para prospectos o clientes que corresponden a la zona de San Luis Potosí."
            },
            {
                "nombre": "👤 Apoyo humano fosas",
                "descripcion": "Cuando el cliente requiere atención directa de Livier o el bot no puede clasificar su solicitud."
            },
            {
                "nombre": "🏆 GANADOS",
                "descripcion": "Venta ganada, servicio ejecutado y facturado con éxito."
            },
            {
                "nombre": "❌ PERDIDOS",
                "descripcion": "Servicios eventuales concluidos, o clientes que contrataron con la competencia."
            },
            {
                "nombre": "🚫 CERRADOS NO POTENCIAL",
                "descripcion": "Prospectos no viables (fuera de zona, proveedores, spam, empleos, o casas habitación filtradas)."
            }
        ]
    },
    "trampas": {
        "responsable": "Asesor de Trampas de Grasa",
        "descripcion": "Limpieza y mantenimiento de trampas de grasa para cocinas comerciales, restaurantes e industrias (8 etapas).",
        "etapas": [
            {
                "nombre": "📥 Contacto inicial",
                "descripcion": "El bot realiza preguntas de calificación: número de trampas (1, 2, o 3+), capacidad (200L estándar, 250-500L, 500L+), material de la trampa, tipo de acceso, distancia de manguera necesaria y si cuenta con rampas.",
                "detalles": "Además, se le solicita fotos/videos de la trampa."
            },
            {
                "nombre": "👤 Apoyo humano",
                "descripcion": "Cuando el lead requiere asistencia directa del asesor o el bot se detiene por datos no clasificados."
            },
            {
                "nombre": "💰 COTIZACIÓN (Automática vs. Manual)",
                "descripcion": "Si es 1 o 2 trampas estándar de 200 LTS y se completaron los datos, se calcula y envía la propuesta automáticamente por un microservicio externo.",
                "detalles": "Si no cumple estas condiciones (ej. más capacidad o trampas), el asesor cotiza manualmente y presiona el botón 'Cotización de trampas de grasa manual' para continuar el flujo."
            },
            {
                "nombre": "📞 En seguimiento",
                "descripcion": "Seguimiento automático a las 21 horas. Si hay objeción de precio, ofrece cupón del 5% y asigna el tag 'Perdido por precio'.",
                "detalles": "Regla Crítica para Quejas: Las quejas de trampas de grasa NO se mandan a otro embudo. El asesor de trampas debe colocar manualmente la etiqueta 'Queja' y darle resolución directamente dentro de la etapa en que se encuentre el lead en este embudo."
            },
            {
                "nombre": "⏸️ En pausa",
                "descripcion": "Servicios viables que se programarán a más de 1 mes en el futuro."
            },
            {
                "nombre": "🔴 Perdido reactivable",
                "descripcion": "Prospectos ideales que no cerraron por precio o agenda. Se guardan para futuras campañas y promociones."
            },
            {
                "nombre": "❌ Perdidos",
                "descripcion": "Servicios eventuales que ya terminaron o que contrataron con competidores."
            },
            {
                "nombre": "🚫 Cerrado",
                "descripcion": "Solicitudes no viables (fuera de zona, proveedores, spam, empleos)."
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
    },
    {
        "question": "¿Bajo qué condiciones y cómo funciona la etapa de 'Seguimiento Automático' en el embudo de Renta de Baños?",
        "options": [
            "Llega cuando el cliente solicita un descuento adicional del 10% y el sistema lo procesa en segundos.",
            "Se activa a las 2 horas de inactividad del lead cuando este se encuentra en la etapa inicial de solicitud.",
            "Ocurre cuando, tras 21h de enviada la cotización el cliente no responde, el bot envía un recordatorio automático. Si pasan otras 24h sin respuesta, el sistema lo mueve automáticamente a esta etapa y le asigna el tag 'Sin respuesta'.",
            "Es una etapa manual donde Daniel Herrera mete los datos de entrega."
        ],
        "correct": 2,
        "explanation": "El Seguimiento Automático ocurre tras 21h de inactividad (primer mensaje del bot) más 24h adicionales sin respuesta. Mueve el lead a la etapa 'Seguimiento automático' y asigna el tag 'Sin respuesta'."
    },
    {
        "question": "¿Cuál es la diferencia entre las etapas 'Campañas Frío' y 'Campañas Caliente' en el embudo de Baños?",
        "options": [
            "Campañas Frío es para la temporada invernal y Campañas Caliente es para la temporada de calor.",
            "Campañas Frío es para leads masivos de recontacto que NO responden; Campañas Caliente es para aquellos que SÍ responden y muestran interés para su atención prioritaria.",
            "Campañas Frío es para clientes residenciales y Campañas Caliente es para el sector comercial.",
            "Campañas Frío es para lodos líquidos y Campañas Caliente es para residuos sólidos."
        ],
        "correct": 1,
        "explanation": "Campañas Frío agrupa a los prospectos inactivos recontactados que no contestaron la campaña; Campañas Caliente es para los que sí respondieron con interés en contratar."
    },
    {
        "question": "¿Cómo se deben gestionar las quejas y reportes en los embudos de Fosas Sépticas y Trampas de Grasa?",
        "options": [
            "Se deben mover de inmediato al embudo especializado de Quejas (ID 12717196).",
            "No se atienden porque Saniglobal no tiene departamento de soporte.",
            "Se reasignan automáticamente al departamento de marketing (Michelle).",
            "NO se envían a otro embudo. El asesor a cargo debe mantener el lead en su etapa actual (o Cliente Actual), asignarle manualmente la etiqueta 'Queja' y darle resolución allí mismo."
        ],
        "correct": 3,
        "explanation": "A diferencia de Baños (que usa un embudo de quejas dedicado), en Fosas y Trampas las quejas se resuelven de forma interna y directa en la misma etapa actual, etiquetando el lead con el tag 'Queja'."
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
