from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics
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
    Fotos,
    Carrito
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
    DisfrazTallaSerializerPost,
    CarritoSerializer,
    AuthSerializer
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

class CarritoView(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer


class UserLoginView(generics.CreateAPIView):
    serializer_class = AuthSerializer

    def create(self, request, *args, **kwargs):
        # Obtener datos del request
        username = request.data.get('username')
        password = request.data.get('password')
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Usuario autenticado, generando token
            token, _ = Token.objects.get_or_create(user=user)
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
            }
            return Response({'token': token.key, 'user': user_data})
        else:
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)