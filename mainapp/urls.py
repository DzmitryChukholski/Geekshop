from django.urls import path

from mainapp.views import products, index

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', products, name='product')
]