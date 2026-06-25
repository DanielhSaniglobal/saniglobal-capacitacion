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
    * Cuando el equipo de operaciones entrega el baño en el sitio, Daniel o el equipo de logística debe **dar clic al botón "Baño entregado"**.
    * **Acción del bot:** Dispara la encuesta post-servicio ("Recopila opiniones con emojis") y prepara la reactivación futura.

11. #### 🔄 Ganado cliente reactiva
    * **¿Cómo funciona?** Si un cliente que está en la etapa **Ganados** vuelve a escribir en el futuro (tenga o no un baño físicamente en sitio), el sistema rompe la espera y lo mueve automáticamente a esta etapa para dispararle el bot de reactivación con su menú interactivo de autogestión.

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
> 1. **Asegurar el estatus:** Siempre debes verificar que cuando una venta se concrete, el lead quede marcado en la etapa **Ganados**. Si no está en Ganados, el flujo se rompe.
> 2. **El disparador por mensaje:** Una vez en **Ganados**, el lead entra en una "pausa" de espera. En el momento en que ese cliente vuelve a escribirnos (incluso tiempo después), el sistema detecta que es un cliente ganado y **automáticamente lo mueve a la etapa de reactivación ("Ganado cliente reactiva")**. **Esto ocurre tenga o no tenga un baño activo en su sitio en ese momento.**
> 3. **¿Por qué funciona así?:** Esta transición automática al embudo de reactivación es lo que permite que se le dispare el menú de opciones (Bot GPT ganados / reactiva) para que el cliente pueda autogestionarse (solicitar retiros, quejas, rentar otro baño, consultar pagos, etc.) sin que tengas que intervenir de inmediato.

#### Menú de Cliente Actual ("Ganados el cliente reactiva")
Cuando un cliente ganado nos vuelve a escribir (tenga o no un baño físicamente en sitio), el bot le presenta un menú interactivo:
- **Retirar o reubicar:** Si elige *Retirar*, le da instrucciones de enviar un correo a operaciones. Cuando el cliente confirma el envío, se le dispara la **encuesta de emojis** y al finalizar se le regala un **cupón del 10% de descuento** para reactivación. Si dice que no quiere retirar, se le ofrece ampliar la renta.
- **Quiero otro baño:** Envía al cliente al proceso de cotización agregando la tarea "Cotizar nuevo baño".
- **Reportes y quejas:** Mueve el lead automáticamente al embudo especializado de **Quejas sanitarios (Pipeline 12717196)** en la etapa `INICIO QUEJA` para atención manual urgente.

---

<a name="seccion-fosas"></a>
## 🌀 SECCIÓN III: SERVICIOS ESPECIALES Y FOSAS SÉPTICAS
### Asesora Responsable: Livier Mora (Usuario 13346199)

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

<a name="recursos-kommo"></a>
## 🔗 Enlaces y Herramientas Oficiales de Kommo CRM

Para complementar tu capacitación, te sugerimos consultar los recursos oficiales de Kommo CRM:

