from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import FormCategoria
from vendedor.models import Productos, Local
from registration.models import Tipo_usuarios
from django.db.models import Q
# Create your views here.
def Panel_Cliente(request, id):
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
    except:
        tipo = None
    if tipo is not None and (tipo.tipo_usuario == 'cliente' or tipo.tipo_usuario == 'administrador') and id == request.user.id:
        try:
            cliente = User.objects.get(id=id)
        except:
            cliente = None
        return render(request, 'cliente/panel_cliente.html',{'cliente':cliente})
    else:
        return redirect('registration:sin_permiso')

def Listar_Productos(request):

    form = FormCategoria()
    locales = Local.objects.all()
    if request.method == 'POST':
        buscar = request.POST.get('buscar', None)
        categoria = request.POST.get('categoria', None)
        if buscar is not None:
            productos = Productos.objects.filter((Q(nombre__contains = buscar)|Q(nombre__icontains = buscar)),Q(activado = True)).order_by('-oferta').exclude(stock = 0)
        else:
            productos = Productos.objects.filter(Q(categoria = categoria),Q(activado = True)).order_by('-oferta').exclude(stock = 0)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos':productos, 'locales':locales})
    elif request.GET.get('filtro') == 'ofertas':
        productos = Productos.objects.filter(Q(oferta=True),Q(activado = True)).exclude(stock = 0)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales})
    else:
        productos = Productos.objects.filter(Q(activado = True)).order_by('-oferta').exclude(stock = 0)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales})

def Detalle_Productos(request, id):
    try:
        producto = Productos.objects.get(id = id)
        local = Local.objects.get(user = producto.user)
    except:
        local = None
        producto = None


    return render(request, 'cliente/detalle_productos.html',{'object':producto, 'local':local})

def Listado_Locales(request):
    return render(request, 'cliente/listado_locales.html',)

def Detalle_Locales(request,id):
    return render(request, 'cliente/detalle_locales.html',)

def Listar_Productos_Tiendas(request, id):
    return render(request, 'cliente/listar_productos_tiendas.html',)

def Mis_Listas(request, id):
    return render(request, 'cliente/mis_listas.html',)

def Detalle_Listas(request,id):
    return render(request, 'cliente/detalle_lista.html',)

def Agregar_Listas(request):
    return render(request, 'cliente/agregar_lista.html',)

def Actualizar_Listas(request, id):
    return render(request, 'cliente/actualizar_listas.html',)

def Eliminar_Listas(request, id):
    return render(request, 'cliente/eliminar_lista.html',)

def Eliminar_Productos_Listas(request, id, id_prod):
    return render(request, 'cliente/eliminar_producto_lista.html',)

def Actualizar_Productos_Listas(request, id, id_prod):
    return render(request, 'cliente/actualizar_producto_lista.html',)


