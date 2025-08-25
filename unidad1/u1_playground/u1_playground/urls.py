"""
URL configuration for u1_playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', include('e01_idioma_timezone.urls')),
    #path('', include('e02_saludo_param.urls')),
    #path('', include('e03_httpresponse_html.urls')),
    #path('', include('e04_template_basico.urls')),
    #path('', include('e05_template_context.urls')),
    #path('', include('e06_urls_por_app_include.urls')),
    #path('', include('e07_base_template_herencia.urls')),
    #path('', include('e08_listas_condicionales_dtl.urls')),
    path('', include('e09_redireccion_basica.urls')),
]

