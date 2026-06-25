# 🚀 Guía de Despliegue en la Nube: Módulo de Capacitación Saniglobal

Para que cualquier persona de tu equipo pueda entrar a la capacitación interactiva desde cualquier lugar y dispositivo sin necesidad de correrla en local, la mejor opción (gratuita y oficial) es usar **Streamlit Community Cloud** conectado a un repositorio de **GitHub**.

Aquí tienes los pasos exactos para subir el proyecto a la nube:

---

## Paso 1: Inicializar Git y subir a GitHub

Necesitas tener una cuenta en [GitHub](https://github.com/). Si no tienes una, crea una rápido (es gratis).

1. Abre tu terminal de PowerShell en tu carpeta del proyecto:
   `c:\Users\DANIELHERRERA\OneDrive - SAN MEX DE JALISCO SA DE CV\Escritorio\Reglas de negocio`

2. Corre los siguientes comandos para iniciar tu repositorio y subir los archivos a GitHub (crea un repositorio vacío en GitHub llamado `saniglobal-capacitacion` primero):

```bash
# Iniciar Git localmente
git init

# Agregar todos los archivos (el archivo .gitignore excluirá carpetas pesadas como .venv y archivos de Excel)
git add .

# Hacer tu primer guardado (commit)
git commit -m "Despliegue inicial de capacitación"

# Crear la rama principal
git branch -M main

# Conectar tu carpeta local con tu repositorio de GitHub (reemplaza con tu URL de GitHub)
git remote add origin https://github.com/TU_USUARIO_DE_GITHUB/saniglobal-capacitacion.git

# Subir los archivos a la nube de GitHub
git push -u origin main
```

---

## Paso 2: Conectar con Streamlit Community Cloud

Una vez que tus archivos (`app.py`, `guia_data.py`, `requirements.txt` y `.gitignore`) estén en tu repositorio de GitHub:

1. Ve a la plataforma de **[Streamlit Community Cloud](https://share.streamlit.io/)**.
2. Dale clic a **"Sign in with GitHub"** (Inicia sesión con tu cuenta de GitHub).
3. Una vez dentro de tu panel de Streamlit, dale clic al botón **"Create app"** (o "Deploy an app" en la esquina superior derecha).
4. Configura los siguientes campos:
   - **Repository:** Selecciona tu repositorio `TU_USUARIO_DE_GITHUB/saniglobal-capacitacion`.
   - **Branch:** Escribe `main`.
   - **Main file path:** Escribe `app.py`.
   - **App URL:** (Opcional) Puedes personalizar el nombre de tu URL, por ejemplo: `saniglobal-capacitacion.streamlit.app`.
5. Dale clic al botón **"Deploy!"**.

---

## Paso 3: ¡Listo para compartir!

Streamlit tardará unos 2-3 minutos en preparar el entorno (instalará automáticamente todas las dependencias listadas en el `requirements.txt` que ya te generé).

- Una vez termine, tu aplicación estará en vivo bajo la URL que seleccionaste (ej. `https://saniglobal-capacitacion.streamlit.app`).
- El sistema cargará directamente la pantalla de acceso seguro solicitando la clave: **`Saniglobal2026@`** para proteger la información confidencial de tus embudos.

*Cualquier actualización que le hagas a tus archivos locales y subas a GitHub con un `git push` se actualizará en vivo en la nube de forma automática.*
