# Proyecto Base – u1_playground

Este proyecto corresponde al **entorno de práctica inicial** para comprender cómo funciona un proyecto en Django y montar sobre él diferentes ejemplos prácticos.  
Es el punto de partida para experimentar con el patrón MVT, vistas, enrutamiento y templates.

---

## 🎯 Objetivos
- Instalar y configurar **Django** en un entorno virtual.  
- Comprender la **estructura de carpetas y archivos** de un proyecto Django.  
- Reemplazar la página por defecto por un **“Hola Mundo desde Django”**.  
- Activar y probar de forma modular las distintas **apps de ejemplo** incluidas.  

---

## 📂 Estructura del Proyecto

u1_playground/
│
├── manage.py                # Script de gestión (servidor, apps, migraciones)
│
├── u1_playground/           # Configuración global del proyecto
│   ├── init.py
│   ├── asgi.py              # Configuración para servidores ASGI
│   ├── settings.py          # Configuración principal
│   ├── urls.py              # Enrutador raíz del proyecto
│   └── wsgi.py              # Configuración para servidores WSGI
│
└── ejemplos/                # Apps de práctica (e01–e09)
├── e01_idioma_timezone/
├── e02_saludo_param/
├── e03_httpresponse_html/
├── e04_template_basico/
├── e05_template_context/
├── e06_urls_por_app_include/
├── e07_base_template_herencia/
├── e08_listas_condicionales_dtl/
└── e09_redireccion_basica/

---

## ⚙️ Archivos Clave

### `manage.py`
Script para interactuar con el proyecto. Ejemplos:
- `python manage.py runserver` → servidor de desarrollo.  
- `python manage.py startapp nombreApp` → crear nueva app.  

### `settings.py`
Archivo central de configuración:
- **INSTALLED_APPS** → registra apps de Django y del proyecto.  
- **MIDDLEWARE** → capas de seguridad y procesamiento.  
- **TEMPLATES** → configuración de vistas HTML.  
- **DATABASES** → base de datos (SQLite por defecto).  
- **LANGUAGE_CODE / TIME_ZONE** → idioma y zona horaria.  

### `urls.py`
Define las rutas disponibles en el proyecto. Aquí se incluyen las URLs de cada app de ejemplo:  
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e01_idioma_timezone.urls')),  # activar un ejemplo a la vez
]

▶️ Cómo ejecutar
	1.	Crear y activar entorno virtual, instalar Django:

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\\Scripts\\activate    # Windows
pip install "Django>=5.0,<6.0"

	2.	Arrancar servidor:

python manage.py runserver

3.	En u1_playground/urls.py activar la app que quieras probar con include().
	4.	Navegar a: http://127.0.0.1:8000/ para ver el resultado.

⸻

🧪 Apps disponibles
	•	e01_idioma_timezone → Configuración de idioma y zona horaria.
	•	e02_saludo_param → Rutas dinámicas con parámetros.
	•	e03_httpresponse_html → Respuestas HTML directas con HttpResponse.
	•	e04_template_basico → Uso de render() y templates básicos.
	•	e05_template_context → Pasar variables a templates.
	•	e06_urls_por_app_include → Enrutamiento modular con include().
	•	e07_base_template_herencia → Herencia de templates (extends, block).
	•	e08_listas_condicionales_dtl → Bucles y condicionales en DTL.
	•	e09_redireccion_basica → Uso de redirect().

⸻

📖 Referencias
	•	Django Software Foundation. (2025). Django documentation. https://docs.djangoproject.com/
	•	Fowler, M. (2002). Patterns of Enterprise Application Architecture. Addison-Wesley.
	•	Vincent, W. (2024). Django for Beginners / APIs. Packt.

⸻

Contexto

Este proyecto está diseñado como un curso introductorio para comprender los fundamentos de Django.
Su fin es aprender el esqueleto del framework y familiarizarse con las piezas que se usarán en proyectos de mayor complejidad.
