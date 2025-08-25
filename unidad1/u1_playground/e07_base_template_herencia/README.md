# e07_base_template_herencia
**Objetivo:** aplicar herencia de templates con `{% extends %}` y `{% block %}`.

## Pasos
1) `INSTALLED_APPS += ['e07_base_template_herencia']`
2) En `u1_playground/urls.py`:
   ```python
   path('', include('e07_base_template_herencia.urls')),