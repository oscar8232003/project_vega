from django.db import models
from django.contrib.auth.models import User

class Categoria_Productos(models.Model):
    categoria = models.CharField(verbose_name="Categoria", max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['categoria']
        verbose_name ="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.categoria

class Unidad_Medida(models.Model):
    medida_unidad = models.CharField(verbose_name="Unidad de Medida Unidad", max_length=200, null=True, blank=True)
    medida_plural = models.CharField(verbose_name="Unidad de Medida Plural", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medidas"

    def __str__(self):
        return self.medida_unidad

# Create your models here.
class Productos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    nombre = models.CharField(verbose_name="Nombre", max_length=200, null=True, blank=True)
    precio = models.PositiveIntegerField(verbose_name="Precio", null=True, blank=True, default=0)
    categoria = models.ForeignKey(Categoria_Productos, on_delete=models.CASCADE,null=True, blank=True)
    oferta = models.BooleanField(verbose_name="Producto en Oferta", null=True, blank=True, default=False)
    precio_oferta = models.PositiveIntegerField(verbose_name="Precio de la Oferta", null=True, blank=True, default=0)
    stock = models.PositiveIntegerField(verbose_name="Stock del Producto", null=True, blank=True, default=0)
    imagen = models.ImageField(upload_to='vendedor/img_productos/', null=True, blank=True, default='core/sin_imagen.jpg')
    cambios_restantes = models.PositiveIntegerField(verbose_name="Cambios restantes de precios", null=True, blank=True,
                                                    default=3)
    activado = models.BooleanField(verbose_name="Producto activado?", null=True, blank=True, default=True)
    unidad_medida = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.TextField(verbose_name="Comentarios", null=True, blank=True)

    class Meta:
        ordering = ['oferta', 'precio', 'nombre']
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

class Local(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre_local = models.CharField(verbose_name="Nombre del Local", max_length=200, null=True, blank=True)
    ubicacion_local = models.CharField(verbose_name="Ubicacion del Local", max_length=200, null=True, blank=True)
    imagen_muestra = models.ImageField(verbose_name="Imagen de muestra", upload_to='vendedor/img_tiendas/', default='core/sin_imagen.jpg', null=True, blank=True)
    imagen_banner = models.ImageField(verbose_name="Imagen de Banner", upload_to='vendedor/img_tiendas/',default='core/sin_imagen.jpg', null=True, blank=True)

    class Meta:
        ordering=['nombre_local']
        verbose_name = "Local"
        verbose_name_plural = "Locales"

    def __str__(self):
        return self.nombre_local

class Oferta(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)
    oferta = models.CharField(verbose_name="Oferta", null=True, blank=True, max_length=200)
    tipo_oferta = models.CharField(verbose_name="Tipo de Oferta", null = True, blank = True, max_length=200)
    activado = models.BooleanField(verbose_name="Oferta activada?", null=True, blank=True, default=True)

    class Meta:
        ordering = ['tipo_oferta']
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"

    def __str__(self):
        return self.oferta

class Puntos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    puntos = models.PositiveIntegerField(verbose_name="Total de puntos", null=True, blank=True, default=0)
    local = models.ForeignKey(Local, on_delete=models.CASCADE,null=True, blank=True)
    tipo_cuenta = models.CharField(verbose_name="Tipo de cuenta", null=True, blank=True, max_length=200)

    class Meta:
        ordering = ['user']
        verbose_name = "Puntos"
        verbose_name_plural = "Puntos"

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.tipo_cuenta)