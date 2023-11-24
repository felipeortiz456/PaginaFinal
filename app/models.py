from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descuento = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('en_proceso', 'En proceso'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    direccion_entrega = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='en_proceso')
    # Agrega otros campos relacionados con el pedido según tus necesidades

    def __str__(self):
        return f"Pedido #{self.id} - {self.estado}"


# Create your models here.
