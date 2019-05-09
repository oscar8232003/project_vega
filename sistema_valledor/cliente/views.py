from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import FormCategoria
from vendedor.models import Productos, Local, Oferta
from registration.models import Tipo_usuarios
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def Panel_Cliente(request, id):
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
    except:
        tipo = None
    if tipo is not None and tipo.tipo_usuario == 'cliente' and id == request.user.id:
        cliente = get_object_or_404(User,id=id)
        ofertas_generales = Oferta.objects.filter(Q(tipo_oferta='general'), Q(activado=True), Q(local__activado=True)).order_by('local__nombre_local')
        return render(request, 'cliente/panel_cliente.html',{'cliente':cliente, 'oferta_general':ofertas_generales, })
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
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos':productos, 'locales':locales,})
    elif request.GET.get('filtro') == 'ofertas':
        productos = Productos.objects.filter(Q(oferta=True),Q(activado = True)).exclude(stock = 0)
        productos = paginador_18(request, productos)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales,})
    else:
        productos = Productos.objects.filter(Q(activado = True)).order_by('-oferta').exclude(stock = 0)
        productos = paginador_18(request, productos)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales,})

def Detalle_Productos(request, id):

    producto = get_object_or_404(Productos, id=id)
    local = get_object_or_404(Local,user = producto.user)

    if producto.activado and producto.stock != 0:
        return render(request, 'cliente/detalle_productos.html',{'object':producto, 'local':local})
    else:
        return redirect('registration:sin_permiso')

def Listado_Locales(request):
    locales = Local.objects.all().order_by('nombre_local')
    locales_ordenados = ordenar_locales(locales)
    objetos = []
    for x in locales_ordenados:
        if x.activado:
            persona = x.user
            premium = Tipo_usuarios.objects.get(user_id = persona)
            productos_vigentes = Productos.objects.filter(Q(user = persona) , Q(activado = True)).exclude(stock = 0).count()
            productos_oferta = Productos.objects.filter(Q(user=persona), Q(activado=True), Q(oferta=True)).exclude(stock=0).count()
            ofertas_locales = Oferta.objects.filter(Q(local=x.id), Q(activado=True)).count()
            try:
                oferta_general = Oferta.objects.get(Q(local=x.id),Q(tipo_oferta='general'),Q(activado=True))
            except:
                oferta_general = None
            diccionario = {}
            diccionario['id']=x.id
            diccionario['user']=x.user
            diccionario['nombre_local']=x.nombre_local
            diccionario['ubicacion_local'] = x.ubicacion_local
            diccionario['imagen_muestra'] = x.imagen_muestra
            diccionario['imagen_banner'] = x.imagen_banner
            diccionario['activado'] = x.activado
            diccionario['tipo_premium'] = premium.tipo_premium
            diccionario['productos'] = productos_vigentes
            diccionario['productos_oferta'] = productos_oferta
            diccionario['numero_ofertas'] = ofertas_locales
            diccionario['oferta_general'] = oferta_general
            objetos.append(diccionario)
    return render(request, 'cliente/listado_locales.html',{'locales':objetos})

def Detalle_Locales(request,id):
    local =get_object_or_404(Local,user=id)
    if local.activado:
        productos_vigentes = Productos.objects.filter(Q(user=id), Q(activado=True)).exclude(stock=0).count()
        productos = Productos.objects.filter(Q(user=id), Q(activado=True), Q(oferta=False)).exclude(
            stock=0).count()
        productos_oferta = Productos.objects.filter(Q(user=id), Q(activado=True), Q(oferta=True)).exclude(
            stock=0).count()
        if productos_vigentes != 0:
            productos_porcentaje = int((productos*100)/productos_vigentes)
            productos_oferta_porcentaje = int((productos_oferta * 100) / productos_vigentes)
        else:
            productos_porcentaje = 0
            productos_oferta_porcentaje = 0

        general = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='general'), Q(activado=True))
        temporada = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='temporada'), Q(activado=True))
        rango_plata = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_plata'), Q(activado=True))
        rango_oro = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_oro'), Q(activado=True))
        rango_diamante = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_diamante'), Q(activado=True))
        convencional = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='convencional'), Q(activado=True))

        dict_productos = {'id':id,'productos_vigentes': productos_vigentes, 'productos':productos,
                          'productos_oferta':productos_oferta,'productos_porcentaje':productos_porcentaje,
                          'productos_oferta_porcentaje':productos_oferta_porcentaje}

        return render(request, 'cliente/detalle_locales.html',{'dict_productos':dict_productos, 'local':local,
                                                               'general': general, 'temporada': temporada,
                                                               'rango_plata': rango_plata, 'rango_oro': rango_oro,
                                                               'rango_diamante': rango_diamante,
                                                               'convencional': convencional,
                                                               })
    else:
        return redirect('registration:sin_permiso')

def Listar_Productos_Tiendas(request, id):

    form = FormCategoria()

    local = get_object_or_404(Local, user=id)
    if local.activado:
        if request.method == 'POST':
            buscar = request.POST.get('buscar', None)
            categoria = request.POST.get('categoria', None)
            if buscar is not None:
                productos = Productos.objects.filter((Q(nombre__contains=buscar) | Q(nombre__icontains=buscar)),
                                                     Q(user=id), Q(activado=True)).order_by('-oferta').exclude(stock=0)
            else:
                productos = Productos.objects.filter(Q(categoria=categoria), Q(activado=True), Q(user=id)).order_by('-oferta').exclude(
                    stock=0)
            productos = paginador_18(request, productos)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
        elif request.GET.get('filtro') == 'ofertas':
            productos = Productos.objects.filter(Q(oferta=True), Q(activado=True), Q(user=id)).exclude(stock=0)
            productos = paginador_18(request, productos)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
        else:
            productos = Productos.objects.filter(Q(activado=True), Q(user=id)).order_by('-oferta').exclude(stock=0)
            productos = paginador_18(request, productos)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
    else:
        return redirect('registration:sin_permiso')

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

#FUNCIONES PERSONALIZADAS

def ordenar_locales(locales):
    locales_ordenados = []
    for x in locales:
        tipo = Tipo_usuarios.objects.get(user_id=x.user.id)
        if tipo.tipo_premium == 3:
            locales_ordenados.append(x)
    for x in locales:
        tipo = Tipo_usuarios.objects.get(user_id=x.user.id)
        if tipo.tipo_premium == 2:
            locales_ordenados.append(x)
    for x in locales:
        tipo = Tipo_usuarios.objects.get(user_id=x.user.id)
        if tipo.tipo_premium == 1:
            locales_ordenados.append(x)
    for x in locales:
        tipo = Tipo_usuarios.objects.get(user_id=x.user.id)
        if tipo.tipo_premium == 0:
            locales_ordenados.append(x)
    return locales_ordenados

def paginador_18(request, productos):
    paginator = Paginator(productos, 18)
    page = request.GET.get('page')
    productos_paginados = paginator.get_page(page)
    return productos_paginados

