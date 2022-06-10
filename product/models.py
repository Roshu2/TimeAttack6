from django.db import models

# Create your models here.

class Product(models.Model):
    class Meta:
        db_table = 'products'
    name = models.CharField(max_length=70, default='')
    category = models.ManyToManyField('Category', related_name='product')
    image = models.TextField(max_length=256, default='')
    description = models.TextField(max_length=256, default='')
    price = models.CharField(max_length=70, default='')
    stock = models.CharField(max_length=70, default='')


class Category(models.Model):
    class Meta:
        db_table = 'categories'
    category_name = models.CharField(max_length=70, default='')


class ProductOrder(models.Model):
    class Meta:
        db_table = 'product_orders'
    product_count = models.CharField(max_length=70, default='')

class OrderStatus(models.Model):
    class Meta:
        db_table = 'order_statuses'
    status_name = models.CharField(max_length=70, default='')


