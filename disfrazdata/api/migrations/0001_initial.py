# Generated by Django 4.2.6 on 2023-10-24 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disfraces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DisfrazTalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('minStock', models.IntegerField()),
                ('maxStock', models.IntegerField()),
                ('precio', models.FloatField()),
                ('disfraz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.disfraces')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Telefono', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(choices=[('XL', 'xl'), ('X', 'x'), ('M', 'm'), ('S', 's'), ('XS', 'xs')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField()),
                ('Cantidad', models.FloatField()),
                ('Total', models.FloatField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.disfraztalla')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ventas')),
            ],
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mensaje', models.CharField(max_length=255)),
                ('Estado', models.BooleanField(default=False)),
                ('Fecha', models.DateField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedores')),
            ],
        ),
        migrations.AddField(
            model_name='disfraztalla',
            name='talla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.talla'),
        ),
        migrations.AddField(
            model_name='disfraces',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedores'),
        ),
    ]
