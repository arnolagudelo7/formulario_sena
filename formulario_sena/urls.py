"""
URL configuration for formulario_sena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from formulario_sena.views import Index,Registro,LugarEventoCrear,VerLugar,ActualizarLugar

urlpatterns = [
    path('admin/', admin.site.urls),
    #Login
    path('accounts/', include('django.contrib.auth.urls')),
    #Registro
    path('Registro/', Registro, name='Registro'),
    #Principal Formulario
    path('Index/', Index, name='Index'),
    #LugarCrear
    path('CrearLugar/', LugarEventoCrear, name='LugarEventoCrear'),
    #VerLugar
    path('VerLugar/', VerLugar, name='VerLugar'),
    #ActualizarLugar
    path('VerActualizarLugar/<int:Id_Lugar>/', ActualizarLugar, name='VerActualizarLugar')

    
]