1. **[Base de Conocimientos Oficial de Kommo (Recursos)](https://www.kommo.com/es/recursos/)**: El portal de ayuda principal de Kommo con manuales detallados de configuración, integraciones y facturación.
2. **[Calculadora de Precios de WhatsApp Business](https://www.kommo.com/es/calculadora-precios-whatsapp/)**: Herramienta interactiva para calcular el costo por mensaje y por país en Meta.
3. **[Generador de Enlaces de WhatsApp](https://www.kommo.com/es/como-crear-un-enlace-de-whatsapp/)**: Utilidad gratuita para generar URLs directas a WhatsApp y códigos QR para campañas comerciales de recontacto.
4. **[Manual de Creación de Salesbots](https://www.kommo.com/es/salesbot/)**: Documento técnico sobre el funcionamiento y diseño de flujos automatizados de respuesta.


---

<a name="guias-operacion-kommo"></a>
## 📖 Guías Prácticas de Operación en Kommo CRM para Vendedores

Para maximizar tus ventas y no interferir con las automatizaciones del sistema, sigue estas instrucciones paso a paso:

### 1. ⚡ Cómo Usar y Crear Respuestas Rápidas (Mensajes Rápidos)
* **¿Qué son?** Son plantillas de texto precargadas que te permiten contestar preguntas comunes (números de cuenta para depósitos, requisitos fiscales, etc.) en menos de 3 segundos.
* **Cómo usarlas en el chat diario:**
  1. Abre el chat del lead.
  2. Escribe una barra diagonal `/` en la caja de texto.
  3. Escribe palabras clave del título (ej. `/pagos` o `/pasos`). El sistema te filtrará las opciones.
  4. Presiona `Enter` para cargar el texto y envíalo.
* **Cómo crear nuevas plantillas:**
  1. Ve a **Ajustes** (icono de engranaje en la barra izquierda) → **Mensajes rápidos**.
  2. Haz clic en el botón **Añadir plantilla**.
  3. Escribe un título descriptivo y redacta el texto del mensaje. Puedes usar variables dinámicas (como `{{contact.name}}` o `{{lead.price}}`) para que Kommo llene los datos del cliente de forma automática.

### 2. 🤖 Cómo Usar y Activar Respuestas Automáticas (Salesbot)
* **¿Qué es?** Es el bot encargado de interactuar inicialmente con el cliente y guiarlo.
* **Cómo forzar la activación de un bot de forma manual:**
  1. Abre la tarjeta del lead.
  2. En el panel de la derecha, localiza la sección **Salesbot**.
  3. Selecciona el bot que necesitas ejecutar (ej. `De solicitud a cotizado` o `Apoyo humano`).
  4. Haz clic en **Ejecutar**. El bot enviará los mensajes y reconfigurará el estatus de forma autónoma.
* **Regla para no romper los bots:**
  - Mientras estás hablando con el cliente, mantenlo en la etapa **Embudo Caliente** (los bots de seguimiento están apagados aquí).
  - Al terminar tu interacción y enviarle la propuesta, muévelo a la etapa de **Cotización** y presiona el botón de **Cotización realizada** para programar las alertas y bots de seguimiento correctamente.

### 3. ⏱️ Cómo Reabrir la Ventana de 24 horas de Meta (WhatsApp)
* **La restricción de Meta:** Por política de seguridad de WhatsApp, si transcurren más de 24 horas desde el último mensaje del cliente, no puedes enviarle mensajes libres (escribir texto ordinario). El sistema bloqueará tus mensajes.
* **Cómo restablecer el contacto:**
  1. Entra al chat del lead.
  2. Haz clic en el botón de **Plantillas de WhatsApp (HSM)**.
  3. Elige una de nuestras plantillas oficiales de reactivación aprobadas por Meta.
  4. Envía la plantilla. En cuanto el cliente responda con un texto o presionando un botón de la plantilla, la ventana de 24 horas se restablecerá y podrás volver a escribirle libremente.

### 4. 📅 Gestión de Tareas y Alertas (Regla de Oro)
* **Nuestra Regla de Oro:** *“Lead activo sin tarea es un lead perdido en el olvido.”* El sistema opera con base en compromisos en agenda.
* **Cómo crear tus recordatorios diarios:**
  1. En la parte inferior de la tarjeta del lead, haz clic en **Añadir tarea**.
  2. Elige el día y la hora de tu recordatorio (ej. Mañana a las 10:00 am).
  3. Escribe lo que debes realizar (ej. *'Confirmar horario de entrega de sanitarios'* o *'Verificar si Livier ya cotizó'*).
  4. Selecciona el tipo de tarea (`Llamada`, `Seguimiento`, `Reunión`).
  5. Guarda. Kommo te enviará notificaciones visuales y sonoras en el navegador y en tu celular.


### 🗂️ 5. El Trío Dinámico de Kommo: Tareas, Notas y Siguientes Pasos
Para organizar tu día de trabajo de forma profesional y garantizar que ningún lead se pierda, debes dominar estas tres herramientas:

#### 📅 A. Las Tareas (Tasks) — Tu Agenda Inteligente
* **¿Qué son?** Recordatorios con fecha, hora y responsable vinculados a un lead.
* **Cómo usarlas para tu beneficio:**
  - **Lista diaria ordenada:** Al iniciar tu jornada laboral, abre la sección de **Tareas** en Kommo. Verás tu lista de llamadas, seguimientos o correos programados para hoy, listados cronológicamente.
  - **Libera espacio mental:** No guardes pendientes en la memoria ni en hojas sueltas. Agenda una tarea y deja que el CRM te alerte en el navegador o en la app móvil de Kommo.
  - **Alerta roja:** Las tareas que pasan de su hora límite sin completarse se pintan de rojo. Evita tener tareas vencidas (en rojo), ya que reflejan negligencia comercial en tus tableros.

#### ✍️ B. Las Notas (Notes) — El Historial Clínico de la Venta
* **¿Qué son?** Comentarios que agregas en el feed de la tarjeta del lead.
* **Qué debes escribir en las notas:**
  - Acuerdos especiales de precio, cotizaciones manuales o descuentos.
  - Especificidades técnicas o del sitio de entrega (ej. *'Jardín con acceso de solo 1 metro'* o *'Cableado bajo, el operador debe tener cuidado'*).
  - Datos de contacto alternos (ej. *'Contacto administrativo: Sra. Elena, tel: XXX'*).
  - Resúmenes rápidos de llamadas (ej. *'Hablé con él, está de viaje y regresa el lunes'*).
* **Cómo usarlas para tu beneficio:**
  - **Trabajo en equipo:** Si sales de vacaciones o estás indispuesto, cualquier compañero puede leer las notas de tus leads y darles seguimiento sin tener que llamar al cliente a repetir preguntas.
  - **Confianza comercial:** Al hablar con el cliente, puedes mencionar los detalles específicos guardados en tus notas. Esto demuestra un servicio al cliente sumamente atento y profesional.

#### 🔄 C. El "Siguiente" (Siguientes Pasos) — La Regla Operativa
* **¿Qué es?** El hábito inquebrantable de programar el próximo contacto antes de cerrar una tarjeta. Al marcar una tarea como "Completada", Kommo te preguntará automáticamente: *¿Cuál es el siguiente paso?*.
* **Cómo usarlo para tu beneficio:**
  - **Mantén el impulso:** Si llamaste al cliente y te dijo que lo evalúa en tres días, programa tu siguiente tarea para esa fecha. Si acabas de cotizar, agenda tu siguiente paso para el día siguiente.
  - **Evita la inactividad:** Al asegurar que todo lead activo tiene siempre una tarea futura, garantizas que sigan avanzando por las etapas del embudo comercial hasta concretarse como **Ganados**.
