# e03_httpresponse_html
**Objetivo:** ver una respuesta rápida sin templates (didáctico).

## Pasos
1) `INSTALLED_APPS += ['e03_httpresponse_html']`
2) `u1_playground/urls.py` → `path('', include('e03_httpresponse_html.urls')),`
3) Abre `/` y observa el HTML renderizado.

## Variantes
- Integra un pequeño fragmento de CSS inline para notar limitaciones.
- Devuelve un `HttpResponse` con `content_type="text/plain"` y compara.

## Preguntas
- ¿Por qué NO es buena práctica mantener HTML en la vista?