from django.urls import path
from .views import ahora

urlpatterns = [ path('', ahora, name='ahora') ]