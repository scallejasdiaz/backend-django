# e01_idioma_timezone
**Objetivo:** mostrar el impacto de `LANGUAGE_CODE`, `TIME_ZONE`, `USE_TZ`.

## Pasos
1) Agrega a `INSTALLED_APPS`: `'e01_idioma_timezone'`.
2) En `u1_playground/urls.py`: `path('', include('e01_idioma_timezone.urls')),`
3) Ejecuta: `python manage.py runserver` y abre `http://127.0.0.1:8000/`.

## Qué observar
- Formato y zona de la fecha/hora dependen de `LANGUAGE_CODE`, `TIME_ZONE` y `USE_TZ`.

## Variantes
- Cambia `TIME_ZONE = 'UTC'` y compara.
- Desactiva temporalmente `USE_TZ` y observa diferencias.

## Preguntas
- ¿Por qué conviene activar `USE_TZ` en backend modernos?