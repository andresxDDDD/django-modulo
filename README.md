# 🚀 Proyecto Django 6.2 - Guía de Instalación

Este documento describe paso a paso cómo configurar el entorno de desarrollo e iniciar un proyecto utilizando **Django 6.2**.

---

## 📌 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.10 o superior**
- **pip** (gestor de paquetes de Python)

Puedes verificarlo con:

```bash
python --version
pip --version
```
🧱 2. Entorno Virtual (venv)

El entorno virtual permite aislar las dependencias del proyecto.

❓ ¿Por qué usarlo?

Evita conflictos entre versiones de librerías.
Ejemplo: puedes tener un proyecto con Django 5 y otro con Django 6 sin problemas.

⚙️ Crear entorno virtual
python -m venv venv
▶️ Activar entorno virtual
Windows
.\venv\Scripts\activate
Linux / macOS
source venv/bin/activate
📦 3. Archivo de Dependencias

Crea un archivo llamado:

requirements.txt
📄 Contenido recomendado:
# Framework Principal
Django==6.2

# Manejo de variables de entorno
python-decouple==3.8

# Base de datos PostgreSQL
psycopg2-binary==2.9.9

# Herramientas de desarrollo
django-extensions==3.2.3

# Servidor para producción
gunicorn==21.2.0
📚 4. Explicación de Dependencias
Django → Framework web principal
python-decouple → Manejo seguro de variables sensibles (.env)
psycopg2-binary → Conector para PostgreSQL
django-extensions → Herramientas extra para desarrollo
gunicorn → Servidor para despliegue en producción
⚙️ 5. Instalación del Proyecto

Con el entorno virtual activado:

pip install --upgrade pip
pip install -r requirements.txt
🏗️ 6. Crear Proyecto Django
django-admin startproject core .

⚠️ El punto . evita crear una carpeta adicional innecesaria.

🗄️ 7. Migraciones Iniciales

Django incluye un sistema de autenticación que necesita tablas:

python manage.py migrate
▶️ 8. Ejecutar Servidor
python manage.py runserver

Accede en tu navegador a:

http://127.0.0.1:8000/
📁 9. Estructura del Proyecto
Archivo / Carpeta	Descripción
venv/	Entorno virtual aislado
requirements.txt	Lista de dependencias
manage.py	CLI de Django
core/settings.py	Configuración principal
core/urls.py	Enrutamiento de URLs
✅ Resumen
Crear entorno virtual
Activarlo
Crear requirements.txt
Instalar dependencias
Crear proyecto Django
Ejecutar migraciones
Levantar servidor
💡 Recomendaciones
Usa un archivo .env para credenciales sensibles
No subas venv/ al repositorio (.gitignore)
Usa PostgreSQL en producción
Mantén tus dependencias versionadas