from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tipo_usuarios(models.Model):

    tipos_usuario=(('administrador','administrador'),('vendedor','vendedor'),('cliente','cliente'))
    tipos_premium=((0,'sin premium'), (1,'premium nivel 1'), (2,'premium nivel 2'), (3,'premium nivel 3'))

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_usuario= models.CharField(verbose_name="Tipo de Usuario", max_length=200, blank=True, null=True, default="cliente", choices=tipos_usuario)
    tipo_premium= models.PositiveIntegerField(verbose_name="Tipo de Premium", default=0, null=True, blank=True, choices=tipos_premium)
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio del Premium", null=True, blank=True)
    fecha_caducidad = models.DateField(verbose_name="Fecha de Caducidad del Premium", null=True, blank=True)

    class Meta:
        verbose_name="Tipo de Usuarios"
        verbose_name_plural="Tipos de Usuarios"
        ordering=['tipo_usuario','fecha_caducidad','id']

    def __str__(self):
        return "{}, {}, tipo {}, premium {}, caduce {}".format(self.user_id.username, self.user_id.first_name, self.tipo_usuario, self.tipo_premium, self.fecha_caducidad)
