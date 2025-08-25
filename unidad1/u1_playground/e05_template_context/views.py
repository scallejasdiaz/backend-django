from django.shortcuts import render

def perfil(request):
    data = {"usuario": {"nombre": "Ana", "edad": 22}}
    return render(request, "perfil.html", data)