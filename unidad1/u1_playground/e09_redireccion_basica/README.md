# e09_redireccion_basica
**Objetivo:** mostrar el uso de `redirect()` para mover al usuario a otra ruta.

## Pasos
1) `INSTALLED_APPS += ['e09_redireccion_basica']`
2) En `u1_playground/urls.py`:
   ```python
   path('', include('e09_redireccion_basica.urls')),