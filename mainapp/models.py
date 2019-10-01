from django.db import models
# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="name", max_length=64, unique=True)
    description = models.TextField(verbose_name="description", blank=True, max_length=128)
    is_active = models.BooleanField(verbose_name="active", default=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Product name", max_length=64)
    image = models.ImageField(verbose_name="Product image", upload_to="product_images",blank=True)
    shortdesc = models.TextField(verbose_name="Short products description", blank=True, max_length=64)
    description = models.TextField(verbose_name="Product description", blank=True, max_length=128)
    price = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="Quantity", default=0)
    is_active = models.BooleanField(verbose_name="active", default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
