from django.contrib import admin
from .models import Listas, Productos_listas

# Register your models here.

class Listas_admin(admin.ModelAdmin):
    pass

class Productos_listas_admin(admin.ModelAdmin):
    pass

admin.site.register(Listas, Listas_admin)
admin.site.register(Productos_listas, Productos_listas_admin)

