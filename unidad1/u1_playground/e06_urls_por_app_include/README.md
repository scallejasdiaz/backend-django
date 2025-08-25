# e06_urls_por_app_include
**Objetivo:** separar las rutas de cada app y centralizar en `urls.py` del proyecto con `include()`.

## Pasos
1) `INSTALLED_APPS += ['e06_urls_por_app_include']`
2) En `u1_playground/urls.py`:
   ```python
   path('', include('e06_urls_por_app_include.urls')),