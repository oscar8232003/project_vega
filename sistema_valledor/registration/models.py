from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tipo_usuarios(models.Model):

    tipos_usuario=(('administrador','administrador'),('vendedor','vendedor'),('cliente','cliente'))
    tipos_premium=((0,'sin premium'), (1,'premium nivel 1'), (2,'premium nivel 2'), (3,'premium nivel 3'))

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_usuario= models.CharField(verbose_name="Tipo de Usuario", max_length=20, blank=True, null=True, default="cliente", choices=tipos_usuario)
    tipo_premium= models.PositiveIntegerField(verbose_name="Tipo de Premium", default=0, null=True, blank=True, choices=tipos_premium)
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio del Premium", null=True, blank=True)
    fecha_caducidad = models.DateField(verbose_name="Fecha de Caducidad del Premium", null=True, blank=True)

    class Meta:
        verbose_name="Tipo de Usuarios"
        verbose_name_plural="Tipos de Usuarios"
        ordering=['tipo_usuario','fecha_caducidad','id']

    def __str__(self):
        return "{}, {}, tipo {}, premium {}, caduce {}".format(self.user_id.username, self.user_id.first_name, self.tipo_usuario, self.tipo_premium, self.fecha_caducidad)

class Log_Acceso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_registro = models.CharField(verbose_name="Fecha de Registro", max_length=30, blank=True, null=True)
    tipo_cliente = models.CharField(verbose_name="Tipo de Cliente", max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = "Log de Acceso"
        verbose_name_plural = "Log de Accesos"

    def __str__(self):
        return "Registro ID {}".format(self.id)

class Preguntas_secretas(models.Model):
    pregunta= models.CharField(verbose_name="Pregunta Secreta", null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = "Preguntas secretas"
        verbose_name_plural = "Preguntas secretas"

    def __str__(self):
        return "{}".format(self.pregunta)

class Login_respuesta_secreta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Preguntas_secretas, on_delete=models.CASCADE)
    respuesta = models.CharField(verbose_name="Respuesta Secreta", null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = "Tabla de Preguntas y Respuestas"
        verbose_name_plural = "Tabla de Preguntas y Respuestas"

    def __str__(self):
        return "{} - {}".format(self.pregunta, self.respuesta)