from django.contrib import admin
from .models import Local, Categoria_Productos, Unidad_Medida, Productos, Oferta, Puntos, Registro_auditoria_productos

# Register your models here.

class Local_admin(admin.ModelAdmin):
    list_display = ('nombre_local', 'user', 'ubicacion_local', 'activado',)
    search_fields = ('nombre_local',)
    list_filter = ('user',)

class Categoria_Productos_admin(admin.ModelAdmin):
    pass

class Unidad_Medida_admin(admin.ModelAdmin):
    list_display = ('medida_unidad', 'medida_plural')
    search_fields = ('medida_unidad',)
    list_filter = ('medida_unidad', 'medida_plural')

class Productos_admin(admin.ModelAdmin):
    list_display = ('nombre', 'user', 'precio', 'categoria', 'stock', 'unidad_medida', 'activado')
    search_fields = ('nombre',)
    list_filter = ('user',)

class Oferta_admin(admin.ModelAdmin):
    list_display = ('oferta', 'tipo_oferta', 'local', 'activado')
    search_fields = ('user',)
    list_filter = ('local', 'local__user')

class Puntos_admin(admin.ModelAdmin):
    pass

class Registro_auditoria_productos_admin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'vendedor_id', 'nombre_producto', 'accion', 'fecha_registro')
    search_fields = ('producto',)
    list_filter = ('vendedor',)

admin.site.register(Local, Local_admin)
admin.site.register(Categoria_Productos, Categoria_Productos_admin)
admin.site.register(Unidad_Medida, Unidad_Medida_admin)
admin.site.register(Productos, Productos_admin)
admin.site.register(Oferta, Oferta_admin)
admin.site.register(Puntos, Puntos_admin)
admin.site.register(Registro_auditoria_productos, Registro_auditoria_productos_admin)