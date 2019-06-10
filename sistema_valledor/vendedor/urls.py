from django.urls import path
from .views import Listar_Productos, Agregar_Productos, Actualizar_Productos, Eliminar_Productos, Panel_de_vendedor, \
    Detalle_Local, Actualizar_Local, Panel_Listas, Detalle_Listas, Revisar_Listas, Mis_Ofertas, Agregar_Ofertas,\
    Actualizar_Ofertas, Eliminar_Ofertas,Detalle_pedidos_success, Reportes_Registro_Listas, Reportes_Premium

vendedor_urlpatterns = ([
    path('panel_de_vendedor/<int:id>/', Panel_de_vendedor, name = "panel_de_vendedor"),
    path('lista_productos/<int:id>/',Listar_Productos, name = "listar_productos"),
    path('agregar_productos/<int:id>/', Agregar_Productos, name="agregar_productos"),
    path('actualizar_productos/<int:id>/', Actualizar_Productos, name = "actualizar_productos"),
    path('eliminar_productos/<int:id>/', Eliminar_Productos, name = "eliminar_productos"),
    path('mi_tienda/<int:id>/',Detalle_Local, name = "mi_tienda"),
    path('actualizar_mi_tienda/<int:id>/', Actualizar_Local, name = "actualizar_mi_tienda"),
    path('mis_pedidos/<int:id>/', Panel_Listas, name = "mis_pedidos"),
    path('detalle_mis_pedidos/<int:id>/', Detalle_Listas, name = "detalle_mis_pedidos"),
    path('success_detalle_mis_pedidos/<int:id>/', Detalle_pedidos_success, name = "success_detalle_mis_pedidos"),
    path('revisar_mis_pedidos/<int:id>/', Revisar_Listas, name = "revisar_mis_pedidos"),
    path('mis_ofertas/<int:id>/', Mis_Ofertas, name="mis_ofertas"),
    path('agregar_oferta/<int:id>/',Agregar_Ofertas, name = "agregar_oferta"),
    path('actualizar_oferta/<int:id_oferta>/',Actualizar_Ofertas, name = "actualizar_oferta"),
    path('eliminar_oferta/<int:id_oferta>/',Eliminar_Ofertas, name = "eliminar_oferta"),
    path('reportes_listas/<int:id_user>/' , Reportes_Registro_Listas, name = "reporte_listas"),
    path('reporte_admin/' , Reportes_Premium, name = "reporte_admin"),
], 'vendedor')