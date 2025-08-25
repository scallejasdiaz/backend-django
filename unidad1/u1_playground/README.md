# Proyecto Base – u1_playground

Este proyecto corresponde al entorno de práctica inicial para comprender cómo funciona un proyecto en Django y montar sobre él diferentes ejemplos prácticos.

---

## 🎯 Objetivo del Proyecto
- Instalar y configurar **Django** en un entorno de desarrollo.  
- Comprender la estructura inicial de un proyecto creado con `django-admin startproject`.  
- Configurar el proyecto para desplegar una aplicación web mínima con un mensaje de saludo.  

Este proyecto busca cimentar la base para trabajos posteriores más complejos (manejo de templates, modelos y APIs).

---

## 📂 Estructura del Proyecto

Al ejecutar `django-admin startproject holaMundoDjango`, se genera la siguiente estructura de carpetas:

```
holaMundoDjango/
│
├── manage.py
│
└── holaMundoDjango/         # Carpeta raíz de configuración del proyecto
    ├── __init__.py           # Inicializa el paquete
    ├── asgi.py               # Configuración para servidores ASGI
    ├── settings.py           # Configuración principal del proyecto
    ├── urls.py               # Definición de rutas principales
    └── wsgi.py               # Configuración para servidores WSGI
```

---

## ⚙️ Archivos Clave

### `manage.py`
Script principal para interactuar con el proyecto. Ejemplos de uso:
- `python manage.py runserver` → levanta el servidor de desarrollo.
- `python manage.py startapp <nombre>` → crea una nueva aplicación.

### `settings.py`
Archivo central de configuración del proyecto:
- **INSTALLED_APPS** → se agregan las aplicaciones registradas.
- **MIDDLEWARE** → capas intermedias de procesamiento de requests/responses.
- **TEMPLATES** → configuración de los directorios donde estarán los HTML.
- **DATABASES** → configuración de la base de datos (por defecto SQLite).
- **STATIC_URL** → define la ruta de archivos estáticos (CSS, JS, imágenes).

### `urls.py`
Define las rutas (URLs) que estarán disponibles en el proyecto.  
Ejemplo inicial:
```python
from django.contrib import admin
from django.urls import path
# Aquí se pueden incluir las vistas de las apps creadas en el proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='home'),  # Página principal del proyecto
]
```

### `views.py`
Archivo donde se definen las funciones o clases que responden a cada ruta:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo desde Django")
```

---

## ▶️ Pasos para ejecutar

1. Crear proyecto base:
   ```bash
   django-admin startproject holaMundoDjango
   cd holaMundoDjango
   ```
2. Definir vista `index` en la app correspondiente.

3. Configurar la ruta en `holaMundoDjango/urls.py`.

4. Ejecutar servidor:
   ```bash
   python manage.py runserver
   ```

5. Abrir en navegador: `http://127.0.0.1:8000/`  
   Resultado esperado:  
   **Hola Mundo desde Django**

---

## 📖 Referencias
- Django Software Foundation. (2024). *Django Documentation*. Disponible en: https://docs.djangoproject.com/en/5.0/
- Mele, A. (2018). *Django 3 By Example*. Packt Publishing.
- Ravindran, A. (2018). *Django Design Patterns and Best Practices*. Packt Publishing.

---
