# -*- coding: utf-8 -*-
"""
Banco de preguntas para la sección de Evaluación de Conocimientos.
Cada área tiene 20 preguntas para que se seleccionen 10 al azar por sesión.
Estructura: pregunta, opciones (3), índice de la correcta, explicación.
"""

QUIZ_BANOS = [
    {
        "pregunta": "¿Cuál es el primer embudo por el que pasan TODOS los prospectos de Saniglobal al escribir por WhatsApp?",
        "opciones": [
            "Embudo de Ventas (Baños)",
            "Embudo GPT Completo",
            "Embudo de Entregas y Retiros"
        ],
        "correcta": 1,
        "explicacion": "Todos los leads entran primero al Embudo GPT Completo, donde el bot de bienvenida los clasifica y luego los turna al embudo especializado correspondiente."
    },
    {
        "pregunta": "¿Qué debes hacer obligatoriamente cuando reasignas un lead a otro compañero porque te llegó por error?",
        "opciones": [
            "Solo cambiar el campo 'Responsable' en la tarjeta",
            "Cambiar el responsable Y dejar una nota obligatoria con los datos que el cliente ya compartió",
            "Enviar un correo al administrador solicitando la reasignación"
        ],
        "correcta": 1,
        "explicacion": "La Regla de Oro de Asignación indica que al reasignar debes dejar obligatoriamente una nota en la tarjeta con cualquier dato extra, comentario o necesidad que el cliente ya haya compartido para no perder información."
    },
    {
        "pregunta": "¿Cuántas conversaciones abiertas máximo debes tener en tu sección de chats?",
        "opciones": [
            "5 conversaciones",
            "10 conversaciones",
            "20 conversaciones"
        ],
        "correcta": 1,
        "explicacion": "No se debe dejar la sección de chats con más de 10 conversaciones abiertas al mismo tiempo para mantener el CRM ordenado y dar atención oportuna."
    },
    {
        "pregunta": "¿Cuánto tiempo tiene la ventana de respuesta de WhatsApp antes de que se cierre?",
        "opciones": [
            "12 horas desde el último mensaje del cliente",
            "24 horas desde el último mensaje del cliente",
            "48 horas desde el último mensaje del cliente"
        ],
        "correcta": 1,
        "explicacion": "Meta (WhatsApp, Facebook, Instagram) solo permite responder libremente dentro de las 24 horas posteriores al último mensaje del cliente. Si se cierra, se debe enviar una Plantilla HSM aprobada (tiene costo)."
    },
    {
        "pregunta": "¿A qué hora opera el bot de seguimiento automático después de enviar una cotización en Baños?",
        "opciones": [
            "A las 12 horas",
            "A las 21 horas",
            "A las 48 horas"
        ],
        "correcta": 1,
        "explicacion": "Los bots de seguimiento operan a las 21 horas para enviar el recordatorio antes de que expire la ventana de 24 horas de WhatsApp."
    },
    {
        "pregunta": "Si un cliente de Baños solicita 3 o más sanitarios, ¿qué sucede?",
        "opciones": [
            "El bot cotiza automáticamente aplicando un descuento por volumen",
            "El bot se pausa automáticamente y turna al asesor Daniel Herrera para cotización manual",
            "El bot rechaza la solicitud y pide que llame por teléfono"
        ],
        "correcta": 1,
        "explicacion": "Si el prospecto solicita 3 o más unidades, el bot se pausa automáticamente y lo turna a Daniel Herrera para atención y cotización manual personalizada."
    },
    {
        "pregunta": "¿Qué descuento automático ofrece el bot si el cliente no responde a la cotización de Baños en 2 horas?",
        "opciones": [
            "3% de descuento",
            "5% de descuento",
            "10% de descuento"
        ],
        "correcta": 1,
        "explicacion": "Dos horas después de enviar una cotización, si el cliente no responde, el bot envía automáticamente un incentivo con un 5% de descuento y agrega la etiqueta '-5% descuento'."
    },
    {
        "pregunta": "Cuando un cliente ganado de Baños vuelve a escribir y su conversación se resuelve, ¿a qué etapa debe moverse?",
        "opciones": [
            "Ganados (etapa original)",
            "Ganados Cliente reactiva",
            "Seguimiento automático"
        ],
        "correcta": 1,
        "explicacion": "Una vez finalizada la conversación de un cliente ganado que se reactivó, debe moverse a 'Ganados Cliente reactiva', donde deberá vivir permanentemente de ahí en adelante."
    },
    {
        "pregunta": "¿Qué botón debes presionar obligatoriamente al enviar una cotización formal en PDF al cliente de Baños?",
        "opciones": [
            "Botón 'Enviar cotización'",
            "Botón 'Cotización realizada'",
            "Botón 'Generar PDF'"
        ],
        "correcta": 1,
        "explicacion": "El botón 'Cotización realizada' es obligatorio porque activa la automatización: envía un mensaje predefinido al cliente y programa el bot de seguimiento de 21 horas."
    },
    {
        "pregunta": "¿Qué hace el botón 'Baño entregado y ganado'?",
        "opciones": [
            "Genera la factura automáticamente en el sistema contable",
            "Envía automáticamente al cliente información post-venta (reglas de uso, mantenimiento y próximos pasos)",
            "Marca el lead como inactivo y cierra todas las tareas"
        ],
        "correcta": 1,
        "explicacion": "Al hacer clic en 'Baño entregado y ganado', el bot envía automáticamente al cliente la información post-venta sobre su renta: reglas de uso, mantenimiento y qué procede a partir de ese momento."
    },
    {
        "pregunta": "¿Cómo se gestionan las quejas de clientes en el embudo de Baños?",
        "opciones": [
            "Se resuelven directamente en la misma etapa con la etiqueta 'Queja'",
            "Se trasladan al Embudo de Quejas Sanitarios (Pipeline 12717196) en la etapa INICIO QUEJA",
            "Se escalan por correo electrónico al gerente de operaciones"
        ],
        "correcta": 1,
        "explicacion": "En Baños, las inconformidades se transfieren de inmediato al Embudo de Quejas Sanitarios (Pipeline 12717196) en 'INICIO QUEJA' para su resolución por personal de soporte. Esto es diferente a Fosas y Trampas donde se resuelven localmente."
    },
    {
        "pregunta": "¿Cuál es el filtro que siempre debes tener activo en tu sección de chats?",
        "opciones": [
            "Filtro 'Todos los chats'",
            "Filtro 'Asignado a mí'",
            "Filtro 'Sin respuesta'"
        ],
        "correcta": 1,
        "explicacion": "Siempre debes tener activo el filtro 'Asignado a mí' para visualizar únicamente tus leads y evitar interferencias o dobles atenciones."
    },
    {
        "pregunta": "¿Qué diferencia hay entre 'Conversación cerrada' y 'Marque resuelto'?",
        "opciones": [
            "'Conversación cerrada' elimina tareas; 'Marque resuelto' las conserva",
            "'Conversación cerrada' conserva tareas internas; 'Marque resuelto' elimina todas las tareas pendientes",
            "Ambas opciones hacen exactamente lo mismo"
        ],
        "correcta": 1,
        "explicacion": "'Conversación cerrada' despeja tu buzón sin eliminar recordatorios/tareas internas. 'Marque resuelto' cierra la conversación Y elimina todas las tareas pendientes porque el lead ya concluyó su proceso."
    },
    {
        "pregunta": "Cuando un lead de Baños está listo para entrega, ¿a qué embudo y etapa debes moverlo?",
        "opciones": [
            "Embudo de Ventas → Etapa 'Ganados'",
            "Embudo de Entregas y Retiros → Etapa 'Solicitud de programación'",
            "Embudo GPT Completo → Etapa 'Entrega programada'"
        ],
        "correcta": 1,
        "explicacion": "El lead calificado y listo para entrega se mueve al embudo de Entregas y Retiros en la etapa 'Solicitud de programación', donde se genera automáticamente un correo plantilla a soporte y al responsable."
    },
    {
        "pregunta": "¿A quiénes debes reenviar el correo de programación de entrega de Baños?",
        "opciones": [
            "Solo a facturacion@saniglobal.com.mx y operaciones3@saniglobal.com.mx",
            "A un grupo de 8 direcciones incluyendo facturación, cobranza, operaciones, soporte y dirección",
            "Solo al administrador del CRM para que él lo distribuya"
        ],
        "correcta": 1,
        "explicacion": "El correo debe reenviarse a 8 destinatarios obligatorios: facturación, cobranza1, cobranza3, operaciones3, soporte, casetassanitarias, v.ruiz y d.herrera. Se recomienda crear un grupo de contactos llamado 'programación'."
    },
    {
        "pregunta": "En el embudo de Entregas y Retiros, ¿qué significa una tarjeta en color ROJO?",
        "opciones": [
            "El lead fue cancelado por el cliente",
            "Requiere acciones inmediatas del vendedor (corregir datos, documentos faltantes, etc.)",
            "La entrega ya fue completada exitosamente"
        ],
        "correcta": 1,
        "explicacion": "Una tarjeta en rojo en Entregas y Retiros significa que requiere acciones inmediatas del vendedor: corregir datos, completar documentos faltantes u otros pendientes. Una tarjeta en azul significa que está en manos de E&R y se encuentra programada o en ruta."
    },
    {
        "pregunta": "¿Cuánto tiempo después de no responder la cotización el sistema mueve al cliente a 'Seguimiento automático'?",
        "opciones": [
            "24 horas sin respuesta",
            "45 horas sin respuesta (21h del primer seguimiento + 24h adicionales)",
            "72 horas sin respuesta"
        ],
        "correcta": 1,
        "explicacion": "Si el cliente no responde en 21 horas se envía el primer seguimiento. Si pasan otras 24 horas (45 horas de silencio total), el CRM lo traslada a 'Seguimiento automático' con la etiqueta 'Sin respuesta'."
    },
    {
        "pregunta": "¿Cómo accedes a los Mensajes Rápidos (plantillas predefinidas) en el chat de Kommo?",
        "opciones": [
            "Haciendo clic en el ícono de clip (adjuntar) del chat",
            "Escribiendo '/' (diagonal) en el cuadro de texto del chat",
            "Desde el menú Ajustes → Plantillas → Usar plantilla"
        ],
        "correcta": 1,
        "explicacion": "Para acceder a las plantillas de mensajes rápidos, escribes '/' (diagonal) en el cuadro de texto del chat y luego escribes palabras clave del título para filtrarlas."
    },
    {
        "pregunta": "¿Qué cupón ofrece el bot cuando un cliente ganado de Baños elige 'Retirar' su sanitario y confirma el retiro?",
        "opciones": [
            "Cupón del 5% de descuento para futura reactivación",
            "Cupón del 10% de descuento para futura reactivación",
            "No se ofrece ningún cupón al retirar"
        ],
        "correcta": 1,
        "explicacion": "Cuando un cliente ganado confirma el retiro, se le dispara la encuesta de emojis y al finalizar se le regala un cupón del 10% de descuento para reactivación futura."
    },
    {
        "pregunta": "¿Cada cuánto tiempo debes revisar el CRM de Kommo como buena práctica?",
        "opciones": [
            "Cada 30 minutos",
            "Cada 5 minutos",
            "Cada hora"
        ],
        "correcta": 1,
        "explicacion": "La buena práctica establece que debes revisar Kommo CRM cada 5 minutos, manteniéndolo abierto y activo en tu navegador o app móvil para enterarte de inmediato de nuevos mensajes."
    },
]

