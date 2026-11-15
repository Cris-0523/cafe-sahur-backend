from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaViewSet, ClienteViewSet, PedidoViewSet,DetallePedidoViewSet

router = DefaultRouter()
router.register('productos',ProductoViewSet)
router.register('categorias',CategoriaViewSet)
router.register('clientes',ClienteViewSet)
router.register('pedidos',PedidoViewSet)
router.register('detalle-pedidos',DetallePedidoViewSet)

urlpatterns = router.urls