from django.shortcuts import redirect
from django.http import HttpResponse

def raiz(request):
    return redirect('bienvenida')

def bienvenida(request):
    return HttpResponse("Bienvenido/a. Esta vista fue alcanzada por redirección.")