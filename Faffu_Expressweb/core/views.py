from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required

# Create your views here.

def registro(request):
    return render(request, "core/registro.html")

def menu(request):
    return render(request, "core/menu.html")

def pedidos(request):
    return render(request, "core/pedidos.html")

def factura(request):
    return render(request, "core/factura.html")

def aguadesabores(request):
    return render(request, "core/aguadesabores.html")
