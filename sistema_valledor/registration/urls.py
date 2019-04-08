from django.urls import path
from .views import registro, mi_perfil, sin_permiso, actualizar_perfil

registration_urlpatterns = ([
    path('registro/', registro , name="registro"),
    path('mi_perfil/<int:id>/', mi_perfil, name="mi_perfil"),
    path('sin_permiso/', sin_permiso, name="sin_permiso"),
    ],'registration')