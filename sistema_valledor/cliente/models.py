from django.db import models
from vendedor.models import Local, Productos
from django.contrib.auth.models import User
from registration.models import Tipo_usuarios

# Create your models here.
class Listas(models.Model):
    estados_de_listas = (('lista_retiro', 'Listo para retirar'), ('armando_pedido', 'Armando Pedido'), ('normal', 'Normal'),
                         ('enviada', 'Enviada'), ('cancelada', 'Cancelada'),
                          ('no_retirada', 'No retirada'),('completada', 'Lista completada'))
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(verbose_name="Nombre de la lista", null=True, blank=True, max_length=200)
    total = models.PositiveIntegerField(verbose_name="Total de la lista", null=True, blank=True, default=0)
    fecha_enviado = models.DateField(verbose_name="Fecha de envio de la lista", null=True, blank=True)
    fecha_expiracion = models.DateField(verbose_name="Fecha de expiracion de la lista", null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(verbose_name="Fecha de actualizacion de la lista", null=True, blank=True, auto_now=True)
    comentario_cliente = models.TextField(verbose_name="Comentario de cliente", null=True, blank=True)
    comentario_vendedor = models.TextField(verbose_name="Comentario de vendedor", null=True, blank=True)
    estado_lista = models.CharField(verbose_name="Estado de la lista", max_length=200, null=True, blank=True, choices=estados_de_listas, default='normal')
    cancelaciones = models.PositiveIntegerField(verbose_name = "Veces restantes a cancelar la lista", null=True, blank=True, default=5)
    total_marcado = models.PositiveIntegerField(verbose_name="Total de los productos marcados", null=True, blank=True, default=0)
    valorizacion = models.BooleanField(verbose_name="Fue Valorizada?",null= True, blank=True, default=False)

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
    producto_marcado = models.BooleanField(verbose_name="Producto marcado", null=True, blank=True, default=False)
    oferta = models.BooleanField(verbose_name="Producto en Oferta", null=True, blank=True, default=False)

    class Meta:
        verbose_name = "Producto de la lista"
        verbose_name_plural = "Productos de las listas"

    def __str__(self):
        return "{}, perteneciente al local {}".format(self.productos.nombre, self.local.nombre_local)

#Reporteria para clientes
class Reporte_listas(models.Model):
    lista = models.PositiveIntegerField(verbose_name="ID lista", default=0, null=True, blank=True)
    local = models.ForeignKey(Local, on_delete= models.CASCADE, null = True, blank = True)
    nombre_lista = models.CharField(verbose_name="Nombre de la lista", max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_registro = models.DateField(verbose_name="Fecha de registro", null=True, blank=True)
    total = models.PositiveIntegerField(verbose_name="Total del pedido", null = True, blank=True)
    cantidad_items = models.PositiveIntegerField(verbose_name="Total de Items", null = True, blank=True)
    cantidad_productos = models.PositiveIntegerField(verbose_name="Total de productos", null=True, blank=True)
    estado = models.CharField(verbose_name="Estado del pedido", null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = "Reporte de Pedidos"
        verbose_name_plural = "Reporte de Pedidos"

    def __str__(self):
        return "ID Reporte {}".format(self.id)


#Auditoria para admin
class Registro_premium(models.Model):
    id_registro = models.ForeignKey(Tipo_usuarios, on_delete=models.CASCADE, null=True, blank=True)
    user = user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    premium= models.PositiveIntegerField(verbose_name="Tipo de Premium", default=0, null=True, blank=True)
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio del Premium", null=True, blank=True)
    fecha_caducidad = models.DateField(verbose_name="Fecha de Caducidad del Premium", null=True, blank=True)

    class Meta:
        verbose_name = "Auditoria de premium"
        verbose_name_plural = "Auditoria de premium"

    def __str__(self):
        return "ID Registro {}".format(self.id)

#Reporte productos
#Despues de completar un pedido se tienen que ingresar datos aca
class Reporte_productos(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    lista = models.PositiveIntegerField(verbose_name="ID Lista", default=0, null=True, blank=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.PositiveIntegerField(verbose_name="ID Producto", default=0, null=True, blank=True)
    nombre_producto = models.CharField(verbose_name="Nombre Producto", max_length=200, null=True, blank=True)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad Comprada", null=True, blank=True, default=0)
    oferta = models.BooleanField(verbose_name="Producto en Oferta", null=True, blank=True, default=False)
    Total = models.PositiveIntegerField(verbose_name="Total", null=True, blank=True, default=0)
    fecha_registro = models.DateField(verbose_name="Fecha de registro", null=True, blank=True)

    class Meta:
        verbose_name = "Reporte de Productos"
        verbose_name_plural = "Reporte de Productos"

    def __str__(self):
        return "ID Reporte {}".format(self.id)

#Puntaje de pedidos
class Valorizacion_pedidos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    lista = models.PositiveIntegerField(verbose_name="ID lista", default=0, null=True, blank=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)
    puntuacion = models.PositiveIntegerField(verbose_name="Puntuacion", default=0, null=True, blank=True)
    fecha_registro = models.DateField(verbose_name="Fecha de registro", null=True, blank=True)
    comentarios = models.TextField(verbose_name="Comentarios del pedido", null=True, blank=True)

    class Meta:
        verbose_name = "Valorizacion de Pedidos"
        verbose_name_plural = "Valorizacion de Pedidos"

    def __str__(self):
        return "ID Registro {}".format(self.id)