# 📘 Guía de Capacitación: Cómo Funciona Nuestro Sistema de Ventas en Kommo

**Para:** Equipo de Ventas y Atención al Cliente  
**Plataforma:** Kommo CRM + WhatsApp / Meta  
**Última actualización:** Junio 2026

---

> [!IMPORTANT]
> **"El Embudo GPT Completo es el origen de todo."** Todos los prospectos entran por ahí primero, y desde ahí el sistema los canaliza al área correspondiente. Como nuestro equipo se divide por especialidades, esta guía está estructurada para que cada asesor consulte únicamente lo que le corresponde, además de contar con una sección de reglas generales de uso obligatorio para todos.

---

## 📌 Tabla de Contenidos

### ⚙️ PARTE I: BASES GENERALES (Para todo el equipo)
1. [Glosario rápido: términos clave](#glosario)
2. [El Embudo GPT Completo: El Origen de todo](#gpt-completo)
3. [Reglas de Operación Diaria (Meta, Asignación, etc.)](#reglas-operacion)
4. [Embudos de Soporte y Regla Especial de Quejas](#embudos-soporte)

### 🚽 SECCIÓN II: RENTA DE BAÑOS PORTÁTILES
* **Vendedor Responsable:** Daniel Herrera (Usuario 12824423)
* [Flujo y 17 etapas del Embudo de Ventas (Baños)](#seccion-baños)
* [Secuencia de preguntas del Bot de Renta](#preguntas-baños)
* [Gestión de Clientes Activos (Ganados, Reactivaciones y Retiros)](#clientes-activos-baños)

### 🌀 SECCIÓN III: SERVICIOS ESPECIALES Y FOSAS SÉPTICAS
* **Vendedora Responsable:** Livier Mora (Usuario 13346199)
* [Flujo y 13 etapas del Embudo de Fosas](#seccion-fosas)
* [Secuencia de preguntas del Bot de Fosas](#preguntas-fosas)
* [Filtro crítico de Casa Habitación (Exclusión)](#filtro-fosas)
* [Visita de Diagnóstico y Seguimiento](#seguimiento-fosas)

### 🍳 SECCIÓN IV: TRAMPAS DE GRASA
* **Vendedor Responsable:** Asesor de Trampas de Grasa
* [Flujo y 8 etapas del Embudo de Trampas](#seccion-trampas)
* [Secuencia de preguntas del Bot de Trampas](#preguntas-trampas)
* [Cotización Automática vs. Cotización Manual](#cotizacion-trampas)

---

<a name="glosario"></a>
## ⚙️ PARTE I: BASES GENERALES (Para todo el equipo)

### 1. 📖 Glosario Rápido

Antes de entrar de lleno, aquí están los términos que usamos constantemente:

| Término | Qué significa |
|---|---|
| **Lead / Prospecto** | Cualquier persona o empresa que nos contacta por primera vez a través de nuestros canales digitales |
| **Embudo (Pipeline)** | El "camino" o proceso de ventas estructurado en etapas secuenciales por el que transita un prospecto |
| **Etapa (Estatus)** | La fase específica de negociación en la que se encuentra el cliente dentro de un embudo |
| **Bot / Automatización** | Mensajes y acciones lógicas ejecutadas por el sistema sin intervención humana |
| **Etiqueta (Tag)** | Marcas de color añadidas a la tarjeta del cliente para filtrado rápido, campañas o disparar automatizaciones |
| **Webhook** | Solicitud HTTP automática para enviar datos a microservicios externos (ej. cotizadores automáticos) |
| **Ventana de 24h** | Regla de Meta que limita el envío de mensajes libres a 24 horas desde la última interacción del usuario |
| **Mensaje rápido** | Plantillas de texto predefinidas en Kommo que se invocan con la tecla '/' para agilizar la comunicación |
| **Casa Habitación** | Etiqueta y filtro aplicado por el bot para descartar y cerrar solicitudes residenciales no viables en fosas |

---

<a name="gpt-completo"></a>
### 2. 🌟 El Embudo GPT Completo — El Origen de Todo

Cuando alguien nos escribe por primera vez —sea por WhatsApp, Facebook o Instagram— su conversación aterriza automáticamente aquí. Este bot es el **recepcionista virtual de la empresa**. Se llama "GPT Completo" porque usa inteligencia artificial para entender lo que el cliente escribe y guiarlo por el camino correcto.

**Lo primero que hace el bot** es presentarse y preguntar:

> *"Mucho gusto, ¿en qué te podemos servir hoy? ¿Te interesa rentar un baño portátil o buscas algún servicio especializado como limpieza de fosas sépticas, trampas de grasa, recolección de residuos?"*

El cliente tiene tres botones para elegir:
- 🚽 **Rentar baños** → El bot lo mueve al **Embudo de Ventas (Baños)** y lo asigna a Daniel Herrera.
- 🔧 **Servicios especiales** → El bot lo mueve al **Embudo de Servicios Especiales (Fosas)** y lo asigna a Livier Mora.
- 💬 **Otro asunto** → El bot lo mueve al **Embudo de Otros Asuntos**.

> [!NOTE]
> Si el cliente escribe en lugar de usar un botón (ej. "renta de sanitarios" o "limpieza de fosa"), el sistema intenta detectarlo y enviarlo al embudo correcto automáticamente. Si no puede clasificarlo, lo pasa a soporte humano.

#### ¿Qué pasa si el cliente no responde?
El bot espera **61 minutos**. Si no hay respuesta, pregunta si prefiere recibir una llamada. Si tampoco responde, espera **5 horas**, manda un mensaje de despedida cordial y espera **24 horas**. Si en ese tiempo no hay reacción, el sistema le pone la etiqueta **"Sin respuesta"** y cierra la conversación automáticamente.

---

<a name="reglas-operacion"></a>
### 3. 🛠️ Reglas de Operación Diaria

#### ⏱️ La Regla de las 24 Horas de Meta
Meta (WhatsApp, Facebook, Instagram) solo permite responder libremente dentro de las **24 horas posteriores al último mensaje del cliente**. 
- Si la ventana se cierra, no puedes enviar mensajes libres.
- Para reabrirla, debes enviar una **Plantilla HSM aprobada** (tiene costo).
- Por esto, nuestros bots de seguimiento operan a las **21 horas** para enviar el recordatorio antes de que expire la ventana.
- **Tu deber:** Responde rápido. No dejes conversaciones abiertas de un día para otro si están a punto de expirar.

#### 👤 Asignación de Leads a Otro Usuario
Cada lead tiene un asesor asignado. Si necesitas transferirlo (por carga de trabajo o territorio):
- Ve a la tarjeta del lead, busca el campo "Responsable" y cámbialo al usuario correcto.
- Guarda los cambios. El sistema le notificará automáticamente y reasignará las tareas pendientes.
- ⚠️ **REGLA DE ORO DE ASIGNACIÓN:** Cuando reasignes una oportunidad a un compañero porque te llegó a ti por error, **debes dejar obligatoriamente una nota** en la tarjeta con cualquier dato extra, comentario o necesidad que el cliente ya te haya compartido en el chat anterior. Esto evita la pérdida de información y facilita el trabajo del nuevo asesor asignado.

#### 🖱️ Botones Manuales en la Tarjeta
Muchos bots de seguimiento no se activarán a menos que le des clic al botón manual correspondiente dentro de la tarjeta del lead (ej. "Cotización realizada", "Cotización de trampas de grasa manual", "Baño entregado"). **Si no das clic, el cliente se queda congelado sin automatizaciones.**

#### ⚡ Mensajes Rápidos
Escribe `/` (diagonal) en el chat para buscar plantillas predefinidas. Úsalas para saludos, cuentas de pago o preguntas frecuentes y mantén la consistencia profesional del equipo.

---

<a name="embudos-soporte"></a>
### 4. 😤 Embudos de Soporte y Regla Especial de Quejas

#### 🚽 Renta de Baños (Daniel Herrera): Embudo de Quejas dedicado
* **¿Cómo se maneja?** Si un cliente de Baños tiene un reporte o inconformidad, la conversación se traslada de inmediato al **Embudo de Quejas Sanitarios (Pipeline 12717196)** en la etapa `INICIO QUEJA`.
* **Acción:** El sistema le pone la etiqueta **"Quejas"** y crea alertas urgentes para resolución inmediata por el equipo de soporte.

#### 🌀 Fosas (Livier Mora) y 🍳 Trampas: Resolución Local (Misma Etapa)
* **¿Cómo se maneja?** A diferencia de baños, las quejas de fosas sépticas o trampas de grasa **NUNCA se envían a otro embudo**.
* **Acción obligatoria:** El asesor responsable debe mantener el lead en su embudo y etapa actual (o en la etapa `CLIENTE ACTUAL` si es post-venta), **colocar manualmente la etiqueta `Queja`** al contacto, y dar seguimiento y resolución al inconveniente directamente allí mismo.

#### Embudo de Otros Asuntos (Pipeline 13756408)
* **¿Cuándo llega?** Cuando eligen "Otro asunto" en el menú principal del Bot GPT Completo.
* **Funcionamiento:** El bot filtra si es:
  - *Empleo:* Da datos de RH y pone la etiqueta **"Vacante laboral"**.
  - *Proveedores:* Da datos de compras y pone la etiqueta **"Proveedores"**.
  - *Otros:* Crea tarea de soporte humano.
* **Cierre:** Al no ser prospectos comerciales, se mueven a la etapa **Cerrado**.

---

<a name="seccion-baños"></a>
## 🚽 SECCIÓN II: RENTA DE BAÑOS PORTÁTILES
### Asesor Responsable: Daniel Herrera (Usuario 12824423)
* **Embudo en Kommo CRM:** Embudo de ventas (este es el que se debe tener seleccionado en la sección de Leads, en el menú de la barra izquierda que siempre está fija).

#### Vista general de las 17 etapas del Embudo de Ventas (Baños)
```
Solicitud/Contacto → apoyo humano → Embudo caliente → Solicitud de información → Cotizado/Cotización 
→ Seguimiento automático / Campañas frío / Campañas caliente → Programado → Baño entregado (Ganados)
↘ En pausa / Solicitud retiro / Quejas sin resolver / Perdido reactivable / Perdidos / Cerrado
```

---

### Explicación Etapa por Etapa (Baños):

1. #### 📥 Solicitud de Cotización / Contacto Inicial
   * **¿Cómo llega?** El cliente elige "Rentar baños" en el menú inicial. El bot lo asigna a Daniel Herrera.
   * **Automatización:** El bot recopila los datos para cotizar:
     1. *¿Obra o Evento?* (Recomienda cantidad según tipo y personas).
     2. *¿Cuántos baños?* (Si pide 3 o más, se pasa a Daniel para atención manual).
     3. *¿Tipo de baño?* (Sencillo vs. Con Lavamanos. Muestra fotos de comparación).
     4. *¿Por cuánto tiempo?* (Por mes/quincena en obra, por día/semana en eventos).
     5. *¿Dirección de entrega?* (Valida que sea texto y no un pin de ubicación. Debe estar en ZM Guadalajara o ZM San Luis Potosí).

2. #### 👤 Apoyo Humano
   * **¿Cómo llega?** Si el bot no puede clasificar la respuesta del cliente, o si el cliente escribe un mensaje solicitando un asesor humano de forma expresa, el lead se mueve a este estatus.
   * **Acción:** Detiene las preguntas del bot y genera una tarea urgente para Daniel Herrera.

3. #### 🌡️ Etapa: Embudo Caliente
   * **¿Qué significa?** El cliente está respondiendo activamente al chat en tiempo real.
   * **Regla de oro:** **No se disparan mensajes automáticos** en esta etapa para evitar interrumpir o confundir al cliente mientras chatea en vivo con el asesor.

4. #### ℹ️ Etapa: Solicitud de Información
   * Etapa temporal donde el bot procesa y valida datos de dirección y datos fiscales antes de activar la cotización automática.

5. #### 💰 Etapa: Cotizado / Cotización
   * **Ruta Automática:** Si el bot recopiló todos los datos, calcula el precio, envía la propuesta en PDF y mueve el lead a esta etapa.
   * **Ruta Manual:** Si Daniel Herrera envía la propuesta manualmente (ej. cuando son 3 o más baños), **es obligatorio dar clic en el botón "Cotización realizada"** en la tarjeta del lead.
   * **Qué hace el bot aquí:** Pone la etiqueta **"Propuesta enviada"** y ofrece botones de ayuda rápida (*Pasos para contratar*, *Formas de pago*, *Tiempos de entrega*).
   * **Descuento del 5%:** Si el cliente no responde tras **2 horas** de recibir la cotización, el bot le ofrece un 5% de descuento por WhatsApp y le añade la etiqueta **"-5% descuento"**.

6. #### 🤖 Etapa: Seguimiento Automático
   * **¿Cómo llega aquí?** Cuando una cotización es enviada, el bot de seguimiento inicia una espera de **21 horas**. Si el cliente no escribe ningún mensaje, el bot envía un mensaje automático de seguimiento. Si transcurren **24 horas más** y el cliente sigue sin responder, el sistema lo mueve automáticamente a esta etapa y le coloca la etiqueta **"Sin respuesta"**.
   * **Cómo funciona:** Mover al cliente aquí permite limpiar la bandeja de cotizaciones activas del vendedor. El bot detiene su secuencia aquí, pero si el cliente llega a responder en el futuro, el CRM lo detecta y vuelve a notificar a Daniel para atención humana.

7. #### ❄️ Etapa: Campañas Frío
   * **¿Qué significa?** Es la etapa designada para almacenar aquellos leads provenientes de campañas masivas de recontacto (ej. promociones masivas enviadas a clientes antiguos o perdidos) que **NO respondieron** al mensaje de la campaña o no mostraron interés.

8. #### 🔥 Etapa: Campañas Caliente
   * **¿Qué significa?** Si los leads de la campaña de recontacto **sí responden el mensaje de forma positiva y muestran interés** en rentar de nuevo, el sistema los mueve automáticamente a esta etapa.
   * **Prioridad:** Esta etapa es de máxima prioridad. Daniel Herrera debe dar seguimiento manual inmediato a estos prospectos calientes para concretar la renta.

9. #### 📅 Etapa: Programado
   * El servicio ha sido aceptado y programado en agenda, el pago de la garantía o primer mes está confirmado, pero el baño aún no se entrega físicamente.

10. #### 🚪 Etapa: Baño Entregado (Ganados)
    * Cuando se ganen los leads por primera vez, el lead se debe mover al embudo de **Ganados**.
    * **⚠️ BOTÓN OBLIGATORIO:** Se debe usar preferentemente el botón de la tarjeta que dice **"Baño entregado y ganado"**, ya que este botón activa un mayor número de automatizaciones que el botón de entrega ordinario.

11. #### 🔄 Ganado cliente reactiva
    * **¿Cómo funciona?** Esta es la etapa donde deben vivir de ahí en adelante todos los clientes que ya se habían ganado pero que se reactivaron por cualquier razón.
    * **Lógica de flujo:** Una vez que el cliente está en **Ganados**, si este vuelve a iniciar una conversación (pide información, seguimiento o retiros) y **se finaliza/resuelve esa conversación**, el lead se debe mover a esta etapa, donde residirá permanentemente.

12. #### 🚚 Solicitud retiro
    * El cliente solicita que se recoja el baño. El bot le da los pasos para confirmarlo y le dispara la encuesta de emojis.

13. #### 😤 Quejas sin resolver
    * Estatus donde se concentran los reportes e inconformidades de baños para su seguimiento técnico y operativo.

14. #### ⏸️ En Pausa / Pausado
    * Leads viables que indicaron que requieren el servicio en más de 1 mes en el futuro.

15. #### 🔴 Perdido Reactivable
    * Prospectos viables que no cerraron por precio o agenda, archivados para futuras promociones.

16. #### ❌ Perdidos
    * Servicios eventuales terminados, o clientes que contrataron con la competencia de manera definitiva.

17. #### 🚫 Cerrado
    * Contactos no viables (fuera de zona, proveedores, spam, empleos).

---

<a name="clientes-activos-baños"></a>
### 📋 Gestión y Reactivación de Clientes Ganados (Tengan o no Baño Activo)

> [!IMPORTANT]
> **Regla de oro sobre los clientes Ganados:**
> 1. **Asegurar el estatus:** Cuando una venta se concrete por primera vez, se debe mover el lead al embudo de **Ganados** y utilizar preferentemente el botón **"Baño entregado y ganado"**, ya que este botón contiene más automatizaciones integradas.
> 2. **Reactivación y finalización:** Si un cliente en **Ganados** vuelve a iniciar una conversación (para pedir información, seguimiento, retiros, etc.), una vez que **se finalice/resuelva esa conversación**, el lead debe mandarse a la nueva etapa llamada **Ganados Cliente reactiva**.
> 3. **Residencia permanente:** En la etapa de **Ganados Cliente reactiva** es donde deberá vivir siempre aquel cliente que ya se había ganado previamente, pero que se reactivó por cualquier razón.

#### Menú de Cliente Actual ("Ganados el cliente reactiva")
Cuando un cliente ganado nos vuelve a escribir (tenga o no un baño físicamente en sitio), el bot le presenta un menú interactivo:
- **Retirar o reubicar:** Si elige *Retirar*, le da instrucciones de enviar un correo a operaciones. Cuando el cliente confirma el envío, se le dispara la **encuesta de emojis** y al finalizar se le regala un **cupón del 10% de descuento** para reactivación. Si dice que no quiere retirar, se le ofrece ampliar la renta.
- **Quiero otro baño:** Envía al cliente al proceso de cotización agregando la tarea "Cotizar nuevo baño".
- **Reportes y quejas:** Mueve el lead automáticamente al embudo especializado de **Quejas sanitarios (Pipeline 12717196)** en la etapa `INICIO QUEJA` para atención manual urgente.

---

<a name="seccion-fosas"></a>
## 🌀 SECCIÓN III: SERVICIOS ESPECIALES Y FOSAS SÉPTICAS
### Asesora Responsable: Livier Mora (Usuario 13346199)
* **Embudo en Kommo CRM:** Embudo Fosas GDL (este es el que se debe tener seleccionado en la sección de Leads, en el menú de la barra izquierda que siempre está fija).

#### Vista general del Embudo de Fosas y Especiales (13 etapas)
```
Contacto inicial → CASA HABITACIÓN → Solicitud de información → Visita de diagnóstico → Cotización 
→ Seguimiento → En pausa → CLIENTE ACTUAL (Reactivación) 
→ CLIENTES SLP → Apoyo humano fosas → GANADOS → PERDIDOS → CERRADOS NO POTENCIAL
```

---

### Etapa por Etapa: Fosas Sépticas y Lodos

1. #### 📥 Contacto inicial
   * **¿Cómo llega?** El cliente elige "Servicios especiales" en el menú inicial y selecciona una categoría aplicable (como fosas sépticas, lodos, vinazas, etc.). El sistema lo asigna automáticamente a Livier Mora.
   * **Preguntas del Bot para Calificación:**
     1. *¿Qué residuo es?* (Fosas sépticas, lodo biológico, aguas de proceso, vinazas, etc. Se envía PDF de presentación comercial de Saniglobal).
     2. *¿Estado del material?* (Líquido, Lodo o pasta, Sólido o polvo).
     3. *¿Dónde está almacenado?* (Fosa/cisterna, Tambo/tolva/sacos, Sobre terreno).
     4. *¿Volumen o cantidad?* (Menos de 5,000 lt/kg, 5,000 a 10,000, Más de 10,000).

2. #### 🏠 CASA HABITACIÓN (Filtro Crítico)
   * **¿Qué significa?** Es la etapa a la que se envían automáticamente los prospectos residenciales que no califican para nuestro servicio comercial/industrial.
   * **Cómo actúa el Bot:** El bot pregunta: *¿Es para una casa habitacional o residencial?* Si responde "Sí", el bot le coloca la etiqueta **`CASA HABITACIÓN`**, envía el mensaje de rechazo cortés, y mueve el lead a la etapa **Cerrado**. Si responde "No", continúa con el flujo normal.

3. #### ℹ️ Solicitud de información
   * Validación técnica de las características físicas del residuo, accesos y datos de facturación de la empresa.

4. #### 🔎 Visita de Diagnóstico
   * En proyectos complejos de fosas, antes de cotizar se requiere una visita física. Livier programa la visita y el lead se mantiene en esta etapa en espera del reporte técnico de condiciones de acceso y tipo de residuo.

5. #### 💰 Cotización (Fosas)
   * Las fosas requieren cotizaciones detalladas y manuales. Livier elabora la propuesta. Al enviarla al cliente, **debe presionar obligatoriamente el botón "Cotización realizada"** en Kommo para activar el seguimiento automático de 21 horas. Si no lo presiona, el sistema no disparará los recordatorios automáticos.

6. #### 📞 Seguimiento
   * Pasan **21 horas** sin respuesta del cliente. El bot le envía un mensaje de seguimiento preguntando por el estado de la decisión.
   * Si el cliente indica que no contratará por *Precio*, el bot le ofrece un cupón de descuento del **5% de descuento** (a diferencia de baños, aquí el descuento máximo es del 5%) y añade la etiqueta **`Perdido por precio`**.

7. #### ⏸️ En pausa
   * **¿Cuándo se usa?** El cliente tiene intenciones de contratar pero requiere el servicio en más de 1 mes en el futuro. Mover el lead a esta etapa mantiene despejado el tablero de seguimiento diario.

8. #### 🔄 CLIENTE ACTUAL (Reactivación y Quejas)
   * **¿Cómo funciona?** Si un cliente en **Ganados** vuelve a escribir, el bot de reactivación lo mueve automáticamente a esta etapa y le muestra un menú interactivo (Solicitar servicio, reportes y quejas, dudas).
   * ⚠️ **REGLA CRÍTICA DE QUEJAS:** Las quejas de fosas **NO SE ENVIÁN A OTRO EMBUDO**. El asesor debe mantener el lead en esta etapa de CLIENTE ACTUAL, **etiquetarlo manualmente con el tag `Queja`** y darle resolución técnica directamente aquí.

9. #### 📍 CLIENTES SLP
   * Control y almacenamiento de servicios y prospectos pertenecientes a la zona de San Luis Potosí.

10. #### 👤 Apoyo humano fosas
    * Cuando el cliente requiere atención directa de Livier Mora o el bot se detiene por datos no clasificados.

11. #### 🏆 GANADOS
    * Venta concretada con éxito. El servicio técnico fue programado, ejecutado y pagado.

12. #### ❌ PERDIDOS
    * Clientes que decidieron contratar definitivamente con competidores sin opción de recuperación.

13. #### 🚫 CERRADOS NO POTENCIAL
    * Contactos no viables (fuera de zona, proveedores, spam, o las casas habitación filtradas automáticamente).

---

<a name="seccion-trampas"></a>
## 🍳 SECCIÓN IV: TRAMPAS DE GRASA
### Asesor Responsable: Asesor de Trampas de Grasa
* **Embudo en Kommo CRM:** Embudo de Trampas de grasa (este es el que se debe tener seleccionado en la sección de Leads, en el menú de la barra izquierda que siempre está fija).

#### Vista general del Embudo de Trampas de Grasa (8 etapas)
```
Contacto inicial → apoyo humano → COTIZACIÓN → En seguimiento 
→ En pausa → Perdido reactivable → Perdidos → Cerrado
```

---

### Etapa por Etapa: Trampas de Grasa

1. #### 📥 Contacto inicial
   * **¿Cómo llega?** El cliente elige "Servicios especiales" en el menú inicial y selecciona **Grasas alimenticias (trampas de grasa)**.
   * **Preguntas de Calificación del Bot:**
     1. *¿Cuántas trampas de grasa?* (Solo 1, 2, o 3 o más. Si pide 3 o más, el bot lo turna al asesor para cotización manual).
     2. *¿Capacidad o tamaño promedio?* (200 LTS estándar, 250 a 500 LTS, Más de 500 LTS. Tamaños mayores a 200 LTS van a cotización manual).
     3. *¿De qué material son?* (Plástico/PVC, Acero inoxidable/Metal, Concreto/Obra civil).
     4. *¿Cómo es el acceso para la unidad?* (A pie de trampa, Acceso complicado, Requiere permisos).
     5. *¿Distancia del camión a la trampa?* (Corta 0-10m, Media 11-20m, Larga más de 21m).
     6. *¿Cuenta con rampas accesibles?* (Sí, No lo sé, No).
     7. *Fotos/Videos:* Solicita evidencia visual para verificar las condiciones físicas antes del servicio.

2. #### 👤 Apoyo humano
   * Cuando el lead requiere asistencia directa del asesor de trampas o el bot se detiene por datos no clasificados.

3. #### 💰 COTIZACIÓN (Automática vs. Manual)
   * **Cotización Automática:** Si el cliente solicita **1 o 2 trampas de 200 LTS (estándar)** y responde todas las preguntas del bot, el sistema procesa el webhook. El bot le envía al cliente un enlace personalizado generado en el campo `{{lead.cf.1117077}}` con la cotización lista y mueve el lead a *COTIZACIÓN*.
   * **Cotización Manual:** Si el tamaño es mayor a 200 LTS, requiere permisos complejos o son más de 3 trampas, el bot pausa la automatización. El asesor debe formular la cotización manualmente. Al enviarla, **debe presionar obligatoriamente el botón "Cotización de trampas de grasa manual"** en Kommo para mover el lead al estatus de cotización.

4. #### 📞 En seguimiento
   * A las **21 horas** de haber enviado la cotización, el bot pregunta el estatus de la decisión.
   * Si el cliente rechaza por *Precio*, se le ofrece un cupón del **5% de descuento** y se le etiqueta como **"Perdido por precio"**.
   * ⚠️ **REGLA CRÍTICA DE QUEJAS:** Las quejas de trampas de grasa **NO SE ENVÍAN A OTRO EMBUDO**. El asesor debe mantener el lead en su etapa actual, **colocarle manualmente la etiqueta `Queja`** al contacto, y darle resolución directamente dentro de la etapa en que se encuentre el lead en este embudo.

5. #### ⏸️ En pausa
   * **¿Cuándo se usa?** El cliente necesita la limpieza en más de 1 mes en el futuro. Se mueve aquí para mantener limpio el tablero diario.

6. #### 🔴 Perdido reactivable
   * Prospectos comerciales viables que no concretaron el servicio por precio o agenda. Se guardan para futuras campañas comerciales y promociones.

7. #### ❌ Perdidos
   * Servicios eventuales concluidos, o clientes que contrataron con la competencia.

8. #### 🚫 Cerrado
   * Contactos no viables (fuera de zona, proveedores, spam, empleos).

---

## 📌 Tabla Resumen de Reglas, Cupones y Gestión de Quejas

| Embudo | Descuento Inicial (Sin respuesta) | Cupón en Seguimiento (Objeción de Precio) | Disparador de Seguimiento | Gestión de Quejas y Soporte |
|---|---|---|---|---|
| **Baños (Daniel Herrera)** | **5%** (a las 2 horas sin respuesta) | **10%** (en seguimiento de 21h) | Botón manual "Cotización realizada" / Webhook automático | **Se traslada al embudo especializado de Quejas** (Pipeline 12717196) |
| **Fosas (Livier Mora)** | N/A (Cotización siempre manual) | **5%** (en seguimiento de 21h) | Botón manual "Cotización realizada" | **Resolución local en la etapa CLIENTE ACTUAL** (Tag manual `Queja`) |
| **Trampas (Asesor Trampas)** | N/A | **5%** (en seguimiento de 21h) | Botón manual "Cotización de trampas de grasa manual" | **Resolución local en la etapa actual** (Tag manual `Queja`) |


---

<a name="buenas-practicas-servicio"></a>
## 🚀 Buenas Prácticas de Servicio (Uso de Kommo CRM)

Para brindar una atención comercial de excelencia, agilizar el flujo de ventas y asegurar que ningún prospecto se pierda, todos los asesores deben cumplir estrictamente con el siguiente listado de buenas prácticas:

*   **⏱️ Revisar Kommo CRM cada 5 minutos:** Mantén la plataforma abierta y activa en tu navegador o aplicación móvil. Debes revisarla de manera continua para enterarte de inmediato de nuevos mensajes, cambios de estatus o asignación de tareas.
*   **📥 Monitorear la entrada de nuevos leads:** Revisa constantemente la sección de Chats para verificar qué nuevos leads han entrado e identificar si el bot recepcionista los está direccionando de forma correcta.
*   **🚨 Reportar anomalías al administrador:** Si notas que un lead se queda trabado, que el bot no responde, o detectas que un webhook no generó una cotización automática, repórtalo de inmediato con el administrador del sistema para solucionarlo a tiempo.
*   **👤 Estar revisando constantemente las etapas de "Apoyo Humano":** Consulta de forma prioritaria las etapas de `apoyo humano` en todos los embudos (Baños, Fosas y Trampas). Estos prospectos requieren atención directa e inmediata porque el bot no logró calificar su duda o solicitaron hablar directamente con un asesor.
*   **📞 Dar seguimiento por llamada telefónica:** No dependas únicamente de los chats escritos. Para los prospectos que se encuentren en el **Embudo Caliente** (chat activo) o en fases de **Seguimiento**, realiza una llamada telefónica. Esto rompe objeciones rápidamente, genera confianza y acelera drásticamente el cierre de la venta.
*   **🏷️ Poner etiquetas (Tags) siempre:** Acostúmbrate a catalogar a tus clientes usando etiquetas manuales cuando sea necesario (ej. `Queja`, `Propuesta enviada`, `-5% descuento`, `Sin respuesta`). Esto mantiene tu tablero ordenado y facilita campañas futuras de marketing masivo.

---

<a name="preguntas-respuestas-guia"></a>
## ❓ Sección de Preguntas y Respuestas (Q&A) de la Guía de Ventas

A continuación se presenta un resumen estructurado en formato de preguntas y respuestas que abarca toda la lógica comercial de la guía:

*   **P1: ¿Cuál es el canal de entrada y flujo inicial de todos los prospectos de Saniglobal?**
    *   **R:** Todos los leads entran al **Embudo GPT Completo**. Un bot de bienvenida recopila su interés dándoles a elegir entre: *Rentar baños* (se turna a Baños y asigna a Daniel Herrera), *Servicios especiales* (se turna a Fosas/Trampas y asigna a Livier Mora/Asesor de Trampas) u *Otros asuntos* (RH, proveedores, soporte).
*   **P2: ¿Bajo qué circunstancias llega un lead al estatus de "Seguimiento Automático" en el embudo de Baños?**
    *   **R:** Ocurre de forma 100% automática. Cuando el bot o el asesor envían una cotización, si el cliente no responde en 21 horas, el bot le envía un seguimiento automático. Si pasan otras 24 horas sin respuesta (45 horas de silencio en total), el CRM lo traslada a la etapa *Seguimiento automático* con la etiqueta `Sin respuesta` para limpiar el tablero principal del vendedor.
*   **P3: ¿Cuál es la política para solicitudes residenciales de limpieza de fosas sépticas o desazolves?**
    *   **R:** Saniglobal **no brinda servicios residenciales** (casas habitación o domicilios particulares) en Servicios Especiales. El bot les pregunta directamente el tipo de propiedad; si responden que "Sí" es residencial, el bot les coloca el tag `CASA HABITACIÓN`, les envía un mensaje cortés de rechazo y los mueve a **Cerrado** automáticamente.
*   **P4: ¿Cuándo califica una trampa de grasa para cotización automática en su embudo?**
    *   **R:** Únicamente cuando la solicitud es para **1 o 2 trampas** y ambas de capacidad estándar (**200 LTS**). Si son 3 o más trampas, o de mayor capacidad (250L+), el bot de desazolves se pausa y asigna el caso al asesor comercial para cotizar manualmente.
*   **P5: ¿Cómo se diferencian las reglas de soporte y quejas entre los embudos de Baños, Fosas y Trampas?**
    *   **R:**
        - **En Baños:** Las inconformidades de los clientes se transfieren de inmediato al **Embudo de Quejas Sanitarios** (Pipeline 12717196) en `INICIO QUEJA` para su resolución por personal de soporte.
        - **En Fosas y Trampas:** Las quejas **no se envían a otro embudo**; deben ser resueltas por el asesor responsable de forma local dentro de la misma etapa (o CLIENTE ACTUAL) agregando la etiqueta manual `Queja`.
*   **P6: ¿Qué debes hacer bajo la "Regla de Oro de Asignación" si te llega un prospecto por error?**
    *   **R:** Si te llega un lead por error y necesitas asignarlo a un compañero, debes cambiar el Responsable en Kommo CRM y **dejar obligatoriamente una nota interna** detallando cualquier dato extra, comentario o necesidad que el cliente ya te haya compartido en la conversación previa para no perder el contexto.
*   **P7: ¿Cómo funciona la oferta de descuento en el embudo de Baños?**
    *   **R:** Dos horas después de enviar una cotización (manual o automática), si el cliente no responde, el bot le envía de forma automática un incentivo con un **5% de descuento** sobre el costo y agrega la etiqueta `-5% descuento`.
*   **P8: ¿Cómo funciona la reactivación para un cliente que ya fue ganado?**
    *   **R:** Cuando un cliente ya ganado vuelve a iniciar una conversación (para pedir información, seguimiento, retiros, etc.), una vez que finalice o se resuelva esa conversación, se le debe mover a la etapa **Ganados Cliente reactiva**, donde deberá vivir permanentemente de ahí en adelante.

---

<a name="guias-operacion-kommo"></a>
## 📖 Guías Prácticas de Operación en Kommo CRM para Vendedores

Para maximizar tus ventas, mantener tu bandeja limpia y hacer un seguimiento impecable, sigue estas instrucciones:

### 1. ⚡ Cómo Usar y Crear Respuestas Rápidas (Mensajes Rápidos)
* **¿Qué son?** Son textos precargados (ej. números de cuenta, requisitos de contratación, precios básicos) que evitan escribir lo mismo a cada cliente.
* **Cómo usarlas en el chat diario:**
  1. En el cuadro de texto del chat de un lead, escribe una barra diagonal `/`.
  2. Escribe palabras clave del título (ej. `/pagos` o `/requisitos`).
  3. El sistema filtrará las plantillas. Presiona `Enter` para cargar el texto y envíalo.
* **Cómo crear nuevas plantillas:**
  1. Ve a **Ajustes** (icono de engranaje) → **Mensajes rápidos**.
  2. Haz clic en **Añadir plantilla**.
  3. Escribe un título y el cuerpo del mensaje. Puedes usar variables dinámicas (como `{{contact.name}}` o `{{lead.price}}`) para personalizar los mensajes de forma automática.

### 2. 📅 Las Tareas y la Sección de Calendario
Las tareas en Kommo son recordatorios de acciones comerciales vinculados a un cliente. Tienen fecha, hora y responsable asignados.
* **Tipos de Tareas en Kommo:**
  - **Seguimiento:** Recordatorios de llamadas rutinarias o envío de propuestas.
  - **Reunión:** Visitas físicas de diagnóstico o reuniones de presupuesto.
  - **Personalizadas:** Tareas configuradas manualmente con descripciones particulares.
* **Monitoreo del Calendario:** Siempre debes revisar la sección de **Calendario** en el menú izquierdo de Kommo. Ahí verás organizadas tus tareas: las que están *en proceso* (pendientes) y las *vencidas* (que se pintan en color rojo). Mantener tareas vencidas (en rojo) indica negligencia comercial en tus leads y afecta las métricas del tablero de ventas.
* **Alarma Externa Obligatoria:** Las alertas del navegador pueden pasarse por alto. **Es obligatorio programar recordatorios externos** (como alarmas en tu celular personal o eventos sincronizados en Google Calendar) para contactar a los clientes en la fecha y hora exacta programada.

### 3. ✍️ Las Notas (Notes) — Registro de Acuerdos Especiales
Las notas son anotaciones internas y permanentes en la tarjeta del lead que no son visibles para el cliente.
* **Qué debes registrar en las notas para tu beneficio:**
  - Precios especiales acordados o descuentos autorizados.
  - **Requerimientos especiales del sitio de entrega:** Detalles logísticos esenciales (ej. *'La calle es estrecha, se requiere camión chico'*, *'Hay cables de alta tensión bajos en la entrada'*, *'El acceso requiere identificación previa'*).
  - Datos de contacto alternos (ej. *'Nombre de la secretaria: Patricia, ext: 102'*).
  - Información de facturación o RFC rápido.
* **Beneficio:** Si te vas de vacaciones o te enfermas, cualquier compañero podrá leer tus notas y dar soporte o seguimiento a tu cliente sin repetir preguntas que molesten al prospecto.

### 4. 💬 Bandeja de Chats Limpia y Filtros de Usuario
La bandeja de chats es tu canal diario de prospección. Si no la mantienes ordenada, perderás leads.
* **Importancia de mantener limpia la sección de chats:** Si dejas abiertas conversaciones ya atendidas o acumuladas, el chat se saturará y las conversaciones nuevas irán empujando hacia abajo a los leads entrantes. Estos se sepultarán en el fondo y se perderán porque expirará su ventana de 24 horas.
* **¿En qué momentos marcar como 'Cerrada' o 'Marcar como resuelto'?**
  - **Marcar como resuelto:** Se hace en cuanto has contestado la duda del cliente, le enviaste la información y no hay ninguna acción pendiente por hacer de tu parte en el chat. Esto quita la conversación de tu bandeja de chats activos y la mantiene limpia.
  - **Cerrar conversación / Marcar como cerrada:** Cuando el lead ya fue rechazado definitivamente (ej. Casa Habitación en fosas) o fue transferido a otro embudo (ej. Quejas en baños).
* **Filtros de Chat por Usuario:**
  Para ver solo lo que a ti te corresponde y no saturarte con leads ajenos:
  1. Abre la sección de **Chats**.
  2. Haz clic en la barra de búsqueda y filtros.
  3. En el campo **Responsable**, selecciona tu usuario (ej. Daniel Herrera o Livier Mora).
  4. Guarda el filtro. Ahora la pantalla te mostrará **únicamente** las conversaciones de leads asignados a ti, manteniendo tu espacio de trabajo enfocado al 100%.
