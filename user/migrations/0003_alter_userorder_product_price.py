# Generated by Django 4.0.5 on 2022-06-10 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productorder_table'),
        ('user', '0002_userorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='product_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
