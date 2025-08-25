# e04_template_basico
**Objetivo:** usar `render()` y cargar un template.

## Pasos
1) `INSTALLED_APPS += ['e04_template_basico']`
2) `u1_playground/urls.py` → `path('', include('e04_template_basico.urls')),`
3) Abre `/` y verifica el template.

## Variantes
- Cambia el nombre `home.html` y provoca un `TemplateDoesNotExist` adrede.
- Agrega una carpeta `templates/pages/` y ajusta la ruta en `render()`.

## Preguntas
- ¿Qué busca Django cuando `APP_DIRS=True`?