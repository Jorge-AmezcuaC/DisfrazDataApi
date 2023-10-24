from django.db import models
from django.contrib.auth.models import User

class Proveedores(models.Model):
    Nombre = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    Telefono = models.CharField(max_length=12)

class Talla(models.Model):
    tallas = (('XL', 'xl'),
              ('X', 'x'),
              ('M', 'm'),
              ('S', 's'),
              ('XS', 'xs')
              )
    talla = models.CharField(max_length=2, choices=tallas)

class Disfraces(models.Model):
    Nombre = models.CharField(max_length=40)
    Descripcion = models.CharField(max_length=255)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

class DisfrazTalla(models.Model):
    disfraz = models.ForeignKey(Disfraces, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    minStock = models.IntegerField()
    maxStock = models.IntegerField()
    precio = models.FloatField()

class Ventas(models.Model):
    Fecha = models.DateTimeField()
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    Cantidad = models.FloatField()
    Total = models.FloatField()

class VentaProducto(models.Model):
    producto = models.ForeignKey(DisfrazTalla, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)

class Notificaciones(models.Model):
    Mensaje = models.CharField(max_length=255)
    Estado = models.BooleanField(default=False)
    Fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
