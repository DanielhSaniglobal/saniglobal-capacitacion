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

ETAPAS_BANOS = [
    {
        "num": 1,
        "nombre": "Lead Entrante",
        "razon": "Primer contacto o mensaje que entra a la plataforma de Kommo. Es la etapa inicial por defecto del CRM.",
        "automatizacion": "Se dispara de inmediato el Bot GPT Completo (recepcionista inteligente) para calificar al cliente y redireccionarlo al embudo correcto.",
        "deber_vendedor": "No intervenir de inmediato para permitir que el bot recepcionista realice las preguntas de calificación y canalice el lead de forma automatizada."
    },
    {
        "num": 2,
        "nombre": "Cerrado",
        "razon": "Estatus final y de archivo para solicitudes descartadas, inviables (fuera de zona, proveedores, spam, empleos).",
        "automatizacion": "El bot archiva y cierra de forma automatizada las solicitudes que no aplican.",
        "deber_vendedor": "Monitorear ocasionalmente para verificar que no haya falsos descartes."
    },
    {
        "num": 3,
        "nombre": "apoyo humano",
        "razon": "Estatus para leads que requieren asistencia directa de un asesor o donde el bot se detiene por respuestas no clasificadas.",
        "automatizacion": "Detiene el bot y genera de inmediato una tarea urgente asignada a Daniel Herrera.",
        "deber_vendedor": "Retomar la conversación de forma manual e inmediata para resolver y dar atención."
    },
    {
        "num": 4,
        "nombre": "Solicitud cotización",
        "razon": "Punto de entrada inicial cuando el prospecto ingresa manifestando interés de rentar sanitarios portátiles.",
        "automatizacion": "El bot inicia la recopilación de datos (uso de obra/evento, cantidad, tipo, dirección).",
        "deber_vendedor": "Monitorear el chat. Si pide 3 o más baños, el bot se pausa y debes cotizar de forma manual."
    },
    {
        "num": 5,
        "nombre": "Cotizado",
        "razon": "La cotización formal ha sido elaborada y enviada a revisión del cliente.",
        "automatizacion": "Al enviar cotización manual, presionar el botón activa el bot de seguimiento de 21h. Si no responde en 2h, el bot ofrece 5% de descuento.",
        "deber_vendedor": "Enviar la propuesta en PDF y dar clic obligatoriamente al botón manual 'Cotización realizada'."
    },
    {
        "num": 6,
        "nombre": "Embudo caliente",
        "razon": "El prospecto se encuentra chateando activamente con el asesor en tiempo real.",
        "automatizacion": "Se desactivan las respuestas automáticas para evitar entorpecer la conversación humana en vivo.",
        "deber_vendedor": "Atender con prioridad para resolver dudas y apresurar el cierre de la venta."
    },
    {
        "num": 7,
        "nombre": "Seguimiento automatico",
        "razon": "Leads que quedaron inactivos tras el envío de la propuesta.",
        "automatizacion": "Envía recordatorio a las 21 horas. Si pasan otras 24 horas sin respuesta, el CRM los traslada a esta etapa y añade el tag 'Sin respuesta'.",
        "deber_vendedor": "Monitorear y realizar llamadas telefónicas para recuperar la venta."
    },
    {
        "num": 8,
        "nombre": "Programado",
        "razon": "La renta ha sido acordada, el pago inicial/garantía verificado y está en agenda para entrega física.",
        "automatizacion": "Pausa alertas en espera de que se concrete la entrega física del sanitario.",
        "deber_vendedor": "Confirmar la fecha con operaciones y asegurar la correcta documentación del pago."
    },
    {
        "num": 9,
        "nombre": "Perdido reactivable",
        "razon": "Prospectos ideales que no cerraron por razones de precio o agenda, candidatos para futuras promociones.",
        "automatizacion": "Almacenamiento clasificado bajo etiquetas de archivado comercial.",
        "deber_vendedor": "Registrar de forma obligatoria la objeción del cliente en la tarjeta del lead."
    },
    {
        "num": 10,
        "nombre": "En pausa",
        "razon": "Prospectos viables que requieren el servicio dentro de 1 mes o más.",
        "automatizacion": "Detiene seguimientos automatizados para no saturar al cliente.",
        "deber_vendedor": "Programar tarea de seguimiento en calendario para la fecha de interés."
    },
    {
        "num": 11,
        "nombre": "Reubicar baños",
        "razon": "Trámite de logística solicitado por el cliente para mover un sanitario activo de lugar dentro de la obra o evento.",
        "automatizacion": "Pausa las alertas comerciales ordinarias para centrarse en la logística de reubicación.",
        "deber_vendedor": "Coordinar la nueva dirección y costo de maniobra con operaciones y confirmar la reubicación física en sitio."
    },
    {
        "num": 12,
        "nombre": "Quejas sin resolver",
        "razon": "Reporte de inconvenientes técnicos, mala limpieza o daños en los sanitarios rentados.",
        "automatizacion": "La conversación se traslada de inmediato al Embudo de Quejas Sanitarios en la etapa 'INICIO QUEJA'.",
        "deber_vendedor": "Dar seguimiento urgente y reportar a soporte técnico para resolución inmediata."
    },
    {
        "num": 13,
        "nombre": "Solicitud retiro",
        "razon": "El cliente ha solicitado formalmente la recolección física del baño en el sitio.",
        "automatizacion": "El bot da instrucciones de enviar correo a operaciones y envía la encuesta de emojis.",
        "deber_vendedor": "Validar correo de retiro y reportar a logística para recolección física."
    },
    {
        "num": 14,
        "nombre": "Campañas frío",
        "razon": "Leads inactivos provenientes de recontactos masivos que no mostraron respuesta o interés.",
        "automatizacion": "Se agrupan en esta etapa para futuras campañas de promociones masivas.",
        "deber_vendedor": "Mantenerlos en esta etapa para futuras campañas de promociones masivas."
    },
    {
        "num": 15,
        "nombre": "Campañas caliente",
        "razon": "Leads que sí respondieron positivamente y muestran interés en rentar nuevamente tras un recontacto.",
        "automatizacion": "El sistema los mueve aquí automáticamente si el cliente contesta el mensaje masivo.",
        "deber_vendedor": "Dar atención prioritaria inmediata y enviar cotización para cerrar la venta."
    },
    {
        "num": 16,
        "nombre": "Ganado cliente reactiva",
        "razon": "Residencia permanente para clientes ganados previamente que se reactivaron por dudas, información o retiros.",
        "automatizacion": "Una vez resuelta la consulta del cliente reactivado, al cerrar el chat el sistema lo archiva en esta etapa permanente.",
        "deber_vendedor": "Mover el lead a esta etapa al finalizar/resolver su conversación reactivada."
    },
    {
        "num": 17,
        "nombre": "Ganados",
        "razon": "El sanitario ha sido entregado en sitio por primera vez.",
        "automatizacion": "Se debe usar preferentemente el botón 'Baño entregado y ganado' de la tarjeta porque activa más automatizaciones que el botón normal.",
        "deber_vendedor": "Mover el lead a Ganados y dar clic obligatoriamente al botón manual 'Baño entregado y ganado'."
    },
    {
        "num": 18,
        "nombre": "Perdidos",
        "razon": "Prospectos comerciales que decidieron contratar con la competencia o no procedieron.",
        "automatizacion": "Finaliza el seguimiento del bot.",
        "deber_vendedor": "Archivar y registrar causa de pérdida."
    }
]

