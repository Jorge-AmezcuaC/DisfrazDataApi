from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            },
            'is_superuser': {
                'read_only': True
            },
            'is_staff': {
                'read_only': True
            },
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fotos
        fields = '__all__'

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proveedores
        fields = '__all__'
        
class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Talla
        fields = '__all__'
        
class DisfrazTallaSerializer(serializers.ModelSerializer):
    talla = TallaSerializer(read_only = True)
    class Meta:
        model = models.DisfrazTalla
        fields = [
            'id',
            'disfraz',
            'cantidad',
            'minStock',
            'maxStock',
            'precio',
            'talla',
        ]

class DisfrazTallaSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = models.DisfrazTalla
        fields = [
            'disfraz',
            'cantidad',
            'minStock',
            'maxStock',
            'precio',
            'talla',
        ]
        
class DisfracesSerializer(serializers.ModelSerializer):
    tallas = DisfrazTallaSerializer(many = True, read_only = True)
    fotos = FotoSerializer(many = True, read_only = True)
    class Meta:
        model = models.Disfraces
        fields = [
            'id',
            'Nombre',
            'Descripcion',
            'proveedor',
            'tallas',
            'fotos'
            ]
        
class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ventas
        fields = '__all__'
        
class VentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VentaProducto
        fields = '__all__'
        
class NotificacionesSerializer(serializers.ModelSerializer):
    producto = DisfracesSerializer(read_only = True)
    class Meta:
        model = models.Notificaciones
        fields = '__all__'
        
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrito
        fields = '__all__'