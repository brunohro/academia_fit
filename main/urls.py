"""
URL configuration for main project.

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
from django.urls import path
from academia.views import index
from academia.views import cadastro_personal, editar_personal, remover_personal
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("cadastro_personal/", cadastro_personal, name="cadastro_personal"),
    path("editar_personal/ <int:id>", editar_personal, name="editar_personal"),
    path("remover_personal/ <int:id>", remover_personal, name="remover_personal"),
]