QUIZ_FOSAS = [
    {
        "pregunta": "¿Quién es la asesora responsable del Embudo de Fosas GDL?",
        "opciones": [
            "Daniel Herrera (Usuario 12824423)",
            "Livier Mora (Usuario 13346199)",
            "Asesor de Trampas de Grasa"
        ],
        "correcta": 1,
        "explicacion": "Livier Mora (Usuario 13346199) es la asesora responsable del Embudo Fosas GDL, donde se gestionan los servicios de sondeos, desazolves y disposición de lodos."
    },
    {
        "pregunta": "¿Cuántas etapas tiene el Embudo de Fosas GDL?",
        "opciones": [
            "11 etapas",
            "13 etapas",
            "18 etapas"
        ],
        "correcta": 1,
        "explicacion": "El Embudo de Fosas GDL tiene 13 etapas: Contacto Inicial, CLIENTE ACTUAL, apoyo humano fosas, CERRADOS NO POTENCIAL, CASA HABITACIÓN, CLIENTES SLP, Solicitud de información, Visita diagnóstico, Cotización, Seguimiento, En pausa, GANADOS y PERDIDOS."
    },
    {
        "pregunta": "¿Cómo se gestionan las quejas de clientes en el embudo de Fosas?",
        "opciones": [
            "Se trasladan al Embudo de Quejas Sanitarios como en Baños",
            "Se resuelven de forma local en la etapa CLIENTE ACTUAL agregando la etiqueta manual 'Queja'",
            "Se escalan automáticamente al departamento de soporte técnico"
        ],
        "correcta": 1,
        "explicacion": "En Fosas las quejas NO se mandan a otro embudo. Livier debe resolver de forma local en la etapa CLIENTE ACTUAL agregando manualmente la etiqueta 'Queja'. Esto es diferente a Baños donde sí se trasladan."
    },
    {
        "pregunta": "¿Qué sucede si un prospecto de fosas indica que es para una CASA HABITACIÓN?",
        "opciones": [
            "El bot lo conecta con un asesor para evaluar si se puede atender",
            "El bot le coloca el tag 'CASA HABITACIÓN', envía mensaje de rechazo cortés y lo mueve a Cerrado",
            "El bot le ofrece un precio especial residencial"
        ],
        "correcta": 1,
        "explicacion": "Saniglobal no atiende domicilios residenciales. Si el prospecto indica que es casa habitación, el bot le pone el tag 'CASA HABITACIÓN', envía un mensaje de rechazo cortés y lo mueve a la etapa Cerrado automáticamente."
    },
    {
        "pregunta": "¿Cómo es la cotización en el embudo de Fosas?",
        "opciones": [
            "Es automática vía webhook como en Trampas de Grasa",
            "Siempre es manual. La asesora debe presionar el botón 'Cotización realizada' para activar el seguimiento",
            "El bot genera un enlace de cotización automático basado en el volumen"
        ],
        "correcta": 1,
        "explicacion": "En Fosas la cotización siempre es manual. Es obligatorio presionar el botón 'Cotización realizada' después de enviar la cotización en PDF para configurar el bot de seguimiento de 21 horas."
    },
    {
        "pregunta": "¿Qué cupón de descuento ofrece el bot de Fosas cuando la objeción del cliente es precio?",
        "opciones": [
            "10% de descuento",
            "5% de descuento",
            "No ofrece descuento en Fosas"
        ],
        "correcta": 1,
        "explicacion": "En el embudo de Fosas, si la objeción es precio, el bot ofrece un cupón del 5% y etiqueta como 'Perdido por precio'."
    },
    {
        "pregunta": "¿Para qué sirve la etapa 'CLIENTES SLP' en el embudo de Fosas?",
        "opciones": [
            "Para clientes que requieren servicio en San Luis Potosí, separando el flujo para operaciones regionales",
            "Para clientes con solicitudes de servicio a largo plazo (SLP = Servicio Largo Plazo)",
            "Para clientes que provienen de campañas de marketing en SLP"
        ],
        "correcta": 0,
        "explicacion": "CLIENTES SLP es un control geográfico interno para leads que corresponden a la zona de San Luis Potosí. Separa el flujo comercial para coordinar con el equipo regional de operaciones en SLP."
    },
    {
        "pregunta": "¿Qué datos técnicos solicita el bot de Fosas en el flujo de calificación?",
        "opciones": [
            "Número de fosas, capacidad en litros, material y acceso de manguera",
            "Tipo de residuo, estado del material, tipo de almacenamiento y volumen",
            "Dirección, tipo de propiedad, nombre del contacto y RFC"
        ],
        "correcta": 1,
        "explicacion": "El bot de fosas pregunta: tipo de residuo (fosas sépticas, lodo biológico, vinazas, etc.), estado del material (líquido, lodo/pasta, sólido/polvo), tipo de almacenamiento (fosa/cisterna, tambo/tolva, sobre terreno) y volumen estimado."
    },
    {
        "pregunta": "¿Cuándo un lead de Fosas pasa a la etapa 'Visita diagnóstico'?",
        "opciones": [
            "Cuando el cliente solicita más de 10,000 litros de servicio",
            "Cuando el proyecto es complejo y requiere verificación física del sitio antes de cotizar",
            "Cuando el bot no puede clasificar las respuestas del cliente"
        ],
        "correcta": 1,
        "explicacion": "La etapa 'Visita diagnóstico' es para proyectos complejos donde es necesario verificar físicamente el sitio antes de cotizar. Se pausa la automatización mientras se realiza la visita."
    },
    {
        "pregunta": "¿Qué sucede con un lead en la etapa 'apoyo humano fosas'?",
        "opciones": [
            "El bot continúa con preguntas adicionales de calificación técnica",
            "El bot se detiene y genera una tarea urgente a Livier Mora para atención manual inmediata",
            "El lead se marca como no potencial y se archiva"
        ],
        "correcta": 1,
        "explicacion": "En 'apoyo humano fosas', el bot se detiene completamente y genera una tarea urgente a Livier Mora. La asesora debe retomar la conversación de forma manual e inmediata."
    },
    {
        "pregunta": "¿Qué acción realiza el vendedor cuando un lead de Fosas pasa a la etapa 'En pausa'?",
        "opciones": [
            "Nada, el bot se encarga de reactivar al cliente automáticamente",
            "Programar una tarea de seguimiento en calendario para la fecha de interés del cliente",
            "Mover el lead a PERDIDOS después de 30 días"
        ],
        "correcta": 1,
        "explicacion": "Cuando un lead está 'En pausa' (quiere el servicio pero lo requiere dentro de 1 mes o más), se detienen los recordatorios diarios y el vendedor debe programar una tarea de seguimiento en calendario para la fecha de interés."
    },
    {
        "pregunta": "¿Qué embudo debe tener seleccionado Livier Mora en la barra lateral izquierda de Kommo?",
        "opciones": [
            "Embudo GPT Completo",
            "Embudo Fosas GDL",
            "Embudo de Ventas"
        ],
        "correcta": 1,
        "explicacion": "Livier Mora debe tener seleccionado el Embudo Fosas GDL en la sección de Leads del menú de la barra izquierda fija de Kommo."
    },
    {
        "pregunta": "¿Qué hace el bot cuando un lead de Fosas no responde a la cotización en 21 horas?",
        "opciones": [
            "Cierra la conversación automáticamente",
            "Envía un mensaje de seguimiento automático al cliente",
            "Reasigna el lead a otro asesor"
        ],
        "correcta": 1,
        "explicacion": "A las 21 horas sin respuesta, el bot envía un seguimiento automático. Si la objeción es precio, ofrece un cupón del 5% y etiqueta como 'Perdido por precio'."
    },
    {
        "pregunta": "¿Qué información debe validar la asesora de Fosas antes de la visita de diagnóstico?",
        "opciones": [
            "Solo la dirección y teléfono del contacto",
            "Los requerimientos de sitio, accesos de camión y manguera",
            "El historial crediticio de la empresa cliente"
        ],
        "correcta": 1,
        "explicacion": "La asesora debe validar los requerimientos de sitio, accesos de camión y necesidades de manguera en la tarjeta del lead antes de programar la visita técnica."
    },
    {
        "pregunta": "¿Cuál es el primer paso que realiza el bot cuando un prospecto selecciona 'Servicios especiales → Fosas'?",
        "opciones": [
            "Le solicita inmediatamente su RFC y datos fiscales",
            "Le pregunta tipo de residuo, estado del material, almacenamiento, volumen y envía el PDF de presentación",
            "Le conecta directamente con Livier Mora para atención personalizada"
        ],
        "correcta": 1,
        "explicacion": "El bot del Contacto Inicial pregunta tipo de residuo, estado del material, almacenamiento y volumen. Envía el PDF de presentación de Saniglobal y asigna al lead a Livier Mora."
    },
    {
        "pregunta": "Si un lead de Fosas fue ganado, ¿qué debe documentar el vendedor?",
        "opciones": [
            "Solo el nombre del cliente y la fecha de cierre",
            "Mover el lead a GANADOS y asegurar que se documenten los datos de pago",
            "Enviar un correo a facturación con los datos del servicio"
        ],
        "correcta": 1,
        "explicacion": "El vendedor debe mover el lead a GANADOS (servicio ejecutado, facturado y cobrado con éxito) y asegurar que se documente el pago en la tarjeta."
    },
    {
        "pregunta": "¿Qué sucede cuando un lead de Fosas es clasificado como CERRADOS NO POTENCIAL?",
        "opciones": [
            "Se elimina permanentemente del CRM",
            "El bot los mueve aquí automáticamente tras descartar (leads residenciales, spam o proveedores)",
            "Se reasigna a otro asesor para segunda opinión"
        ],
        "correcta": 1,
        "explicacion": "Los leads clasificados como CERRADOS NO POTENCIAL son movidos automáticamente por el bot. Incluyen leads residenciales descartados, spam o proveedores. El vendedor debe validar ocasionalmente que no haya leads comerciales válidos ahí."
    },
    {
        "pregunta": "¿Cuándo un lead de Fosas pasa a 'PERDIDOS'?",
        "opciones": [
            "Cuando el cliente no responde el primer mensaje del bot",
            "Cuando el prospecto decidió contratar definitivamente con la competencia o no procedió",
            "Cuando la visita de diagnóstico revela que el servicio no es viable"
        ],
        "correcta": 1,
        "explicacion": "Un lead se mueve a PERDIDOS cuando el prospecto comercial decidió contratar con la competencia o no procedió. Se detienen los flujos de seguimiento automático y se registra la causa de pérdida."
    },
    {
        "pregunta": "¿Cada cuánto debe la asesora de Fosas revisar las etapas de 'apoyo humano fosas'?",
        "opciones": [
            "Una vez al día por la mañana",
            "De forma prioritaria y constante, estos leads requieren atención inmediata",
            "Solo cuando recibe una notificación de tarea"
        ],
        "correcta": 1,
        "explicacion": "Las buenas prácticas indican revisar constantemente y de forma prioritaria las etapas de 'apoyo humano' porque estos prospectos requieren atención directa e inmediata."
    },
    {
        "pregunta": "¿Qué documento envía el bot automáticamente a los nuevos prospectos de Fosas?",
        "opciones": [
            "Una cotización estimada de precios",
            "El PDF de presentación de Saniglobal",
            "El contrato de servicio para firma digital"
        ],
        "correcta": 1,
        "explicacion": "Al primer contacto, el bot envía el PDF de presentación de Saniglobal al prospecto como parte del flujo de calificación inicial."
    },
]

