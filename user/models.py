from django.db import models
from product.models import Product
# Create your models here.


class User(models.Model):
    class Meta:
        db_table = 'users'
    email = models.CharField(max_length=70, default='')
    password = models.CharField(max_length=70, default='')

class UserOrder(models.Model):
    class Meta:
        db_table = 'user_orders'
    adress = models.TextField(max_length=256, default='')
    ordered_time = models.DateTimeField(auto_now_add=True)
    product_price = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_sale = models.CharField(max_length=70, default='')
    sale_price = models.CharField(max_length=70, default='')
    is_ok = models.CharField(max_length=70, default='')



