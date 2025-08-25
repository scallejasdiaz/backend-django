from django.http import HttpResponse

def saludo(request, nombre):
    return HttpResponse(f"Hola {nombre}, ¡bienvenido a Django!")