from django.shortcuts import render
import datetime

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {'title': 'GeekShop - Каталог', 'date_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    return render(request, 'mainapp/products.html', context)
