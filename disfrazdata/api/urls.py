from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'PostTallas', views.DisfrazTallaViewPost)
router.register(r'PostNotificaciones', views.PostNotificacionesView)
router.register(r'users', views.UserViewSet)
router.register(r'Proveedores', views.ProveedoresView)
router.register(r'Talla', views.TallaView)
router.register(r'Disfraces', views.DisfracesView)
router.register(r'DisfrazTalla', views.DisfrazTallaView)
router.register(r'Ventas', views.VentasView)
router.register(r'VentaProducto', views.VentaProductoView)
router.register(r'Notificaciones', views.NotificacionesView)
router.register(r'fotos', views.FotosView)
router.register(r'carro', views.CarritoView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)