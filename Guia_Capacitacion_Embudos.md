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
4. [Embudos de Soporte (Quejas y Otros Asuntos)](#embudos-soporte)

### 🚽 SECCIÓN II: RENTA DE BAÑOS PORTÁTILES
* **Vendedor Responsable:** Daniel Herrera
* [Flujo y etapas del Embudo de Ventas (Baños)](#seccion-baños)
* [Secuencia de preguntas del Bot de Renta](#preguntas-baños)
* [Gestión de Clientes Activos (Ganados y Retiros)](#clientes-activos-baños)

### 🌀 SECCIÓN III: SERVICIOS ESPECIALES Y FOSAS SÉPTICAS
* **Vendedora Responsable:** Livier Mora
* [Flujo y etapas del Embudo de Fosas y Especiales](#seccion-fosas)
* [Secuencia de preguntas del Bot de Fosas](#preguntas-fosas)
* [Filtro crítico de Casa Habitación (Exclusión)](#filtro-fosas)
* [Visita de Diagnóstico y Seguimiento](#seguimiento-fosas)

### 🍳 SECCIÓN IV: TRAMPAS DE GRASA
* **Vendedor Responsable:** Asesor de Trampas de Grasa
* [Flujo y etapas del Embudo de Trampas](#seccion-trampas)
* [Secuencia de preguntas del Bot de Trampas](#preguntas-trampas)
* [Cotización Automática vs. Cotización Manual](#cotizacion-trampas)

---

<a name="glosario"></a>
## ⚙️ PARTE I: BASES GENERALES (Para todo el equipo)

### 1. 📖 Glosario Rápido

Antes de entrar de lleno, aquí están los términos que usamos constantemente:

| Término | Qué significa |
|---|---|
| **Lead / Prospecto** | Cualquier persona que nos escribe por primera vez |
| **Embudo (Pipeline)** | El "camino" o proceso de ventas con etapas definidas |
| **Etapa (Estatus)** | La fase específica en la que está el lead dentro del embudo |
| **Bot / Automatización** | Mensajes y acciones que el sistema ejecuta solo, sin que intervengas |
| **Etiqueta (Tag)** | Marca de color que le ponemos al contacto para clasificarlo |
| **Webhook** | Conexión automática con otro sistema (ej. cotizador automático) |
| **Ventana de 24h** | El tiempo que Meta te da para responder libremente por WhatsApp |
| **Mensaje rápido** | Plantilla de texto guardada para no escribir lo mismo cada vez |
| **Casa Habitación** | Tag y filtro para prospectos residenciales que no atendemos y se mandan a Cerrado |

---

<a name="gpt-completo"></a>
### 2. 🌟 El Embudo GPT Completo — El Origen de Todo

Cuando alguien nos escribe por primera vez —sea por WhatsApp, Facebook o Instagram— su conversación aterriza automáticamente aquí. Este bot es el **recepcionista virtual de la empresa**. Se llama "GPT Completo" porque usa inteligencia artificial para entender lo que el cliente escribe y guiarlo por el camino correcto.

**Lo primero que hace el bot** es presentarse y preguntar:

> *"Mucho gusto, ¿en qué te podemos servir hoy? ¿Te interesa rentar un baño portátil o buscas algún servicio especializado como limpieza de fosas sépticas, trampas de grasa, recolección de residuos?"*

El cliente tiene tres botones para elegir:
- 🚽 **Rentar baños** → El bot lo mueve al **Embudo de Ventas (Baños)** y lo asigna a Daniel Herrera.
- 🔧 **Servicios especiales** → El bot lo mueve al **Embudo de Servicios Especiales** y lo asigna a Livier Mora.
- 💬 **Otro asunto** → El bot lo mueve al **Embudo de Otros Asuntos**.

> [!NOTE]
> Si el cliente escribe en lugar de usar un botón (ej. "renta de sanitarios" o "trampa de grasa"), el sistema intenta detectarlo y enviarlo al embudo correcto automáticamente. Si no puede clasificarlo, lo pasa a soporte humano.

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
Muchos bots de seguimiento no se activarán a menos que le des clic al botón manual correspondiente dentro de la tarjeta del lead (ej. "Cotización realizada", "Baño entregado"). **Si no das clic, el cliente se queda congelado sin automatizaciones.**

#### ⚡ Mensajes Rápidos
Escribe `/` (diagonal) en el chat para buscar plantillas predefinidas. Úsalas para saludos, cuentas de pago o preguntas frecuentes y mantén la consistencia profesional del equipo.

---

<a name="embudos-soporte"></a>
### 4. 😤 Embudos de Soporte: Quejas y Otros Asuntos

#### Embudo de Quejas (Pipeline 12717196)
* **¿Cuándo llega?** Cuando un cliente selecciona "Reportes y quejas" en el menú o lo solicita a un asesor.
* **Acción:** El sistema le pone la etiqueta **"Quejas"** y lo mueve aquí para atención humana inmediata.

#### Embudo de Otros Asuntos (Pipeline 13756408)
* **¿Cuándo llega?** Cuando eligen "Otro asunto" en el menú principal.
* **Funcionamiento:** El bot filtra si es:
  - *Empleo:* Da datos de RH y pone la etiqueta **"Vacante laboral"**.
  - *Proveedores:* Da datos de compras y pone la etiqueta **"Proveedores"**.
  - *Otros:* Crea tarea de soporte humano.
* **Cierre:** Al no ser prospectos comerciales, se mueven a la etapa **Cerrado**.

---

<a name="seccion-baños"></a>
## 🚽 SECCIÓN II: RENTA DE BAÑOS PORTÁTILES
### Asesor Responsable: Daniel Herrera (Usuario 12824423)

#### Vista general del Embudo de Ventas (Baños)
```
Solicitud → Embudo caliente → Solicitud de información → Cotización → En seguimiento 
→ Programado → Baño entregado → [Ganados] 
                               ↘ [Pausado]
                               ↘ [Perdido reactivable] → [Perdidos]
```

---

### Etapa por Etapa: Renta de Baños

#### 📥 Etapa: Solicitud de Cotización
* **¿Cómo llega?** El cliente elige "Rentar baños" en el menú inicial. El bot lo asigna a Daniel Herrera.
* **Automatización:** El bot recopila los datos para cotizar:
  1. *¿Obra o Evento?* (Recomienda cantidad según tipo y personas).
  2. *¿Cuántos baños?* (Si pide 3 o más, se pasa a Daniel para atención manual).
  3. *¿Tipo de baño?* (Sencillo vs. Con Lavamanos. Muestra fotos de comparación).
  4. *¿Por cuánto tiempo?* (Por mes/quincena en obra, por día/semana en eventos).
  5. *¿Dirección de entrega?* (Valida que sea texto y no un pin de ubicación. Debe estar en ZM Guadalajara o ZM San Luis Potosí).

#### 🌡️ Etapa: Embudo Caliente
* **¿Qué significa?** El cliente está respondiendo activamente al chat.
* **Regla de oro:** **No se disparan mensajes automáticos** en esta etapa para evitar interrumpir o confundir al cliente mientras chatea con el asesor.

#### ℹ️ Etapa: Solicitud de Información
* Etapa temporal donde el bot procesa y valida datos de dirección antes de activar la cotización automática.

#### 💰 Etapa: Cotización
* **Ruta Automática:** Si el bot recopiló todos los datos, calcula el precio, envía la propuesta en PDF y mueve el lead a esta etapa.
* **Ruta Manual:** Si Daniel Herrera envía la propuesta manualmente (ej. cuando son 3 o más baños), **es obligatorio dar clic en el botón "Cotización realizada"** en la tarjeta del lead.
* **Qué hace el bot aquí:** Pone la etiqueta **"Propuesta enviada"** y ofrece botones de ayuda rápida (*Pasos para contratar*, *Formas de pago*, *Tiempos de entrega*).
* **Descuento del 5%:** Si el cliente no responde tras **2 horas** de recibir la cotización, el bot le ofrece un 5% de descuento por WhatsApp y le añade la etiqueta **"-5% descuento"**.

#### 📞 Etapa: En Seguimiento
* **¿Cómo llega?** Pasan **21 horas** sin respuesta tras enviar la cotización. El sistema lo mueve aquí y manda un mensaje de seguimiento preguntando el estado de su decisión.
* *Botones de respuesta del cliente:*
  - *"Deseo rentar ya"* → Pasa al asesor Daniel Herrera.
  - *"Evaluando opciones" / "En pausa"* → El bot le pregunta cuándo recontactar (mañana, 3 días, 1 semana).
  - *"Ya no lo requiero"* → El bot pregunta el motivo. Si es *Precio*, le ofrece argumentos de valor, un cupón del **10% de descuento** y le pone la etiqueta **"Perdido por precio"**. Si son otros motivos, pone la etiqueta correspondiente (*Falta de espacio en programación*, *No fue necesario el servicio*).

#### 📅 Etapa: Programado
* El servicio ha sido aceptado y programado en agenda, pero el baño aún no se entrega físicamente.

#### 🚪 Etapa: Baño Entregado (Ganado - Baños)
* Cuando el equipo de operaciones entrega el baño, Daniel o el equipo de logística debe **dar clic al botón "Baño entregado"**.
* **Acción del bot:** Dispara la encuesta post-servicio ("Recopila opiniones con emojis") y prepara la reactivación futura.

---

<a name="clientes-activos-baños"></a>
### 📋 Gestión y Reactivación de Clientes Ganados (Tengan o no Baño Activo)

> [!IMPORTANT]
> **Regla de oro sobre los clientes Ganados:**
> 1. **Asegurar el estatus:** Siempre debes verificar que cuando una venta se concrete, el lead quede marcado en la etapa **Ganados** (ya sea que lo mueva el vendedor manualmente o que ocurra por una automatización del sistema). Si no está en Ganados, el flujo se rompe.
> 2. **El disparador por mensaje:** Una vez en **Ganados**, el lead entra en una "pausa" de espera. En el momento en que ese cliente vuelve a escribirnos (incluso tiempo después), el sistema detecta que es un cliente ganado y **automáticamente lo mueve al embudo "Ganados el cliente reactiva"** (etapa: *Cliente Actual*). **Esto ocurre tenga o no tenga un baño activo en su sitio en ese momento.**
> 3. **¿Por qué funciona así?:** Esta transición automática al embudo de reactivación es lo que permite que se le dispare el menú de opciones (Bot GPT ganados / reactiva) para que el cliente pueda autogestionarse (solicitar retiros, quejas, rentar otro baño, consultar pagos, etc.) sin que tengas que intervenir de inmediato.

#### Menú de Cliente Actual ("Ganados el cliente reactiva")
Cuando un cliente ganado nos vuelve a escribir (tenga o no un baño físicamente en sitio), el bot le presenta un menú interactivo:
- **Retirar o reubicar:** Si elige *Retirar*, le da instrucciones de enviar un correo a operaciones. Cuando el cliente confirma el envío, se le dispara la **encuesta de emojis** y al finalizar se le regala un **cupón del 10% de descuento** para reactivación. Si dice que no quiere retirar, se le ofrece ampliar la renta.
- **Quiero otro baño:** Lanza el **Bot GPT Ganados** (un flujo rápido de cotización que crea la tarea "Cotizar nuevo baño" asignada a Daniel).
- **Reportes y quejas:** Mueve el lead al *Embudo de Quejas* con etiqueta **"Quejas"**.
- **Manifiestos y pagos:** Da los contactos de Michelle (Manifiestos) o Leslie Arellano (Crédito y Cobranza) según elija.

---

<a name="seccion-fosas"></a>
## 🌀 SECCIÓN III: SERVICIOS ESPECIALES Y FOSAS SÉPTICAS
### Asesora Responsable: Livier Mora (Usuario 13346199)

#### Vista general del Embudo de Fosas y Especiales
```
Solicitud → Visita de diagnóstico → Cotización → En seguimiento 
→ [Ganados] 
→ [Pausado] (Servicio para > 1 mes)
→ [Perdido reactivable] (Perdido por precio o agenda) → [Perdidos]
→ [Cerrado] (No califica / Casa Habitación)
```

---

### Etapa por Etapa: Fosas Sépticas y Lodos

#### 📥 Etapa: Solicitud de Cotización (Servicios Especiales)
* **¿Cómo llega?** El cliente elige "Servicios especiales" en el menú inicial y selecciona una categoría aplicable (como fosas sépticas, lodos, vinazas, etc.). El sistema lo asigna a Livier Mora.
* **Preguntas del Bot para Calificación:**
  1. *¿Qué residuo es?* (Fosas sépticas, lodo biológico, aguas de proceso, vinazas, etc. Se envía PDF de presentación comercial de Saniglobal).
  2. *¿Estado del material?* (Líquido, Lodo o pasta, Sólido o polvo).
  3. *¿Dónde está almacenado?* (Fosa/cisterna, Tambo/tolva/sacos, Sobre terreno).
  4. *¿Volumen o cantidad?* (Menos de 5,000 lt/kg, 5,000 a 10,000, Más de 10,000).

---

<a name="filtro-fosas"></a>
### 🏠 Filtro Crítico: Casa Habitación o Domicilio Particular

> [!CAUTION]
> **REGLA DE NEGOCIO:** Saniglobal **no realiza servicios residenciales o para casas particulares** en limpieza de fosas sépticas ni desazolve. Este servicio está enfocado exclusivamente al sector comercial e industrial.

#### ¿Cómo actúa el Bot ante esto?
Después de preguntar por el volumen en fosas sépticas, el bot pregunta:
> *¿Es para una casa habitacional o residencial?*

* **Si el cliente responde "Sí":**
  1. El bot le coloca automáticamente la etiqueta **`CASA HABITACIÓN`**.
  2. Le envía el mensaje de rechazo cortés: *"Una disculpa, por el momento no estamos brindando servicios para casa habitación ni domicilios particulares, sin embargo, esperamos poderlo reactivar en la brevedad. Déjanos tus datos..."*
  3. Mueve el lead automáticamente a la etapa **Cerrado**.
* **Si el cliente responde "No":**
  1. El bot continúa con la cotización preguntando por la distancia de manguera (distancia del camión al residuo: 0-10m, 11-20m, 21m+).

---

<a name="seguimiento-fosas"></a>
### Visita de Diagnóstico, Cotización y Seguimiento

#### 🔎 Visita de Diagnóstico
* En proyectos complejos de fosas, antes de cotizar se requiere una visita física. Livier programa la visita y el lead se mantiene en esta etapa intermedia.

#### 💰 Etapa: Cotización (Fosas)
* Como las fosas requieren cotizaciones detalladas y manuales, Livier elabora la propuesta. Al enviarla al cliente, **debe presionar el botón "Cotización realizada"** en Kommo para activar el seguimiento automático.

#### 📞 Etapa: En Seguimiento (Fosas)
* Pasan **21 horas** sin respuesta del cliente. El bot le envía un mensaje de seguimiento.
* Si el cliente indica que no contratará por *Precio*, el bot le da argumentos de valor y le ofrece un cupón de descuento del **5% de descuento** (a diferencia de baños, aquí el descuento máximo es del 5%).

---

<a name="seccion-trampas"></a>
## 🍳 SECCIÓN IV: TRAMPAS DE GRASA
### Asesor Responsable: Asesor de Trampas de Grasa

#### Vista general del Embudo de Trampas de Grasa
```
Solicitud → Cotización → En seguimiento 
→ [Ganados] 
→ [Pausado]
→ [Perdido reactivable] → [Perdidos]
```

---

<a name="preguntas-trampas"></a>
### Etapa por Etapa: Trampas de Grasa

#### 📥 Etapa: Solicitud de Cotización (Trampas)
* **¿Cómo llega?** El cliente elige "Servicios especiales" en el menú inicial y selecciona **Grasas alimenticias (trampas de grasa)**.
* **Preguntas de Calificación del Bot:**
  1. *¿Cuántas trampas de grasa?* (Solo 1, 2, o 3 o más. Si pide 3 o más, el bot lo turna al asesor para cotización manual).
  2. *¿Capacidad o tamaño promedio?* (200 LTS estándar, 250 a 500 LTS, Más de 500 LTS. Tamaños mayores a 200 LTS van a cotización manual).
  3. *¿De qué material son?* (Plástico/PVC, Acero inoxidable/Metal, Concreto/Obra civil).
  4. *¿Cómo es el acceso para la unidad?* (A pie de trampa, Acceso complicado, Requiere permisos).
  5. *¿Distancia del camión a la trampa?* (Corta 0-10m, Media 11-20m, Larga más de 21m).
  6. *¿Cuenta con rampas accesibles?* (Sí, No lo sé, No).
  7. *Fotos/Videos:* Solicita evidencia visual para verificar las condiciones físicas antes del servicio.

---

<a name="cotizacion-trampas"></a>
### 💰 Etapa: Cotización (Trampas)

#### 1. Cotización Automática
* Si el cliente solicita **1 o 2 trampas de 200 LTS (estándar)** y responde todas las preguntas del bot, el sistema procesa el webhook `https://trampas-de-grasa-microservicio.vercel.app/api/webhook`.
* El bot le envía al cliente un enlace personalizado generado en el campo `{{lead.cf.1117077}}` con la cotización lista y mueve el lead a *Cotización*.

#### 2. Cotización Manual
* Si el tamaño es mayor a 200 LTS, requiere permisos complejos o son más de 3 trampas, el bot pausa la automatización.
* El asesor debe formular la cotización manualmente. Al enviarla, **debe presionar obligatoriamente el botón "Cotización de trampas de grasa manual"** en Kommo para mover el lead al estatus de cotización.

#### 📞 Etapa: En Seguimiento (Trampas)
* A las **21 horas** de haber enviado la cotización, el bot pregunta el estatus de la decisión.
* Si el cliente rechaza por *Precio*, se le ofrece un cupón del **5% de descuento** y se le etiqueta como **"Perdido por precio"**.

---

## 📌 Tabla Resumen de Reglas y Cupones de Descuento

| Embudo | Descuento Inicial (Sin respuesta) | Cupón en Seguimiento (Objeción de Precio) | Disparador de Seguimiento |
|---|---|---|---|
| **Baños (Daniel Herrera)** | **5%** (a las 2 horas sin respuesta) | **10%** (en seguimiento de 21h) | Botón manual "Cotización realizada" / Webhook automático |
| **Fosas (Livier Mora)** | N/A (Cotización siempre manual) | **5%** (en seguimiento de 21h) | Botón manual "Cotización realizada" |
| **Trampas (Asesor Trampas)** | N/A | **5%** (en seguimiento de 21h) | Botón manual "Cotización de trampas de grasa manual" |
