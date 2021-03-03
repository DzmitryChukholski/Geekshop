from django.shortcuts import render
import datetime

from mainapp.models import Product, ProductCategory

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop - Каталог', 'date_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
