from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaViewSet, ClienteViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('categorias',CategoriaViewSet)
router.register('clientes',ClienteViewSet)

urlpatterns = router.urls