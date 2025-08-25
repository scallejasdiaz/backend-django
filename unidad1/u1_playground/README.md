# Proyecto Base: holaMundoDjango

Este proyecto corresponde al **ejemplo inicial de la Unidad I** de la asignatura **Programación Backend (TI2041)**.  
El objetivo es guiar a los estudiantes en la creación de un proyecto Django desde cero, comprendiendo la estructura de carpetas, los archivos principales y la configuración básica para desplegar una aplicación web mínima.

---

## 🎯 Objetivo del Proyecto
- Instalar y configurar **Django** en un entorno de desarrollo.  
- Comprender la estructura inicial de un proyecto creado con `django-admin startproject`.  
- Crear una primera aplicación (`firstApp`) y configurarla en `settings.py`.  
- Desarrollar una vista simple que despliegue en el navegador el mensaje:  
  **"Hola Mundo desde Django"**.  

Este proyecto busca cimentar la base para trabajos posteriores más complejos (manejo de templates, modelos y APIs).

---

## 📂 Estructura del Proyecto

Al ejecutar `django-admin startproject holaMundoDjango`, se genera la siguiente estructura de carpetas:

```
holaMundoDjango/
│
├── manage.py
│
├── holaMundoDjango/         # Carpeta raíz de configuración del proyecto
│   ├── __init__.py           # Inicializa el paquete
│   ├── asgi.py               # Configuración para servidores ASGI
│   ├── settings.py           # Configuración principal del proyecto
│   ├── urls.py               # Definición de rutas principales
│   └── wsgi.py               # Configuración para servidores WSGI
│
└── firstApp/                 # Aplicación creada con startapp
    ├── __init__.py
    ├── admin.py              # Configuración de administración
    ├── apps.py               # Configuración de la app
    ├── migrations/           # Carpeta para migraciones de BD
    ├── models.py             # Definición de modelos
    ├── tests.py              # Pruebas unitarias
    └── views.py              # Definición de vistas
```

---

## ⚙️ Archivos Clave

### `manage.py`
Script principal para interactuar con el proyecto. Ejemplos de uso:
- `python manage.py runserver` → levanta el servidor de desarrollo.
- `python manage.py startapp <nombre>` → crea una nueva aplicación.

### `settings.py`
Archivo central de configuración del proyecto:
- **INSTALLED_APPS** → se agregan las aplicaciones registradas (ej: `firstApp`).
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
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  # Página principal del proyecto
]
```

### `views.py` (en firstApp)
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
   python manage.py startapp firstApp
   ```

2. Agregar `firstApp` a **INSTALLED_APPS** en `settings.py`.

3. Definir vista `index` en `firstApp/views.py`.

4. Configurar la ruta en `holaMundoDjango/urls.py`.

5. Ejecutar servidor:
   ```bash
   python manage.py runserver
   ```

6. Abrir en navegador: `http://127.0.0.1:8000/`  
   Resultado esperado:  
   **Hola Mundo desde Django**

---

## 📖 Referencias
- Django Software Foundation. (2024). *Django Documentation*. Disponible en: https://docs.djangoproject.com/en/5.0/
- Mele, A. (2018). *Django 3 By Example*. Packt Publishing.
- Ravindran, A. (2018). *Django Design Patterns and Best Practices*. Packt Publishing.

---

## 👨‍🏫 Contexto Académico
Este proyecto forma parte de la **Unidad I: Tecnologías del Lado del Servidor** en la carrera **Ingeniería en Informática – INACAP**.  
Sirve como primer paso en el aprendizaje de frameworks backend y será la base para ejercicios y evaluaciones posteriores en la asignatura.

