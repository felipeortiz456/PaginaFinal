# Generated by Django 4.2.7 on 2023-11-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_categoria_descuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('en_proceso', 'En proceso'), ('enviado', 'Enviado'), ('entregado', 'Entregado')], default='en_proceso', max_length=20),
        ),
    ]
