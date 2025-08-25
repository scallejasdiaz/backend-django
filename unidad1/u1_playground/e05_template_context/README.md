# e05_template_context
**Objetivo:** pasar datos desde la vista al template.

## Pasos
1) `INSTALLED_APPS += ['e05_template_context']`
2) `u1_playground/urls.py` → `path('', include('e05_template_context.urls')),`
3) Abre `/` y valida las variables renderizadas.

## Variantes
- Cambia `usuario` por un diccionario vacío y usa `{% if usuario %}` en la plantilla.
- Pasa una lista y recórrela con `{% for %}`.

## Preguntas
- ¿Qué diferencia hay entre pasar `data` y usar contexto global vía `context_processors`?