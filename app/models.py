from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descuento = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=3)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    cantidad = models.IntegerField(default=0)
    comentario = models.CharField(max_length=100,default="")


    SIMPLE = 'Simple'
    DOBLE = 'Doble'
    OPCIONES_HAMBURGUESA = [
        (SIMPLE, 'Hamburguesa Simple'),
        (DOBLE, 'Hamburguesa Doble'),
    ]

    # Agregar el campo de elección
    tipo_hamburguesa = models.CharField(
        max_length=10,
        choices=OPCIONES_HAMBURGUESA,
        default=SIMPLE,
    )
    

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
