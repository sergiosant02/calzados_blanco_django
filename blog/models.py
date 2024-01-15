from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Categoria")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="post/", verbose_name="Imagen", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return self.title