from django.contrib import admin
from .models import (
    Proveedores,
    Talla,
    Disfraces,
    DisfrazTalla,
    Ventas,
    VentaProducto,
    Notificaciones,
)

admin.site.register(Proveedores)
admin.site.register(Talla)
admin.site.register(Disfraces)
admin.site.register(DisfrazTalla)
admin.site.register(Ventas)
admin.site.register(VentaProducto)
admin.site.register(Notificaciones)
