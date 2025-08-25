# Backend con Django – Ejemplos Prácticos

Este repositorio ofrece una colección de ejemplos prácticos y progresivos desarrollados en **Django**, diseñados para cualquier persona interesada en aprender y mejorar sus habilidades en desarrollo backend.  
El objetivo es proporcionar una base sólida en el uso de **frameworks backend modernos**, con énfasis en **buenas prácticas, seguridad y escalabilidad**.

---

## 🎯 Objetivos del Repositorio
- Explorar los fundamentos del desarrollo **backend con Django**.
- Aplicar el patrón **MVT (Model-View-Template)** en proyectos reales.
- Practicar con ejemplos que van **desde lo básico hasta lo avanzado**.
- Facilitar el aprendizaje a través de ejemplos prácticos y claros.
- Contar con un repositorio de referencia para proyectos personales y profesionales.

---

## 📂 Estructura del Repositorio

```
backend-django/
│
├── unidad1/                     # Unidad I – Introducción y Fundamentos
│   ├── u1_playground/           # Proyecto base (holaMundoDjango)
│   └── ejemplos/                # Apps prácticas e01–e09
│
├── unidad2/                     # Unidad II – Models y Forms
│   └── (en construcción)
│
├── unidad3/                     # Unidad III – API RESTful con DRF
│   └── (en construcción)
│
└── evaluaciones/                # Ejemplos adicionales y pruebas
    └── (en construcción)
```

---

## 🧭 Contenido de la Unidad I

- **Proyecto Base – holaMundoDjango**  
  - [README proyecto base](./unidad1/u1_playground/README_proyecto_base.md)  
  - Creación del proyecto y primera app (`firstApp`).  
  - Configuración de `settings.py` y `urls.py`.  
  - Vista básica con *Hola Mundo desde Django*.  

- **Ejemplos prácticos (e01–e09):**  
  - [e01_idioma_timezone](./unidad1/u1_playground/e01_idioma_timezone/) → Idioma y zona horaria en `settings.py`  
  - [e02_saludo_param](./unidad1/u1_playground/e02_saludo_param/) → Rutas dinámicas con parámetros  
  - [e03_httpresponse_html](./unidad1/u1_playground/e03_httpresponse_html/) → `HttpResponse` con HTML básico  
  - [e04_template_basico](./unidad1/u1_playground/e04_template_basico/) → Template mínimo con `render()`  
  - [e05_template_context](./unidad1/u1_playground/e05_template_context/) → Contexto y variables en templates  
  - [e06_urls_por_app_include](./unidad1/u1_playground/e06_urls_por_app_include/) → Enrutamiento modular con `include()`  
  - [e07_base_template_herencia](./unidad1/u1_playground/e07_base_template_herencia/) → Herencia de templates (`extends` y `block`)  
  - [e08_listas_condicionales_dtl](./unidad1/u1_playground/e08_listas_condicionales_dtl/) → Listas y condicionales en DTL  
  - [e09_redireccion_basica](./unidad1/u1_playground/e09_redireccion_basica/) → Redirecciones con `redirect()`  

Cada ejemplo incluye su propio `README.md` con explicaciones detalladas.

---

## 🚀 Cómo usar los ejemplos

1. Clonar este repositorio:
   ```bash
   git clone git@github.com:scallejasdiaz/backend-django.git
   cd backend-django/unidad1/u1_playground
   ```

2. Crear entorno virtual e instalar Django:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows

   pip install "Django>=5.0,<6.0"
   ```

3. Activar una app de ejemplo:  
   - Agregar la app en `INSTALLED_APPS` de `settings.py`.  
   - Incluir su `urls.py` en `u1_playground/urls.py`.  

4. Levantar servidor:
   ```bash
   python manage.py runserver
   ```

5. Navegar a `http://127.0.0.1:8000/` para probar.

---

## 📖 Referencias Bibliográficas

- Django Software Foundation. (2025). *Django documentation*. https://docs.djangoproject.com/  
- Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison‑Wesley.  
- Vincent, W. (2024). *Django for Beginners / APIs*.  
- Jamro, A. (2022). *Django 4 By Example*. Packt Publishing.  

---
