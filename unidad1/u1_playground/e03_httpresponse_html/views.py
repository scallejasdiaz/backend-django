from django.http import HttpResponse

def about(request):
    return HttpResponse("""
        <h1>Acerca de</h1>
        <p>Este sitio está construido con Django.</p>
        <small>Nota: En producción, usa templates. Esto es sólo demostrativo.</small>
    """)