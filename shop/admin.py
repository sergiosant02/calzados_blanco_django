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

class ProductImageAdminInLine(admin.TabularInline):
    model = ProductImage
    fields = ('image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'image')
    
    extra = 1 
    
    def image(self, obj):
        # Devuelve una etiqueta HTML con la imagen para mostrarla en el admin
        return f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />'

    # Establece el atributo "image" como seguro (safe) para mostrar HTML
    image.allow_tags = True
    image.short_description = 'Imagen'
    
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
    
class FirstProductAdmin(UpdatingInfoAdmin):
    inlines=[ProductImageAdminInLine, SecondProductSpecAdminInLine]
    
class ProductAdmin(UpdatingInfoAdmin):
    list_display = ['name', 'category', 'created_at', 'updated_at']
    inlines = [ProductImageAdminInLine, FirstProductSpecAdminInLine]
    
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(FirstProductSpecification, FirstProductAdmin)
admin.site.register(SecondProductSpecification, UpdatingInfoAdmin)
