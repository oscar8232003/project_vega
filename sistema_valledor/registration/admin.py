from django.contrib import admin
from .models import Tipo_usuarios
# Register your models here.

class Tipo_usuario_admin(admin.ModelAdmin):
    list_display = ('user_id', 'tipo_usuario', 'tipo_premium', 'fecha_caducidad')
    search_fields = ('user_id__username', 'user_id__first_name')
    list_filter = ('user_id__username',)

admin.site.register(Tipo_usuarios, Tipo_usuario_admin)