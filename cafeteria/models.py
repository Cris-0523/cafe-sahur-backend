from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    imagen = models.CharField(max_length=255, blank=True)
    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT,related_name='productos')

class Cliente(models.Model):
        nombre = models.CharField(max_length=100)
        email = models.EmailField(max_length=254, unique=True)
        telefono = PhoneNumberField(blank=True)

class Pedido(models.Model):
    class Estado(models.TextChoices):
        CONFIRMADO = 'confirmado', 'Confirmado'
        PENDIENTE = 'pendiente', 'Pendiente'
        CANCELADO = 'cancelado', 'Cancelado'
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT,related_name='pedidos')
    estado = models.CharField(max_length=20,choices=Estado.choices,default=Estado.PENDIENTE)

class DetalleProducto(models.Model):
     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,related_name='detalles')
     producto = models.ForeignKey(Producto, on_delete=models.PROTECT,related_name='detalles_pedido')
     cantidad = models.PositiveIntegerField(validators=())
     precio_unitario = models.PositiveIntegerField()
     
