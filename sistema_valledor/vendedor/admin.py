from django.contrib import admin
from .models import Local, Categoria_Productos, Unidad_Medida, Productos, Oferta, Puntos
# Register your models here.

class Local_admin(admin.ModelAdmin):
    pass

class Categoria_Productos_admin(admin.ModelAdmin):
    pass

class Unidad_Medida_admin(admin.ModelAdmin):
    pass

class Productos_admin(admin.ModelAdmin):
    pass

class Oferta_admin(admin.ModelAdmin):
    pass

class Puntos_admin(admin.ModelAdmin):
    pass

admin.site.register(Local, Local_admin)
admin.site.register(Categoria_Productos, Categoria_Productos_admin)
admin.site.register(Unidad_Medida, Unidad_Medida_admin)
admin.site.register(Productos, Productos_admin)
admin.site.register(Oferta, Oferta_admin)
admin.site.register(Puntos, Puntos_admin)