ETAPAS_FOSAS = [
    {
        "num": 1,
        "nombre": "Contacto Inicial",
        "razon": "Primer contacto de prospectos que seleccionaron 'Servicios especiales' -> 'Fosas' en el Bot GPT Completo.",
        "automatizacion": "El bot pregunta tipo de residuo, estado del material, almacenamiento y volumen. Envía el PDF de presentación de Saniglobal y lo asigna a Livier Mora.",
        "deber_vendedor": "Monitorear que el lead califique correctamente."
    },
    {
        "num": 2,
        "nombre": "CLIENTE ACTUAL",
        "razon": "Reactivación y soporte post-venta para clientes ganados que vuelven a escribir.",
        "automatizacion": "El bot despliega menú interactivo. REGLA CRÍTICA DE QUEJAS: En Fosas las quejas NO se mandan a otro embudo. Livier debe resolver de forma local en esta etapa agregando manualmente la etiqueta 'Queja'.",
        "deber_vendedor": "Atender requerimientos de servicios adicionales o gestionar quejas con el tag manual 'Queja'."
    },
    {
        "num": 3,
        "nombre": "apoyo humano fosas",
        "razon": "Prospectos que requieren atención directa de la asesora o el bot se detiene por respuestas no clasificadas.",
        "automatizacion": "Detiene el bot y genera tarea urgente a Livier Mora.",
        "deber_vendedor": "Retomar la conversación de forma manual e inmediata."
    },
    {
        "num": 4,
        "nombre": "CERRADOS NO POTENCIAL",
        "razon": "Leads residenciales descartados por el bot, spam o proveedores.",
        "automatizacion": "El bot los mueve aquí automáticamente tras descartar.",
        "deber_vendedor": "Validar ocasionalmente que no haya leads comerciales válidos aquí."
    },
    {
        "num": 5,
        "nombre": "CASA HABITACIÓN",
        "razon": "Filtro crítico de exclusión. Saniglobal no atiende domicilios residenciales/particulares.",
        "automatizacion": "Si responde que es casa habitación, el bot pone el tag 'CASA HABITACIÓN', envía mensaje de rechazo cortés y lo mueve a Cerrado.",
        "deber_vendedor": "Ninguno comercial (proceso 100% automatizado)."
    },
    {
        "num": 6,
        "nombre": "CLIENTES SLP",
        "razon": "Control geográfico interno para leads que corresponden a la zona de San Luis Potosí.",
        "automatizacion": "Separa el flujo comercial para operaciones de SLP.",
        "deber_vendedor": "Coordinar con el equipo regional de operaciones en SLP para logística y precios aplicables."
    },
    {
        "num": 7,
        "nombre": "Solicitud de información",
        "razon": "Validación técnica de los datos del residuo e información fiscal antes de formular propuesta.",
        "automatizacion": "El bot solicita datos técnicos complementarios.",
        "deber_vendedor": "Validar los requerimientos de sitio, accesos de camión y manguera."
    },
    {
        "num": 8,
        "nombre": "Visita diagnóstico",
        "razon": "Proyectos complejos donde es necesario verificar físicamente el sitio antes de cotizar.",
        "automatizacion": "Pausa las automatizaciones mientras se realiza la visita.",
        "deber_vendedor": "Programar fecha y hora para la visita del personal técnico."
    },
    {
        "num": 9,
        "nombre": "Cotización",
        "razon": "Propuesta formulada y enviada a revisión del cliente.",
        "automatizacion": "Cotización siempre manual. Es obligatorio presionar el botón 'Cotización realizada' para configurar el bot de seguimiento de 21h.",
        "deber_vendedor": "Enviar cotización en PDF y dar clic obligatoriamente en el botón manual 'Cotización realizada'."
    },
    {
        "num": 10,
        "nombre": "Seguimiento",
        "razon": "Seguimiento a propuestas no contestadas.",
        "automatizacion": "A las 21 horas envía seguimiento. Si la objeción es precio, el bot ofrece un cupón del 5% y etiqueta como 'Perdido por precio'.",
        "deber_vendedor": "Realizar llamada telefónica para empujar el cierre del servicio."
    },
    {
        "num": 11,
        "nombre": "En pausa",
        "razon": "Clientes que sí quieren el servicio pero lo requieren dentro de 1 mes o más.",
        "automatizacion": "Detiene recordatorios de chat diarios.",
        "deber_vendedor": "Programar tarea de seguimiento en calendario para la fecha de interés."
    },
    {
        "num": 12,
        "nombre": "GANADOS",
        "razon": "Servicio comercial ejecutado, facturado y cobrado con éxito.",
        "automatizacion": "Cierra ciclo de ventas inicial y programa ventana de reactivación.",
        "deber_vendedor": "Mover el lead a GANADOS and asegurar que se documente el pago."
    },
    {
        "num": 13,
        "nombre": "PERDIDOS",
        "razon": "Prospectos comerciales que decidieron contratar con la competencia o no procedieron.",
        "automatizacion": "Detiene flujos de seguimiento automático.",
        "deber_vendedor": "Registrar la causa de pérdida (objeción de precio, cobertura, etc.)."
    }
]

