from rest_framework import viewsets
from django.db import transaction
from rest_framework.exceptions import ValidationError
from .models import Producto, Categoria, Cliente, Pedido, DetallePedido
from .serializers import ProductoSerializer, CategoriaSerializer, ClienteSerializer, PedidoSerializer, DetallePedidoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            producto = Producto.objects.select_for_update().get(
                pk=serializer.validated_data['producto'].pk
            )

            cantidad = serializer.validated_data['cantidad']

            if producto.stock < cantidad:
                raise ValidationError({
                    'cantidad': f'Stock insuficiente. Disponible: {producto.stock}'
                })

            producto.stock -= cantidad
            producto.save(update_fields=['stock'])

            serializer.save()
        
    def perform_destroy(self, instance):
        with transaction.atomic():
            producto = Producto.objects.select_for_update().get(
                pk=instance.producto_id
            )

            producto.stock += instance.cantidad
            producto.save(update_fields=['stock'])

            instance.delete()

            