QUIZ_TRAMPAS = [
    {
        "pregunta": "¿Cuántas etapas tiene el Embudo de Trampas de Grasa?",
        "opciones": [
            "11 etapas",
            "13 etapas",
            "18 etapas"
        ],
        "correcta": 0,
        "explicacion": "El Embudo de Trampas de Grasa tiene 11 etapas: Contacto Inicial, CLIENTE ACTUAL, APOYO HUMANO, CERRADOS NO POTENCIAL, SOLICITUD DE INFORMACIÓN, VISITA DIAGNÓSTICO, COTIZACIÓN, SEGUIMIENTO, EN PAUSA, GANADOS y PERDIDOS."
    },
    {
        "pregunta": "¿Bajo qué condición la cotización de Trampas de Grasa es AUTOMÁTICA?",
        "opciones": [
            "Cuando son 1 o 2 trampas estándar de 200 LTS",
            "Cuando el cliente envía fotos y videos de las trampas",
            "Cuando el acceso para el camión es fácil (a pie de trampa)"
        ],
        "correcta": 0,
        "explicacion": "La cotización es automática vía webhook únicamente cuando la solicitud es para 1 o 2 trampas de capacidad estándar (200 LTS). Si supera esto (más trampas o más litros), el asesor debe cotizar manualmente."
    },
    {
        "pregunta": "¿Cuál es el nombre del botón que el asesor de Trampas debe presionar al enviar una cotización manual?",
        "opciones": [
            "Botón 'Cotización realizada'",
            "Botón 'Cotización de trampas de grasa manual'",
            "Botón 'Enviar propuesta comercial'"
        ],
        "correcta": 1,
        "explicacion": "En el embudo de Trampas, el botón específico se llama 'Cotización de trampas de grasa manual'. Esto es diferente al botón de Baños que se llama 'Cotización realizada'."
    },
    {
        "pregunta": "¿Cómo se gestionan las quejas de clientes en Trampas de Grasa?",
        "opciones": [
            "Se trasladan al Embudo de Quejas Sanitarios como en Baños",
            "Se resuelven de forma local agregando la etiqueta manual 'Queja' en la etapa actual",
            "Se envían al departamento de control de calidad por correo"
        ],
        "correcta": 1,
        "explicacion": "Las quejas de Trampas NO se mandan a otro embudo. El asesor debe colocar manualmente la etiqueta 'Queja' y resolver directamente en la etapa actual. Esto es diferente a Baños donde sí se trasladan al Embudo de Quejas."
    },
    {
        "pregunta": "¿Qué datos técnicos solicita el bot de Trampas de Grasa en su flujo de calificación?",
        "opciones": [
            "Solo el número de trampas y la dirección de entrega",
            "Número de trampas, capacidad, material, tipo de acceso, distancia de manguera, rampas y fotos/videos",
            "Tipo de grasa, frecuencia de limpieza y presupuesto disponible"
        ],
        "correcta": 1,
        "explicacion": "El bot solicita: número de trampas, capacidad/tamaño, material (PVC, acero, concreto), tipo de acceso para la unidad, distancia del camión a la trampa, si cuenta con rampas accesibles, y solicita fotos/videos de evidencia."
    },
    {
        "pregunta": "¿Qué porcentaje de descuento ofrece el bot de Trampas cuando la objeción es precio en la etapa de Seguimiento?",
        "opciones": [
            "10% de descuento",
            "5% de descuento",
            "15% de descuento"
        ],
        "correcta": 1,
        "explicacion": "En la etapa de Seguimiento, si la objeción del cliente es precio, el bot ofrece un descuento del 5% y etiqueta al lead como 'Perdido por precio'."
    },
    {
        "pregunta": "Si un cliente de Trampas solicita 3 o más trampas, ¿qué sucede con la cotización?",
        "opciones": [
            "El bot cotiza automáticamente sumando las trampas",
            "El bot se pausa y el asesor debe cotizar manualmente, luego presionar el botón de cotización manual",
            "El bot rechaza la solicitud por exceder el límite"
        ],
        "correcta": 1,
        "explicacion": "Cuando son 3 o más trampas, o de capacidad mayor a 200 LTS, el bot se pausa y asigna el caso al asesor comercial para cotizar manualmente. Luego debe presionar el botón 'Cotización de trampas de grasa manual'."
    },
    {
        "pregunta": "¿Qué etapa del embudo de Trampas se activa cuando el bot no puede clasificar las respuestas del cliente?",
        "opciones": [
            "CERRADOS NO POTENCIAL",
            "APOYO HUMANO",
            "SOLICITUD DE INFORMACIÓN"
        ],
        "correcta": 1,
        "explicacion": "Cuando el cliente requiere asistencia directa o el bot no pudo clasificar sus respuestas, se activa la etapa APOYO HUMANO. Se detiene el bot y se crea una tarea comercial urgente al asesor."
    },
    {
        "pregunta": "¿Cuál es el sector principal de clientes para el servicio de Trampas de Grasa?",
        "opciones": [
            "Industria automotriz y metalúrgica",
            "Restaurantes, hoteles y comedores industriales",
            "Hospitales y centros de salud"
        ],
        "correcta": 1,
        "explicacion": "El servicio de limpieza y desazolve de trampas de grasa está dirigido principalmente a restaurantes, hoteles y comedores industriales."
    },
    {
        "pregunta": "¿Qué embudo debe tener seleccionado el asesor de Trampas en la barra lateral izquierda de Kommo?",
        "opciones": [
            "Embudo GPT Completo",
            "Embudo de Ventas",
            "Embudo de Trampas de grasa"
        ],
        "correcta": 2,
        "explicacion": "El asesor de Trampas debe tener seleccionado el 'Embudo de Trampas de grasa' en la sección de Leads del menú de la barra izquierda que siempre está fija."
    },
    {
        "pregunta": "¿Cuándo un lead de Trampas pasa a la etapa 'VISITA DIAGNÓSTICO'?",
        "opciones": [
            "Cuando el cliente solicita una demostración del servicio",
            "Cuando el proyecto es complejo y requiere inspección física antes de dar precio",
            "Cuando el bot necesita verificar los datos del cliente"
        ],
        "correcta": 1,
        "explicacion": "La etapa VISITA DIAGNÓSTICO es para proyectos complejos que requieren inspección física antes de dar precio. Se pausan las automatizaciones comerciales en espera del diagnóstico técnico."
    },
    {
        "pregunta": "¿Qué acción inmediata debe tomar el asesor cuando un lead cae en APOYO HUMANO en Trampas?",
        "opciones": [
            "Esperar a que el bot reintente la clasificación automática",
            "Tomar la conversación en el chat de forma inmediata para resolver y cotizar",
            "Enviar un correo al cliente solicitando que reintente el proceso del bot"
        ],
        "correcta": 1,
        "explicacion": "Cuando un lead llega a APOYO HUMANO, el asesor debe tomar la conversación en el chat de forma inmediata para resolver y cotizar. El bot ya se detuvo y no volverá a intentar."
    },
    {
        "pregunta": "¿Qué tipos de material de trampa puede identificar el bot en su cuestionario?",
        "opciones": [
            "Solo plástico y metal",
            "Plástico/PVC, Acero inoxidable/Metal, y Concreto/Obra civil",
            "Fibra de vidrio, Aluminio y Cerámica"
        ],
        "correcta": 1,
        "explicacion": "El bot ofrece tres opciones de material: Plástico/PVC, Acero inoxidable/Metal, y Concreto/Obra civil."
    },
    {
        "pregunta": "En la etapa SOLICITUD DE INFORMACIÓN de Trampas, ¿qué debe validar el asesor?",
        "opciones": [
            "El historial de pagos del cliente",
            "Los accesos de camión y requerimientos de manguera en la tarjeta del lead",
            "La capacidad financiera del cliente para pagar"
        ],
        "correcta": 1,
        "explicacion": "En la etapa SOLICITUD DE INFORMACIÓN, el asesor debe validar accesos de camión y requerimientos de manguera en la tarjeta del lead, además de datos fiscales antes de cotizar."
    },
    {
        "pregunta": "¿Qué pasa con los leads de Trampas clasificados como CERRADOS NO POTENCIAL?",
        "opciones": [
            "Se eliminan permanentemente del CRM después de 30 días",
            "El bot los mueve aquí de forma automática (spam, proveedores) y el asesor monitorea descartes ocasionalmente",
            "Se transfieren a otro embudo para una segunda evaluación"
        ],
        "correcta": 1,
        "explicacion": "Los leads CERRADOS NO POTENCIAL son movidos automáticamente por el bot (spam, proveedores, descartados). El asesor debe monitorear los descartes ocasionalmente para verificar que no haya leads válidos."
    },
    {
        "pregunta": "¿Qué categorías de distancia del camión a la trampa maneja el bot?",
        "opciones": [
            "Cerca (0-5m) y Lejos (más de 5m)",
            "Corta (0-10m), Media (11-20m), Larga (más de 21m)",
            "A pie de calle, Interior del edificio, Sótano"
        ],
        "correcta": 1,
        "explicacion": "El bot clasifica la distancia en tres categorías: Corta (0-10 metros), Media (11-20 metros) y Larga (más de 21 metros)."
    },
    {
        "pregunta": "¿Cuándo el asesor de Trampas debe mover un lead a la etapa EN PAUSA?",
        "opciones": [
            "Cuando el lead no responde en 72 horas",
            "Cuando el servicio es viable pero lo requieren a más de 1 mes de distancia",
            "Cuando el bot detecta un problema técnico con la trampa"
        ],
        "correcta": 1,
        "explicacion": "La etapa EN PAUSA es para servicios viables proyectados a más de 1 mes de distancia. Se detienen flujos de seguimiento diario y el asesor debe agendar tarea de seguimiento en calendario."
    },
    {
        "pregunta": "¿Qué debe hacer el asesor de Trampas al registrar un lead como PERDIDOS?",
        "opciones": [
            "Eliminar todos los datos del cliente por protección de datos",
            "Archivar y registrar la causa de pérdida (objeción de precio, cobertura, etc.)",
            "Enviar un correo de despedida al cliente"
        ],
        "correcta": 1,
        "explicacion": "Al pasar un lead a PERDIDOS se detienen todos los flujos de seguimiento automáticos. El asesor debe archivar y registrar la causa de pérdida (objeción de precio, cobertura, competencia, etc.)."
    },
    {
        "pregunta": "¿Cuál es la capacidad estándar de trampa que califica para cotización automática?",
        "opciones": [
            "100 LTS",
            "200 LTS",
            "500 LTS"
        ],
        "correcta": 1,
        "explicacion": "Solo las trampas de capacidad estándar de 200 LTS califican para cotización automática. Tamaños de 250 LTS o más requieren cotización manual por parte del asesor."
    },
    {
        "pregunta": "¿Qué sucede cuando un cliente ganado de Trampas vuelve a escribir?",
        "opciones": [
            "Se crea un nuevo lead independiente en el CRM",
            "El bot despliega menú interactivo en la etapa CLIENTE ACTUAL y el asesor atiende requerimientos o quejas con etiqueta manual",
            "Se le envía automáticamente una nueva cotización con los mismos datos anteriores"
        ],
        "correcta": 1,
        "explicacion": "Cuando un cliente ganado vuelve a escribir, se gestiona en la etapa CLIENTE ACTUAL. El bot despliega un menú interactivo y el asesor atiende requerimientos de nuevos servicios o resuelve inconformidades con la etiqueta manual 'Queja'."
    },
]
