"""Faffu_Expressweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from core import views as coreviews
from login import views as loginviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', loginviews.login, name="login"),
    path('aguadesabores/', coreviews.aguadesabores, name="aguadesabores"),
    path('registro/', coreviews.registro, name="registro"),
    path('menu/', coreviews.menu, name="menu"),
    path('pedidos/', coreviews.pedidos, name="pedidos"),
    path('factura/', coreviews.factura, name="factura"),
    path('admin/', admin.site.urls),
]
