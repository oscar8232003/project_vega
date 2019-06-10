from django.urls import path
from .views import Panel_Cliente, Listar_Productos, Detalle_Productos, Listado_Locales, Detalle_Locales, \
    Listar_Productos_Tiendas, Mis_Listas, Detalle_Listas, Agregar_Listas, Actualizar_Listas, Eliminar_Listas, \
    Eliminar_Productos_Listas, Actualizar_Productos_Listas, Detalle_lista_success


cliente_urlpatterns = ([
    path('panel_cliente/<int:id>/', Panel_Cliente, name="panel_cliente"),
    path('listar_productos/', Listar_Productos, name="listar_productos"),
    path('detalle_productos/<int:id>/', Detalle_Productos, name="detalle_productos"),
    path('listado_locales/', Listado_Locales, name="listado_locales"),
    path('detalle_locales/<int:id>/', Detalle_Locales, name="detalle_locales"),
    path('listar_productos_tiendas/<int:id>/', Listar_Productos_Tiendas, name="listar_productos_tiendas"),
    path('mis_listas/<int:id>/', Mis_Listas, name="mis_listas"),
    path('detalle_listas/<int:id>/', Detalle_Listas, name="detalle_listas"),
    path('success_detalle_lista/<int:id>/',Detalle_lista_success , name = "detalle_lista_ok"),
    path('agregar_lista/', Agregar_Listas, name="agregar_lista"),
    path('actualizar_lista/<int:id>/', Actualizar_Listas, name="actualizar_lista"),
    path('eliminar_lista/<int:id>/', Eliminar_Listas, name="eliminar_lista"),
    path('detalle_listas/<int:id_lista>/eliminar_producto_lista/<int:id_prod>',Eliminar_Productos_Listas, name="eliminar_producto_lista"),
    path('detalle_listas/<int:id_lista>/actualizar_producto_lista/<int:id_prod>',Actualizar_Productos_Listas, name="actualizar_producto_lista"),
    ],'cliente')