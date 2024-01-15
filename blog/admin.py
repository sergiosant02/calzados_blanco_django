from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategroryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')

admin.site.register(Category, CategroryAdmin)
admin.site.register(Post, PostAdmin)