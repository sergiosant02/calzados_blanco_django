from django.contrib import admin
from .models import ProductCategory, Product

# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)