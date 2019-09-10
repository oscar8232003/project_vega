#Defecto para el administrador.
from django.contrib import admin

#Importar los models de referencia
from .models import Listas, Productos_listas, Registro_premium

# Register your models here.

class Listas_admin(admin.ModelAdmin):
    list_display = ('user', 'local', 'nombre', 'estado_lista',)

class Productos_listas_admin(admin.ModelAdmin):
    pass


# class Registro_listas_admin(admin.ModelAdmin):
#     list_display = ('id','cliente_id','cliente', 'lista_id', 'local_id', 'local', 'fecha_registro', 'estado')
#     search_fields = ('id',)
#     list_filter = ('cliente_id', 'lista_id', 'local_id')


@admin.register(Registro_premium)
class Registro_premium_admin(admin.ModelAdmin):
    list_display = ('id', 'id_registro_id', 'user_id', 'premium', 'fecha_inicio', 'fecha_caducidad')
    search_fields = ('id',)
    list_filter = ('user', 'premium')

admin.site.register(Listas, Listas_admin)
admin.site.register(Productos_listas, Productos_listas_admin)
#admin.site.register(Registro_listas, Registro_listas_admin)
#admin.site.register(Registro_premium, Registro_premium_admin)