ETAPAS_TRAMPAS = [
    {
        "num": 1,
        "nombre": "Contacto Inicial",
        "razon": "Primer contacto para desazolve y limpieza de trampas de grasa en restaurantes y comedores.",
        "automatizacion": "El bot pregunta número de trampas, capacidad (lts), material, tipo de acceso, distancia de manguera y rampas. Solicita fotos/videos.",
        "deber_vendedor": "Monitorear que el cliente proporcione los datos técnicos y multimedia solicitados."
    },
    {
        "num": 2,
        "nombre": "CLIENTE ACTUAL",
        "razon": "Reactivación y soporte post-venta para clientes ganados que vuelven a escribir.",
        "automatizacion": "El bot despliega menú interactivo. REGLA CRÍTICA DE QUEJAS: Las quejas de trampas NO se mandan a otro embudo. El asesor debe colocar manualmente la etiqueta 'Queja' y resolver directamente en la etapa actual.",
        "deber_vendedor": "Atender requerimientos de nuevos servicios o resolver inconformidades locales con la etiqueta manual 'Queja'."
    },
    {
        "num": 3,
        "nombre": "APOYO HUMANO",
        "razon": "El cliente requiere asistencia directa del asesor o ingresó respuestas que el bot no pudo clasificar.",
        "automatizacion": "Detiene el bot y crea tarea comercial urgente al asesor de trampas.",
        "deber_vendedor": "Tomar la conversación en el chat de forma inmediata para resolver y cotizar."
    },
    {
        "num": 4,
        "nombre": "CERRADOS NO POTENCIAL",
        "razon": "Leads descartados por el bot, spam o proveedores.",
        "automatizacion": "El bot los mueve aquí de forma automática.",
        "deber_vendedor": "Monitorear descartes ocasionalmente."
    },
    {
        "num": 5,
        "nombre": "SOLICITUD DE INFORMACIÓN",
        "razon": "Validación y recopilación de datos técnicos adicionales, accesos y datos fiscales antes de cotizar.",
        "automatizacion": "El bot solicita información complementaria.",
        "deber_vendedor": "Validar accesos de camión y requerimientos de manguera en la tarjeta del lead."
    },
    {
        "num": 6,
        "nombre": "VISITA DIAGNÓSTICO",
        "razon": "Proyectos complejos que requieren inspección física antes de dar precio.",
        "automatizacion": "Pausa las automatizaciones comerciales en espera del diagnóstico técnico.",
        "deber_vendedor": "Programar la visita física del personal técnico de diagnóstico."
    },
    {
        "num": 7,
        "nombre": "COTIZACIÓN",
        "razon": "Envío de propuesta de limpieza al cliente.",
        "automatizacion": "Si es 1 o 2 trampas estándar de 200 LTS, el bot cotiza automáticamente vía webhook. Si supera el estándar (más trampas o más litros), el asesor debe cotizar manualmente por fuera y presionar el botón 'Cotización de trampas de grasa manual'.",
        "deber_vendedor": "Si la cotización es manual, enviarla en PDF y hacer clic obligatoriamente en el botón 'Cotización de trampas de grasa manual'."
    },
    {
        "num": 8,
        "nombre": "SEGUIMIENTO",
        "razon": "Seguimiento automático a las cotizaciones enviadas.",
        "automatizacion": "A las 21 horas envía mensaje. Si la objeción es precio, el bot ofrece descuento de 5% y etiqueta como 'Perdido por precio'. REGLA CRÍTICA DE QUEJAS: Las quejas de trampas NO se mandan a otro embudo. El asesor debe colocar manualmente la etiqueta 'Queja' y resolver directamente en la etapa actual.",
        "deber_vendedor": "Realizar llamada para negociar y cerrar el servicio."
    },
    {
        "num": 9,
        "nombre": "EN PAUSA",
        "razon": "Servicios viables proyectados a más de 1 mes de distancia.",
        "automatizacion": "Detiene flujos de seguimiento diario.",
        "deber_vendedor": "Agendar tarea de seguimiento en calendario para la fecha futura."
    },
    {
        "num": 10,
        "nombre": "GANADOS",
        "razon": "Limpieza ejecutada con éxito, cobrada y facturada.",
        "automatizacion": "Cierra ciclo de ventas inicial y registra el éxito.",
        "deber_vendedor": "Mover el lead a GANADOS y registrar los datos de pago."
    },
    {
        "num": 11,
        "nombre": "PERDIDOS",
        "razon": "El cliente decidió contratar definitivamente con la competencia.",
        "automatizacion": "Detiene todos los flujos de seguimiento automáticos.",
        "deber_vendedor": "Archivar y registrar causa de pérdida."
    }
]

