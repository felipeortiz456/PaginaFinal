from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descuento = models.CharField(max_length=200)


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



# Create your models here.
