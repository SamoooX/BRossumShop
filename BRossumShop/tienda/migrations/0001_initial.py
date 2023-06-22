# Generated by Django 4.2.2 on 2023-06-22 02:07
from django.db import migrations, models, migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('imagen', models.CharField(max_length=500, verbose_name='Imagen')),
                ('stock', models.IntegerField(verbose_name='Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('correo', models.CharField(max_length=200, verbose_name='Correo')),
                ('contraseña', models.CharField(max_length=12, verbose_name='Contraseña')),
                ('contraseña2', models.CharField(max_length=12, verbose_name='Contraseña 2')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.boleta')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='id_usuario',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='tienda.Usuario'),
        ),
    ]
