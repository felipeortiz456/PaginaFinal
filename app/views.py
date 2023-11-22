from django.shortcuts import render
# Create your views here.
from .models import Producto,Pedido

def home(request):
    # Obtén todos los productos desde la base de datos
    productos = Producto.objects.all()

    # Pasa la lista de productos al contexto de la plantilla
    context = {'productos': productos}

    # Renderiza la plantilla y pasa el contexto
    return render(request, 'app/home.html', context)



def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):


    pedidos = Pedido.objects.all ()
    context = { 'pedidos': pedidos}
    return render(request,'app/galeria.html', context)
