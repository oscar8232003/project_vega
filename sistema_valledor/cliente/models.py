from django.db import models
from vendedor.models import Local, Productos
from django.contrib.auth.models import User

# Create your models here.
class Listas(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True )
    nombre = models.CharField(verbose_name="Nombre del Local", null=True, blank=True, max_length=200)
    total = models.PositiveIntegerField(verbose_name="Total de la lista", null=True, blank=True, default=0)
    fecha_enviado = models.DateField(verbose_name="Fecha de envio de la lista", null=True, blank=True)
    fecha_expiracion = models.DateField(verbose_name="Fecha de expiracion de la lista", null=True, blank=True)
    comentarios = models.TextField(verbose_name="Comentarios", null=True, blank=True)
    estado = models.BooleanField(verbose_name="Estado de la lista", null=True, blank=True, default="normal")

    class Meta:
        verbose_name = "Listas"
        verbose_name_plural = "Listas"

    def __str__(self):
        return self.nombre

class Productos_listas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True, blank=True )
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True )
    lista = models.ForeignKey(Listas, on_delete=models.CASCADE, null=True, blank=True )
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad a comprar", null=True, blank=True, default=0)
    comentarios = models.TextField(verbose_name="Comentarios del productos a comprar", null=True, blank=True)
    precio_producto = models.PositiveIntegerField(verbose_name="Precio actual del producto a comprar", null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Producto de la lista"
        verbose_name_plural = "Productos de las listas"

    def __str__(self):
        return "{}, perteneciente al local {}".format(self.productos.nombre, self.local.nombre_local)