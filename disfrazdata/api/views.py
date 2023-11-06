from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from .models import (
    Disfraces, 
    DisfrazTalla, 
    Notificaciones, 
    Proveedores, 
    Talla, 
    VentaProducto, 
    Ventas,
    Fotos
    )
from .serializer import (
    DisfracesSerializer,
    DisfrazTallaSerializer,
    NotificacionesSerializer,
    ProveedoresSerializer,
    TallaSerializer,
    VentaProductoSerializer,
    VentasSerializer,
    UserSerializer,
    FotoSerializer,
    DisfrazTallaSerializerPost
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        try:
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
        except Exception as exc:
            return Response({'error':'Error desconocido'},status=status.HTTP_400_BAD_REQUEST)
        
class ProveedoresView(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Email']

class TallaView(viewsets.ModelViewSet):
    queryset = Talla.objects.all()
    serializer_class = TallaSerializer

class DisfracesView(viewsets.ModelViewSet):
    queryset = Disfraces.objects.all()
    serializer_class = DisfracesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Nombre']

class DisfrazTallaView(viewsets.ModelViewSet):
    queryset = DisfrazTalla.objects.all()
    serializer_class = DisfrazTallaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['precio']

class DisfrazTallaViewPost(viewsets.ModelViewSet):
    queryset = DisfrazTalla.objects.all()
    serializer_class = DisfrazTallaSerializerPost

class VentasView(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

class VentaProductoView(viewsets.ModelViewSet):
    queryset = VentaProducto.objects.all()
    serializer_class = VentaProductoSerializer

class NotificacionesView(viewsets.ModelViewSet):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer

class FotosView(viewsets.ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = FotoSerializer