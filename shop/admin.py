from django.contrib import admin
from .models import Product, ProductCategory, FirstProductSpecification, SecondProductSpecification, ProductImage

# Register your models here.

class UpdatingInfoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
    
    
class UpdatingInfoInline(admin.TabularInline):
    readonly_fields = ('created_at', 'updated_at')
    
    
class SecondProductSpecAdminInLine(UpdatingInfoInline):
    model = SecondProductSpecification
    extra = 1 

class FirstProductSpecAdminInLine(UpdatingInfoInline):
    model = FirstProductSpecification
    inline=[SecondProductSpecAdminInLine]
    extra = 1

class ProductImageAdminInLine(UpdatingInfoInline):
    model = ProductImage
    extra = 1 
    
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
    
class FirstProductAdmin(UpdatingInfoAdmin):
    inlines=[SecondProductSpecAdminInLine]
    
class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
    inlines = [FirstProductSpecAdminInLine, ProductImageAdminInLine]
    
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(FirstProductSpecification, FirstProductAdmin)
admin.site.register(SecondProductSpecification, UpdatingInfoAdmin)