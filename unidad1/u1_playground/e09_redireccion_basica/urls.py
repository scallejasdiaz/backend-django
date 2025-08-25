from django.urls import path
from .views import raiz, bienvenida

urlpatterns = [
    path('', raiz, name='raiz'),
    path('bienvenida/', bienvenida, name='bienvenida'),
]