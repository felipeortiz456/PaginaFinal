from django.urls import path
from .views import home, contacto, galeria,cambiar_estado_pedido
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home , name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('pedidos/', galeria, name='lista_pedidos'),
    path('cambiar_estado/<int:pedido_id>/', cambiar_estado_pedido, name='cambiar_estado_pedido'),

]
