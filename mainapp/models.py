from django.db import models
# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True, max_length=128)
    add_date = models.DateTimeField(verbose_name="Дата создания категории", auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Имя продукта", max_length=64)
    image = models.ImageField(verbose_name="Картинка продукта", upload_to="product_images",blank=True)
    short_desc = models.TextField(verbose_name="Краткое описание продукта", blank=True, max_length=64)
    description = models.TextField(verbose_name="Описание продукта", blank=True, max_length=128)
    price = models.DecimalField(verbose_name="Цена продукта", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="Количество продукта на складе", default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"




