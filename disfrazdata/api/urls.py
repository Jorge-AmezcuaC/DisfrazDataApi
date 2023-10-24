from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'Proveedores', views.ProveedoresView)
router.register(r'Talla', views.TallaView)
router.register(r'Disfraces', views.DisfracesView)
router.register(r'DisfrazTalla', views.DisfrazTallaView)
router.register(r'Ventas', views.VentasView)
router.register(r'VentaProducto', views.VentaProductoView)
router.register(r'Notificaciones', views.NotificacionesView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]