from django.urls import path
from .views import saludo

urlpatterns = [ path('saludo/<str:nombre>/', saludo, name='saludo') ]