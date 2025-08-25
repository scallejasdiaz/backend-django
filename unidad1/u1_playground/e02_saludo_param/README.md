# e02_saludo_param
**Objetivo:** demostrar rutas dinámicas con captura de parámetros.

## Pasos
1) `INSTALLED_APPS += ['e02_saludo_param']`
2) `u1_playground/urls.py` → `path('', include('e02_saludo_param.urls')),`
3) Navega a: `/saludo/Sebastian/`

## Variantes
- Cambia `<str:nombre>` por `<path:nombre>` y prueba con espacios o slashes.
- Añade una ruta con `<int:id>/`.

## Preguntas
- ¿Cómo validarías el parámetro antes de usarlo en la vista?