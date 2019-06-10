from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from .forms import FormCategoria, FormTienda, FormListas, Productos_listas_form
from vendedor.models import Productos, Local, Oferta
from registration.models import Tipo_usuarios
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Listas, Productos_listas
from django.contrib.auth.decorators import login_required
import time
# Create your views here.
def Panel_Cliente(request, id):

    tipo = buscar_tipo(request.user.id)
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
        productos = paginador_propio(request, productos, 18)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales,})
    else:
        productos = Productos.objects.filter(Q(activado = True)).order_by('-oferta').exclude(stock = 0)
        productos = paginador_propio(request, productos, 18)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales,})

def Detalle_Productos(request, id):

    producto = get_object_or_404(Productos, id=id)
    local = get_object_or_404(Local,user = producto.user)
    tipo_usuario =buscar_tipo(request.user.id)

    if producto.activado and producto.stock != 0:
        form = Productos_listas_form()
        if request.method == 'POST':
            form = Productos_listas_form(request.POST)
            #Validador de datos de inputs hidden
            if form.is_valid() and int(request.POST['user']) == request.user.id and \
                    int(request.POST['productos']) == producto.id and int(request.POST['local'])==local.id:
                if (producto.oferta and int(request.POST['precio_producto']) == producto.precio_oferta) or\
                        (producto.oferta == False and int(request.POST['precio_producto']) == producto.precio):
                    numero_productos = Productos_listas.objects.filter(Q(lista=int(request.POST['lista']))).count()
                    if numero_productos <= 15:
                        numero_repetidos = Productos_listas.objects.filter(Q(lista=int(request.POST['lista'])),
                                                                           Q(productos=int(request.POST['productos']))).count()
                        if numero_repetidos <= 5:
                            form.save()
                            prod = Productos.objects.get(id=int(request.POST['productos']))
                            lista = Listas.objects.get(id = int(request.POST['lista']))
                            if prod.oferta:
                                try:
                                    lista.total+=prod.precio_oferta*int(request.POST['cantidad'])
                                    lista.save()
                                except:
                                    pass
                            else:
                                try:
                                    lista.total+=prod.precio*int(request.POST['cantidad'])
                                    lista.save()
                                except:
                                    pass
                            return redirect(reverse('cliente:detalle_productos', args=[id])+'?msg=form_ok')
                        else:
                            return redirect(reverse('cliente:detalle_productos', args=[id]) + '?msg=error_duplicado')
                    else:
                        return redirect(reverse('cliente:detalle_productos', args=[id]) + '?msg=error_cantidad')
                else:
                    return redirect(reverse('cliente:detalle_productos', args=[id]) + '?msg=form_no_valid')
            else:
                return redirect(reverse('cliente:detalle_productos', args=[id])+'?msg=form_no_valid')

        listas = Listas.objects.filter(Q(user=request.user.id), Q(estado_lista='normal'), Q(local=local.id))
        return render(request, 'cliente/detalle_productos.html',{'object':producto, 'local':local, 'tipo':tipo_usuario,                                                               'form':form, 'listas':listas})
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
            productos = paginador_propio(request, productos, 8)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
        elif request.GET.get('filtro') == 'ofertas':
            productos = Productos.objects.filter(Q(oferta=True), Q(activado=True), Q(user=id)).exclude(stock=0)
            productos = paginador_propio(request, productos, 18)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
        else:
            productos = Productos.objects.filter(Q(activado=True), Q(user=id)).order_by('-oferta').exclude(stock=0)
            productos = paginador_propio(request, productos, 18)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Mis_Listas(request, id):

    tipo = buscar_tipo(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and id == request.user.id:
        form = FormTienda()
        listas = Listas.objects.filter(Q(user = request.user.id)).order_by('-fecha_actualizacion')
        listas = paginador_propio(request, listas, 8)
        if request.method == 'POST':
            buscar = request.POST.get('buscar', None)
            tienda = request.POST.get('local', None)
            if buscar is not None:
                listas = Listas.objects.filter(Q(user = request.user.id), (Q(nombre__contains = buscar)|Q(nombre__icontains = buscar))).order_by('-fecha_actualizacion')
            else:
                listas = Listas.objects.filter(Q(user=request.user.id),Q(local=tienda)).order_by('-fecha_actualizacion')
        elif request.GET.get('estado_lista'):
            filtro = request.GET.get('estado_lista')
            if filtro == 'normal':
                listas = buscar_lista(request,'normal')
            elif filtro == 'enviada':
                listas = buscar_lista(request,'enviada')
            elif filtro == 'armando_pedido':
                listas = buscar_lista(request,'armando_pedido')
            elif filtro == 'lista_retiro':
                listas = buscar_lista(request,'lista_retiro')
            elif filtro == 'cancelada':
                listas = buscar_lista(request,'cancelada')
            elif filtro == 'no_retirada':
                listas = buscar_lista(request,'no_retirada')
            elif filtro == 'completada':
                listas = buscar_lista(request,'completada')
        return render(request, 'cliente/mis_listas.html',{'listas':listas, 'form':form})
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Detalle_Listas(request,id):

    tipo = buscar_tipo(request.user.id)
    lista = get_object_or_404(Listas, id=id)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and lista.user.id == request.user.id:
        productos_lista = Productos_listas.objects.filter(Q(user = request.user.id), Q(lista=id))
        total_lista_aprox = 0
        total_lista_seleccionados = 0
        mensaje_error = []
        mensaje_ok = 0
        for productos in productos_lista:
            total_lista_aprox+=int(productos.cantidad*productos.precio_producto)
            if productos.producto_marcado:
                total_lista_seleccionados+=int(productos.cantidad*productos.precio_producto)
        lista.total_marcado=total_lista_seleccionados
        lista.save()
        if request.method == 'POST':
            mandar_pedido = request.POST.get('hacer_pedido', None)
            cancelar_pedido = request.POST.get('cancelar_pedido', None)
            guardar_marcado = request.POST.get('Guardar_progreso', None)
            volver_normal = request.POST.get('cambiar_normal', None)
            if guardar_marcado:
                for producto in productos_lista:
                    producto.producto_marcado = 0
                    producto.save()
                if len(request.POST) > 2:
                    for objeto in request.POST.keys():
                        if objeto != 'csrfmiddlewaretoken' and objeto!= 'Guardar_progreso':
                            try:
                                x = Productos_listas.objects.get(id = objeto)
                                x.producto_marcado = 1
                                x.save()
                            except:
                                pass
                return redirect(reverse('cliente:detalle_lista_ok', args=[id]))
            elif mandar_pedido:
                for producto in productos_lista:
                    if not producto.productos.activado:
                        mensaje = "El producto {}, no se encuentra disponible, para realizar el pedido debe eliminar " \
                                  "este producto de la lista".format(producto.productos.nombre)
                        mensaje_error.append(mensaje)

                    elif producto.productos.oferta and producto.precio_producto != producto.productos.precio_oferta:
                        mensaje = "El producto {}, no se encuentra disponible el producto con el precio de oferta, para realizar el pedido debe eliminar " \
                                  "este producto de la lista y volver a agregarlo".format(producto.productos.nombre)
                        mensaje_error.append(mensaje)

                    elif not producto.productos.oferta and producto.precio_producto != producto.productos.precio:
                        mensaje = "El producto {}, no se encuentra disponible el producto con el precio original, este ha sido cambiado, para realizar el pedido debe eliminar " \
                                  "este producto de la lista y volver a agregarlo".format(producto.productos.nombre)
                        mensaje_error.append(mensaje)

                    elif producto.productos.maximo_prod_comprar < producto.cantidad:
                        mensaje = "El producto {}, supero la cantidad maxima de compra por item, el maximo a comprar por item es de {}" \
                                  ", modifique la cantidad del producto o eliminelo de la lista para continuar, si desea una cantidad mas elevada " \
                                  "agregue otra vez el producto con el stock permitido, tiene para repertir este producto como maximo 5 veces."\
                            .format(producto.productos.nombre, producto.productos.maximo_prod_comprar)
                        mensaje_error.append(mensaje)

                    elif producto.productos.stock < producto.cantidad:
                        mensaje = "El producto {}, no tiene stock para la cantidad que desea, actualmente quedan {} {}" \
                                  "modifique la cantidad del producto o eliminelo de la lista para continuar"\
                            .format(producto.productos.nombre, producto.productos.stock, producto.productos.unidad_medida.medida_plural)
                        mensaje_error.append(mensaje)

                if productos_lista.count() == 0:
                    mensaje = "El pedido debe tener almenos 1 producto para poder enviar la lista"
                    mensaje_error.append(mensaje)

                if len(mensaje_error) == 0:
                    lista.estado_lista = 'enviada'
                    lista.fecha_enviado = time.strftime("%Y-%m-%d")
                    lista.save()
                    for producto in productos_lista:
                        producto.producto_marcado = 0
                        producto.save()
                        producto_cambiar = Productos.objects.get(id=producto.productos.id)
                        producto_cambiar.stock -=producto.cantidad
                        producto_cambiar.save()
                    mensaje_ok = "La lista a sido enviada, su pedido sera revisado y procesado lo antes posible."
                    return render(request, 'cliente/detalle_lista.html',
                                  {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                                   'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                                   'mensaje_error': mensaje_error,'mensaje_ok': mensaje_ok})
            elif cancelar_pedido:
                if lista.estado_lista == 'enviada':
                    lista.estado_lista = 'normal'
                    if lista.cancelaciones != 0:
                        lista.cancelaciones -=1
                    lista.save()
                    for producto in productos_lista:
                        producto_cambiar = Productos.objects.get(id=producto.productos.id)
                        producto_cambiar.stock += producto.cantidad
                        producto_cambiar.save()
                    mensaje_ok = "La lista a sido cancelada, puede volver a enviarla cuando desee."

                else:
                    mensaje = "El pedido debe estar en estado enviado para poder volverlo a estado normal"
                    mensaje_error.append(mensaje)

                return render(request, 'cliente/detalle_lista.html',
                              {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                               'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                               'mensaje_error': mensaje_error, 'mensaje_ok': mensaje_ok})

            elif volver_normal == 'cambiar_normal_completada':
                if lista.estado_lista == 'completada':
                    lista.estado_lista = 'normal'
                    lista.cancelaciones = 5
                    lista.save()
                    mensaje_ok = "La lista volvio a el estado normal, gracias por su preferencia!"

                else:
                    mensaje = "El pedido debe estar en estado completado para poder volverlo a estado normal"
                    mensaje_error.append(mensaje)

                return render(request, 'cliente/detalle_lista.html',
                              {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                               'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                               'mensaje_error': mensaje_error, 'mensaje_ok': mensaje_ok})

            elif volver_normal == 'cambiar_normal_no_retirada':
                if lista.estado_lista == 'no_retirada':
                    lista.estado_lista = 'normal'
                    lista.save()
                    mensaje_ok = "La lista volvio a el estado normal, el no retiro de los pedidos puede resultar con penalizaciones para el cliente"

                else:
                    mensaje = "El pedido debe estar en estado no retirado para poder volverlo a estado normal"
                    mensaje_error.append(mensaje)

                return render(request, 'cliente/detalle_lista.html',
                              {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                               'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                               'mensaje_error': mensaje_error, 'mensaje_ok': mensaje_ok})

            elif volver_normal == 'cambiar_normal_cancelada':
                if lista.estado_lista == 'cancelada':
                    lista.estado_lista = 'normal'
                    lista.save()
                    mensaje_ok = "La lista volvio a el estado normal, el cancelamiento de un pedido se puede deber a varias razones."

                else:
                    mensaje = "El pedido debe estar en estado cancelada para poder volverlo a estado normal"
                    mensaje_error.append(mensaje)

                return render(request, 'cliente/detalle_lista.html',
                              {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                               'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                               'mensaje_error': mensaje_error, 'mensaje_ok': mensaje_ok})

        return render(request, 'cliente/detalle_lista.html',{'lista':lista,'productos':productos_lista,'total_aprox':total_lista_aprox,
                                                             'tipo':tipo, 'total_marcado':total_lista_seleccionados,
                                                             "mensaje_error":mensaje_error})
    else:
        return redirect('registration:sin_permiso')


def Detalle_lista_success(request, id):
    return render(request, 'cliente/verificar_marcado_detalle_listas.html', {'id':id})

@login_required(redirect_field_name='login')
def Agregar_Listas(request):

    tipo = buscar_tipo(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'cliente':
        form = FormListas()
        tiendas = Local.objects.all()
        if request.method == 'POST':
            form = FormListas(request.POST)
            id_persona = int(request.POST.get('user', None))
            if form.is_valid() and request.user.id == id_persona:
                form.save()
                return redirect(reverse('cliente:mis_listas', args=[request.user.id])+'?msg=form_ok')
            else:
                return redirect(reverse('cliente:agregar_lista', args=[request.user.id]) + '?msg=form_no_valid')
        return render(request, 'cliente/agregar_lista.html',{'form':form, 'tiendas':tiendas})
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Actualizar_Listas(request, id):

    tipo = buscar_tipo(request.user.id)
    lista = get_object_or_404(Listas, id=id)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and lista.user.id == request.user.id:
        form = FormListas(instance=lista)
        if request.method == 'POST':
            lista.nombre = request.POST.get('nombre')
            lista.comentario_cliente = request.POST.get('comentario_cliente')
            lista.save()
            if request.GET.get('msg', None) == 'act_lista':
                return redirect(reverse('cliente:detalle_listas', args=[id]) + '?msg=act_ok')
            else:
                return redirect(reverse('cliente:mis_listas', args=[request.user.id])+'?msg=act_ok')
        return render(request, 'cliente/actualizar_listas.html',{'form':form, 'id_lista':id})
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Eliminar_Listas(request, id):

    tipo = buscar_tipo(request.user.id)
    lista = get_object_or_404(Listas, id=id)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and lista.user.id == request.user.id:
        if request.method == 'POST':
            if lista.delete():
                productos = Productos_listas.objects.filter(Q(lista=id))
                for prod in productos:
                    prod.delete()
                return redirect(reverse('cliente:mis_listas', args=[request.user.id]) + '?msg=elim_ok')
            else:
                return redirect(reverse('cliente:eliminar_lista', args=[id]) + '?msg=elim_error')
        return render(request, 'cliente/eliminar_lista.html',{'lista':lista})
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Eliminar_Productos_Listas(request, id_lista, id_prod):

    tipo = buscar_tipo(request.user.id)
    lista = get_object_or_404(Listas, id=id_lista)
    producto = get_object_or_404(Productos_listas, id=id_prod)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and lista.user.id == request.user.id:
        if request.method == 'POST':
            lista.total -= producto.cantidad * producto.precio_producto
            if producto.delete():
                lista.save()
                return redirect(reverse('cliente:detalle_listas', args=[id_lista])+'?msg=elim_ok')
            else:
                return redirect(reverse('cliente:detalle_listas', args=[id_lista])+'?msg_error=elim_error')
        return render(request, 'cliente/eliminar_producto_lista.html',{'producto':producto, 'id_lista':id_lista})
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Actualizar_Productos_Listas(request, id_lista, id_prod):

    tipo = buscar_tipo(request.user.id)
    lista = get_object_or_404(Listas, id=id_lista)
    producto = get_object_or_404(Productos_listas, id=id_prod)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and lista.user.id == request.user.id:
        if request.method == 'POST':
            cantidad = request.POST.get('stock')
            cantidad = convertidor_numero(cantidad)
            if cantidad is not None:
                lista.total -= producto.cantidad * producto.precio_producto
                producto.cantidad = cantidad
                producto.comentarios = request.POST.get('comentarios')
                producto.save()
                lista.total += cantidad * producto.precio_producto
                lista.save()
                return redirect(reverse('cliente:detalle_listas', args=[id_lista]) + '?msg=act_ok_prod')
            else:
                return redirect(reverse('cliente:actualizar_producto_lista', args=[id_lista, id_prod]) + '?msg=act_error')
        return render(request, 'cliente/actualizar_producto_lista.html',{'lista':lista, 'producto':producto})
    else:
        return redirect('registration:sin_permiso')


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

def paginador_propio(request, productos, cantidad):
    paginator = Paginator(productos, cantidad)
    page = request.GET.get('page')
    productos_paginados = paginator.get_page(page)
    return productos_paginados

def buscar_lista(request,estado):
    listas = Listas.objects.filter(Q(user=request.user.id), Q(estado_lista=estado)).order_by(
        '-fecha_actualizacion')
    return listas

def buscar_tipo(id):
    try:
        tipo = Tipo_usuarios.objects.get(user_id=id)
    except:
        tipo = None
    return tipo

def convertidor_numero(numero):
    try:
        x = int(numero)
    except:
        x = None
    return x