# Generated by Django 4.0.5 on 2022-06-10 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productorder'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productorder',
            table='product_orders',
        ),
    ]
