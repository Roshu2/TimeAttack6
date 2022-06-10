from django.contrib import admin
from .models import Product, Category, ProductOrder, OrderStatus

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductOrder)
admin.site.register(OrderStatus)

# Register your models here.

