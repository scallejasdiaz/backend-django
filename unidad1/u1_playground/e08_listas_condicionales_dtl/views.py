from django.shortcuts import render

def cursos(request):
    lista = ["Python", "Django", "Bases de Datos"]
    return render(request, "cursos.html", {"cursos": lista})