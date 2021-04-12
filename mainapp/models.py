from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Categories'


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'

    def get_item(self):
        return Product.objects.filter(is_active=True).order_by('category', 'name')
