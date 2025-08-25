# Backend con Django – Ejemplos Académicos

Este repositorio contiene el material práctico de la asignatura **Programación Backend (TI2041)**, desarrollado en **Django**, para el apoyo de clases, ejercicios guiados y evaluaciones.  
El propósito es entregar a los estudiantes una base sólida en el uso de **frameworks backend modernos**, con foco en **buenas prácticas, seguridad y escalabilidad**.

---

## 🎯 Objetivos del Repositorio
- Comprender los fundamentos del desarrollo **backend con Django**.
- Aplicar el patrón **MVT (Model-View-Template)** en proyectos reales.
- Practicar de forma progresiva con ejemplos **desde lo básico hasta lo avanzado**.
- Integrar conceptos académicos con **ejercicios prácticos** en clase.
- Contar con un repositorio de referencia para proyectos y evaluaciones.

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
└── evaluaciones/                # Evaluaciones sumativas y formativas
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
  - [e01_idioma_timezone](./unidad1/ejemplos/e01_idioma_timezone/README.md) → Idioma y zona horaria en `settings.py`  
  - [e02_saludo_param](./unidad1/ejemplos/e02_saludo_param/README.md) → Rutas dinámicas con parámetros  
  - [e03_httpresponse_html](./unidad1/ejemplos/e03_httpresponse_html/README.md) → `HttpResponse` con HTML básico  
  - [e04_template_basico](./unidad1/ejemplos/e04_template_basico/README.md) → Template mínimo con `render()`  
  - [e05_template_context](./unidad1/ejemplos/e05_template_context/README.md) → Contexto y variables en templates  
  - [e06_urls_por_app_include](./unidad1/ejemplos/e06_urls_por_app_include/README.md) → Enrutamiento modular con `include()`  
  - [e07_base_template_herencia](./unidad1/ejemplos/e07_base_template_herencia/README.md) → Herencia de templates (`extends` y `block`)  
  - [e08_listas_condicionales_dtl](./unidad1/ejemplos/e08_listas_condicionales_dtl/README.md) → Listas y condicionales en DTL  
  - [e09_redireccion_basica](./unidad1/ejemplos/e09_redireccion_basica/README.md) → Redirecciones con `redirect()`  

Cada ejemplo cuenta con su propio `README.md` explicativo.

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
   .venv\Scripts\activate    # Windows

   pip install "Django>=5.0,<6.0"
   ```

3. Activar una app de ejemplo:  
   - Agregar la app en `INSTALLED_APPS` de `settings.py`.  
   - Incluir su `urls.py` en `u1_playground/urls.py`.  

4. Levantar servidor:
   ```bash
   python manage.py runserver
   ```

5. Navegar en `http://127.0.0.1:8000/` para probar.

---

## 📖 Referencias Bibliográficas

- Django Software Foundation. (2025). *Django documentation*. https://docs.djangoproject.com/  
- Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison‑Wesley.  
- Vincent, W. (2024). *Django for Beginners / APIs*.  
- Jamro, A. (2022). *Django 4 By Example*. Packt Publishing.  

---

## 👨‍🏫 Contexto Académico

Este repositorio es parte del material docente de la asignatura **Programación Backend** en la carrera **Ingeniería en Informática**.  
Busca no solo entregar código, sino también **formar criterio de ingeniería**, enfatizando en:  

- Seguridad de la configuración (`DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`).  
- Organización modular de proyectos.  
- Documentación y uso responsable de IA en la elaboración de tareas y evaluaciones.  

---

## 🧪 Uso responsable de IA

De acuerdo con la normativa vigente, el uso de **IA generativa** debe:  
- Ser declarado en cada entrega.  
- No superar el **50% del trabajo total**.  
- Complementarse siempre con defensa oral o demostración práctica.  

---

