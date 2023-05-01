"""
URL configuration for Proyecto3 project.

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
from django.urls import path
from Proyecto3.views import autor_form, libro_form, editorial_form, busqueda_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autor/', autor_form, name='autor_form'),
    path('libros/', libro_form, name='libro_form'),
    path('editorial/', editorial_form, name='editorial_form'),
    path('busqueda/', busqueda_form, name='busqueda_form'),
]