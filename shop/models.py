from django.db import models
from django.core.validators import MinValueValidator
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
    price = models.DecimalField(verbose_name="Precio", decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    stock = models.IntegerField(verbose_name="Stock", validators=[MinValueValidator(0)])
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Categoría")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    @property
    def get_first_specifications(self):
        return FirstProductSpecification.objects.filter(product=self)
        

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name
    
   
class FirstProductSpecification(models.Model):
    data = models.CharField(max_length = 100, verbose_name="Información")
    stock = models.IntegerField(verbose_name="Stock", validators=[MinValueValidator(0)])
    price = models.DecimalField(verbose_name="Precio", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    @property
    def get_second_specifications(self):
        return SecondProductSpecification.objects.filter(first_spec=self)
    
    def __str__(self):
        return "%s - %s"%(self.product.name, self.data)
    
    class Meta:
        verbose_name = "Especificación de producto"
        verbose_name_plural = "Especificaciones de productos"
        
class SecondProductSpecification(models.Model):
    data = models.CharField(max_length = 100, verbose_name="Información")
    stock = models.IntegerField(verbose_name="Stock", validators=[MinValueValidator(0)])
    price = models.DecimalField(verbose_name="Precio", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    first_spec = models.ForeignKey(FirstProductSpecification, on_delete=models.CASCADE, verbose_name="Producto")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    def __str__(self):
        return "%s - %s"%(self.first_spec.__str__, self.data)
    
    class Meta:
        verbose_name = "Especificación extra de producto"
        verbose_name_plural = "Especificaciones extra de productos" 
        
        
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/", verbose_name="Imagen")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    
    class Meta:
        verbose_name = "Imagen de producto"
        verbose_name_plural = "Imagenes de productos"
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
