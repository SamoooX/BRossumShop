# Generated by Django 4.2.1 on 2023-06-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_alter_boleta_id_usuario_alter_carrito_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
