from django.shortcuts import render,redirect
from django.contrib import messages
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

#Cambiar estado.
def cambiar_estado_pedido(request, pedido_id):
    if request.method == 'POST':
        nuevo_estado = request.POST.get('nuevo_estado')
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.estado = nuevo_estado
        pedido.save()
        messages.success(request, f"Estado del Pedido #{pedido.id} cambiado a {nuevo_estado}.")
        return redirect('lista_pedidos')
    return render(request, 'app/galeria.html')