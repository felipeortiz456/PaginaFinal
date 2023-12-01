# En tu archivo forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'cantidad', 'precio', 'comentario', 'tipo_hamburguesa']
