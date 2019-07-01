from django.contrib import admin
from .models import Tipo_usuarios, Log_Acceso, Preguntas_secretas, Login_respuesta_secreta
# Register your models here.

class Tipo_usuario_admin(admin.ModelAdmin):
    list_display = ('user_id', 'tipo_usuario', 'tipo_premium', 'fecha_caducidad')
    search_fields = ('user_id__username', 'user_id__first_name')
    list_filter = ('user_id__username',)

class Login_respuesta_secreta_admin(admin.ModelAdmin):
    list_display = ('user', 'pregunta', 'respuesta')
    search_fields = ('user__username',)
    list_filter = ('user__username',)


admin.site.register(Tipo_usuarios, Tipo_usuario_admin)
admin.site.register(Log_Acceso,)
admin.site.register(Preguntas_secretas,)
admin.site.register(Login_respuesta_secreta, Login_respuesta_secreta_admin)