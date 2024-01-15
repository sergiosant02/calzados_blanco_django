from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Servicio")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="services/", verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self) -> str:
        return self.title