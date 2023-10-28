from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Proveedores(models.Model):
    Nombre = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    Telefono = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.Nombre} {self.Email} {self.Telefono}'

class Talla(models.Model):
    tallas = (('XL', 'xl'),
              ('X', 'x'),
              ('M', 'm'),
              ('S', 's'),
              ('XS', 'xs')
              )
    talla = models.CharField(max_length=2, choices=tallas)

    def __str__(self):
        return f'{self.talla}'

class Disfraces(models.Model):
    Nombre = models.CharField(max_length=40)
    Descripcion = models.CharField(max_length=255)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Nombre}'

class DisfrazTalla(models.Model):
    disfraz = models.ForeignKey(Disfraces, on_delete=models.CASCADE, related_name='tallas')
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    minStock = models.IntegerField()
    maxStock = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f'{self.disfraz} {self.talla} {self.precio}$'

class Ventas(models.Model):
    Fecha = models.DateTimeField(timezone.now())
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    Total = models.FloatField(default=0)

    def __str__(self):
        return f'{self.Fecha} {self.empleado} {self.Total}$'

class VentaProducto(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    producto = models.ForeignKey(DisfrazTalla, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return f'{self.venta} {self.producto} {self.cantidad} {self.subtotal}$'

class Notificaciones(models.Model):
    Mensaje = models.CharField(max_length=255)
    Estado = models.BooleanField(default=False)
    Fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Fecha} {self.Estado} {self.proveedor}'

class Fotos(models.Model):
    foto = models.ImageField(upload_to='disfraz')
    disfraz = models.ForeignKey(Disfraces, on_delete=models.CASCADE, related_name='fotos')

    def __str__(self):
        return f'{self.foto} {self.disfraz}'