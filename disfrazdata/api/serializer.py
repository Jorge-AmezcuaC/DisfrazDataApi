from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_superuser', 'is_staff', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            },
            'is_superuser': {
                'write_only': True
            },
            'is_staff': {
                'write_only': True
            },
        }

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
    class Meta:
        model = models.Notificaciones
        fields = '__all__'
        