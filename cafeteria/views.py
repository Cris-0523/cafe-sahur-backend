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


    def perform_update(self, serializer):
        with transaction.atomic():
            detalle = serializer.instance
            datos = serializer.validated_data

            producto_anterior_id = detalle.producto_id
            cantidad_anterior = detalle.cantidad

            producto_nuevo = datos.get('producto', detalle.producto)
            cantidad_nueva = datos.get('cantidad', detalle.cantidad)

            if cantidad_nueva <= 0:
                raise ValidationError({
                    'cantidad': 'La cantidad debe ser mayor que cero.'
                })

            ids_productos = sorted({
                producto_anterior_id,
                producto_nuevo.pk
            })

            productos = {
                p.pk: p
                for p in Producto.objects.select_for_update()
                .filter(pk__in=ids_productos)
                .order_by('pk')
            }

            producto_anterior = productos[producto_anterior_id]
            producto_nuevo_obj = productos[producto_nuevo.pk]

            if producto_anterior_id == producto_nuevo.pk:
                diferencia = cantidad_nueva - cantidad_anterior

                if diferencia > 0:
                    if producto_anterior.stock < diferencia:
                        raise ValidationError({
                            'cantidad': f'Stock insuficiente. Disponible: {producto_anterior.stock}'
                        })

                    producto_anterior.stock -= diferencia

                elif diferencia < 0:
                    producto_anterior.stock += abs(diferencia)

                producto_anterior.save(update_fields=['stock'])

            else:
                if producto_nuevo_obj.stock < cantidad_nueva:
                    raise ValidationError({
                        'cantidad': f'Stock insuficiente. Disponible: {producto_nuevo_obj.stock}'
                    })

                producto_anterior.stock += cantidad_anterior
                producto_nuevo_obj.stock -= cantidad_nueva

                producto_anterior.save(update_fields=['stock'])
                producto_nuevo_obj.save(update_fields=['stock'])

            serializer.save()

        
    def perform_destroy(self, instance):
        with transaction.atomic():
            producto = Producto.objects.select_for_update().get(
                pk=instance.producto_id
            )

            producto.stock += instance.cantidad
            producto.save(update_fields=['stock'])

            instance.delete()

            