from django.urls import path
from .views import registro, mi_perfil, sin_permiso, actualizar_perfil, seleccionar_usuario, seleccion_usuario_cliente, seleccion_usuario_vendedor

registration_urlpatterns = ([
    path('registro/', registro , name="registro"),
    path('mi_perfil/<int:id>/', mi_perfil, name="mi_perfil"),
    path('sin_permiso/', sin_permiso, name="sin_permiso"),
    path('seleccion/usuario/', seleccionar_usuario, name = "seleccion_usuario"),
    path('seleccion/usuario/cliente/', seleccion_usuario_cliente, name= "seleccion_usuario_cliente"),
    path('seleccion/usuario/vendedor/', seleccion_usuario_vendedor, name = 'seleccion_usuario_vendedor'),
    ],'registration')