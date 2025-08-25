from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Inicio de la app e06")

def acerca(request):
    return HttpResponse("Página acerca de e06")