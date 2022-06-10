from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def list_view(request):
    categories = Category.objects.all()

    return render(request, 'list.html', {'categories': categories})

def detail_view(request, id):
    category = Category.objects.filter(id=id).values()
    products = Product.objects.filter()

    return render(request, 'detail.html')