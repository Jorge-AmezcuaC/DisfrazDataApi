# Generated by Django 4.2.6 on 2023-11-06 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_notificaciones_producto_alter_ventas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='Fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 11, 6, 20, 28, 27, 685338, tzinfo=datetime.timezone.utc)),
        ),
    ]