EMBUDOS_INFO = {
    "baños": {
        "responsable": "Daniel Herrera",
        "descripcion": "Embudo enfocado en la renta de sanitarios portátiles para obras y eventos (18 etapas en total).",
        "etapas": [
            {
                "nombre": f"{e['num']}. {e['nombre']}",
                "descripcion": e['razon'],
                "detalles": f"🤖 Automatización: {e['automatizacion']}\n👤 Deber del vendedor: {e['deber_vendedor']}"
            } for e in ETAPAS_BANOS
        ]
    },
    "fosas": {
        "responsable": "Livier Mora",
        "descripcion": "Limpieza de fosas sépticas, lodos estables, pozos de absorción y residuos líquidos industriales (13 etapas).",
        "etapas": [
            {
                "nombre": f"{e['num']}. {e['nombre']}",
                "descripcion": e['razon'],
                "detalles": f"🤖 Automatización: {e['automatizacion']}\n👤 Deber del vendedor: {e['deber_vendedor']}"
            } for e in ETAPAS_FOSAS
        ]
    },
    "trampas": {
        "responsable": "Asesor de Trampas de Grasa",
        "descripcion": "Limpieza y mantenimiento de trampas de grasa para cocinas comerciales, restaurantes e industrias (11 etapas).",
        "etapas": [
            {
                "nombre": f"{e['num']}. {e['nombre']}",
                "descripcion": e['razon'],
                "detalles": f"🤖 Automatización: {e['automatizacion']}\n👤 Deber del vendedor: {e['deber_vendedor']}"
            } for e in ETAPAS_TRAMPAS
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
        "question": "Cuando un cliente que ya estaba en estatus 'Ganados' vuelve a iniciar una conversación (pide info, seguimiento o retiros), ¿qué se debe hacer al finalizar esa conversación?",
        "options": [
            "Cerrar la tarjeta por completo y archivarla como Perdidos.",
            "Dejarlo en la etapa de Ganados original sin realizar ningún cambio.",
            "Mandar al lead a la etapa de 'Ganados Cliente reactiva', donde vivirá permanentemente de ahí en adelante.",
            "Crear un lead duplicado en el embudo de solicitud de cotización."
        ],
        "correct": 2,
        "explanation": "La nueva regla de negocio establece que al finalizar cualquier conversación reactivada con un cliente que ya era ganado, se le debe mover a la etapa de 'Ganados Cliente reactiva', donde deberá residir de manera permanente."
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
    },
    {
        "question": "¿Cuál es la 'Regla de Oro' obligatoria cuando un asesor reasigna un lead a otro compañero porque le llegó a él por error?",
        "options": [
            "Simplemente cambiar el responsable y guardar la tarjeta sin hacer nada más.",
            "Eliminar la conversación y el historial del chat para que el nuevo asesor empiece desde cero.",
            "Agregar obligatoriamente una nota en la tarjeta detallando cualquier información extra, comentario o necesidad que el cliente ya le haya comentado.",
            "Mandar un WhatsApp privado al compañero y no modificar nada en Kommo CRM."
        ],
        "correct": 2,
        "explanation": "La Regla de Oro de Asignación establece que si reasignas una oportunidad por error a otro compañero, debes dejar obligatoriamente una nota interna con toda la información extra o comentarios que te haya dado el cliente, para evitar la pérdida de información y facilitar la transición."
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
