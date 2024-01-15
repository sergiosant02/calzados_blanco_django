from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Categoría de producto"
        verbose_name_plural = "Categorías de productos"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="products/", verbose_name="Imagen")
    price = models.FloatField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Categoría")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name