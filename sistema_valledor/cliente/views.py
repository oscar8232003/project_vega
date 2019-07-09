from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from .forms import FormCategoria, FormTienda, FormListas, Productos_listas_form
from vendedor.models import Productos, Local, Oferta, Puntos
from registration.models import Tipo_usuarios
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, Max, Min
from .models import Listas, Productos_listas, Reporte_listas, Valorizacion_pedidos
from django.contrib.auth.decorators import login_required
import time, datetime
from datetime import date
from django.http import HttpResponse, Http404

#GENERAR PDFS
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

# Create your views here.
def Panel_Cliente(request, id):

    tipo = buscar_tipo(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and id == request.user.id:
        cliente = get_object_or_404(User,id=id)
        ofertas_generales = Oferta.objects.filter(Q(tipo_oferta='general'), Q(activado=True), Q(local__activado=True)).order_by('local__nombre_local')
        puntos = Puntos.objects.filter(user = request.user.id)

        return render(request, 'cliente/panel_cliente.html',{'cliente':cliente, 'oferta_general':ofertas_generales, 'puntos':puntos })
    else:
        return redirect('registration:sin_permiso')
#Testeada
def Listar_Productos(request):

    form = FormCategoria()
    locales = Local.objects.all()
    pdf_all = request.GET.get('pdf_all', None)
    pdf = request.GET.get('pdf', None)
    buscar = request.GET.get('buscar', None)
    categoria = request.GET.get('categoria', None)
    if categoria:
        try:
            categoria = int(categoria)
            productos = Productos.objects.filter(Q(categoria=categoria), Q(activado=True)).order_by('-oferta').exclude(
                stock=0)
        except:
            productos = None

        if pdf == 'yes':
            prod = convertir_datos_para_pdf(productos)
            return Imprimir_pdf_detalle_productos(prod)
        return render(request, 'cliente/listado_productos.html',
                      {'form_categoria': form, 'productos': productos, 'locales': locales, })
    elif buscar:
        productos = Productos.objects.filter((Q(nombre__contains = buscar)|Q(nombre__icontains = buscar)),Q(activado = True)).order_by('-oferta').exclude(stock = 0)
        if pdf == 'yes':
            prod = convertir_datos_para_pdf(productos)
            return Imprimir_pdf_detalle_productos(prod)
        return render(request, 'cliente/listado_productos.html',
                      {'form_categoria': form, 'productos':productos, 'locales':locales,})
    elif request.GET.get('filtro') == 'ofertas':
        productos = Productos.objects.filter(Q(oferta=True),Q(activado = True)).exclude(stock = 0)
        productos = paginador_propio(request, productos, 18)
        if pdf == 'yes':
            prod = convertir_datos_para_pdf(productos)
            return Imprimir_pdf_detalle_productos(prod)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales,})
    else:
        productos = Productos.objects.filter(Q(activado = True)).order_by('-oferta').exclude(stock = 0)
        productos = paginador_propio(request, productos, 18)
        if pdf_all == 'yes':
            prod = convertir_datos_para_pdf(productos)
            return Imprimir_pdf_detalle_productos(prod)
        return render(request, 'cliente/listado_productos.html', {'form_categoria': form, 'productos': productos, 'locales':locales,})

#verificado
def Detalle_Productos(request, id):

    producto = get_object_or_404(Productos, id=id)
    local = get_object_or_404(Local,user = producto.user)
    tipo_usuario =buscar_tipo(request.user.id)

    if producto.activado and producto.stock != 0:
        form = Productos_listas_form()
        pdf = request.GET.get('pdf', None)
        if pdf == 'yes':
            datos = []
            dic = {}
            dic['nombre']= producto.nombre
            dic['categoria'] = producto.categoria.categoria
            if producto.oferta:
                dic['oferta'] = 'SI'
                dic['precio_oferta'] = producto.precio_oferta
            else:
                dic['oferta'] = 'NO'
                dic['precio_oferta'] = 0
            dic['precio'] = producto.precio
            dic['stock'] = producto.stock
            dic['unidad_medida'] = producto.unidad_medida.medida_plural
            dic['tienda'] = local.nombre_local
            datos.append(dic)
            return Imprimir_pdf_detalle_productos(datos)

        if request.method == 'POST':
            form = Productos_listas_form(request.POST)
            #Validador de datos de inputs hidden
            try:
                id_user = int(request.POST['user'])
                id_producto = int(request.POST['productos'])
                id_local = int(request.POST['local'])
                precio_producto = int(request.POST['precio_producto'])
                id_lista = int(request.POST['lista'])
            except:
                id_user = None
                id_producto = None
                id_local = None
                precio_producto = None
                id_lista = None
            if id_user and id_producto and id_local and precio_producto and id_lista:
                if form.is_valid() and id_user == request.user.id and \
                        id_producto == producto.id and id_local==local.id:
                    if (producto.oferta and precio_producto == producto.precio_oferta) or\
                            (producto.oferta == False and precio_producto == producto.precio):
                        numero_productos = Productos_listas.objects.filter(Q(lista=id_lista)).count()
                        if numero_productos <= 15:
                            numero_repetidos = Productos_listas.objects.filter(Q(lista=id_lista),
                                                                               Q(productos=id_producto)).count()
                            if numero_repetidos <= 5:
                                form.save()
                                prod = Productos.objects.get(id = id_producto)
                                lista = Listas.objects.get(id = id_lista)
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
            else:
                return redirect(reverse('cliente:detalle_productos', args=[id]) + '?msg=form_no_valid')

        listas = Listas.objects.filter(Q(user=request.user.id), Q(estado_lista='normal'), Q(local=local.id))
        return render(request, 'cliente/detalle_productos.html',{'object':producto, 'local':local, 'tipo':tipo_usuario,
                                                                 'form':form, 'listas':listas})
    else:
        return redirect('registration:sin_permiso')

#verificado
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
            valorizacion = Valorizacion_pedidos.objects.filter(local = x.id).aggregate(Suma = Sum('puntuacion'), Total=Count('id'))
            if valorizacion['Total'] > 0:
                valorizacion_total = int(valorizacion['Suma']/valorizacion['Total'])
            else:
                valorizacion_total = None
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
            diccionario['valorizacion'] = valorizacion_total
            objetos.append(diccionario)
    if request.GET.get('pdf', None):
        return Imprimir_pdf_listas(objetos)

    return render(request, 'cliente/listado_locales.html',{'locales':objetos})

#Verificado
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

        valorizacion = Valorizacion_pedidos.objects.filter(local=local.id).aggregate(Suma=Sum('puntuacion'),
                                                                                 Total=Count('id'))
        if valorizacion['Total'] > 0:
            valorizacion_total = int(valorizacion['Suma'] / valorizacion['Total'])
        else:
            valorizacion_total = None

        valorizaciones_de_personas = Valorizacion_pedidos.objects.filter(local=local.id).order_by('-fecha_registro')
        arr_valorizaciones = []
        for x in valorizaciones_de_personas:
            if len(arr_valorizaciones) < 6:
                arr_valorizaciones.append(x)
            else:
                break

        general = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='general'), Q(activado=True))
        temporada = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='temporada'), Q(activado=True))
        rango_plata = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_plata'), Q(activado=True))
        rango_oro = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_oro'), Q(activado=True))
        rango_diamante = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_diamante'), Q(activado=True))
        convencional = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='convencional'), Q(activado=True))
        total_ofertas = Oferta.objects.filter(Q(local=local.id), Q(activado=True)).count()

        dict_productos = {'id':id,'productos_vigentes': productos_vigentes, 'productos':productos,
                          'productos_oferta':productos_oferta,'productos_porcentaje':productos_porcentaje,
                          'productos_oferta_porcentaje':productos_oferta_porcentaje, 'valorizacion':valorizacion_total}

        return render(request, 'cliente/detalle_locales.html',{'dict_productos':dict_productos, 'local':local,
                                                               'general': general, 'temporada': temporada,
                                                               'rango_plata': rango_plata, 'rango_oro': rango_oro,
                                                               'rango_diamante': rango_diamante,
                                                               'convencional': convencional, 'valoraziones':arr_valorizaciones
                                                               })
    else:
        return redirect('registration:sin_permiso')

#Verificado
#Se tiene que agregar los reportes en pdf y cambiar los forms por GET
def Listar_Productos_Tiendas(request, id):
    form = FormCategoria()
    local = get_object_or_404(Local, user=id)

    if local.activado:
        buscar = request.GET.get('buscar', None)
        categoria = request.GET.get('categoria', None)
        pdf = request.GET.get('pdf', None)
        if buscar:
            productos = Productos.objects.filter((Q(nombre__contains=buscar) | Q(nombre__icontains=buscar)),
                                                     Q(user=id), Q(activado=True)).order_by('-oferta').exclude(stock=0)
            if pdf == 'yes':
                prod = convertir_datos_para_pdf(productos)
                return Imprimir_pdf_detalle_productos(prod)
            productos = paginador_propio(request, productos, 8)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})

        elif categoria:

            try:
                categoria = int(categoria)
            except:
                categoria = None

            if categoria:
                productos = Productos.objects.filter(Q(categoria=categoria), Q(activado=True), Q(user=id)).order_by('-oferta').exclude(
                stock=0)
                if pdf == 'yes':
                    prod = convertir_datos_para_pdf(productos)
                    return Imprimir_pdf_detalle_productos(prod)
                productos = paginador_propio(request, productos, 8)
                return render(request, 'cliente/listar_productos_tiendas.html',
                              {'form_categoria': form, 'productos': productos, 'local': local})
            else:
                productos = Productos.objects.filter(Q(activado=True), Q(user=id)).order_by('-oferta').exclude(stock=0)
                if pdf == 'yes':
                    prod = convertir_datos_para_pdf(productos)
                    return Imprimir_pdf_detalle_productos(prod)
                return render(request, 'cliente/listar_productos_tiendas.html',
                              {'form_categoria': form, 'productos': productos, 'local': local})

        elif request.GET.get('filtro') == 'ofertas':
            productos = Productos.objects.filter(Q(oferta=True), Q(activado=True), Q(user=id)).exclude(stock=0)
            productos = paginador_propio(request, productos, 18)
            if pdf == 'yes':
                prod = convertir_datos_para_pdf(productos)
                return Imprimir_pdf_detalle_productos(prod)
            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
        else:
            productos = Productos.objects.filter(Q(activado=True), Q(user=id)).order_by('-oferta').exclude(stock=0)
            productos = paginador_propio(request, productos, 18)

            if pdf == 'yes':
                prod = convertir_datos_para_pdf(productos)
                return Imprimir_pdf_detalle_productos(prod)

            return render(request, 'cliente/listar_productos_tiendas.html',
                          {'form_categoria': form, 'productos': productos, 'local': local})
    else:
        return redirect('registration:sin_permiso')

#Verficada
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
                try:
                    tienda = int(tienda)
                except:
                    tienda = None
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

#Verificada
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
            valorizar = request.POST.get('valorizar', None)

            #Logica para el guardar los productos seleccionados
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

            #Logica para la valorizacion
            elif valorizar:
                valor = request.POST.get('valor', None)
                if valor != '':
                    comentarios = request.POST.get('comentarios_valorizacion', None)
                    try:
                        valor = int(valor)
                    except:
                        valor = None
                    if valor == 1 or valor == 2 or valor == 3 or valor == 4 or valor == 5:
                        cliente = User.objects.get(id=lista.user.id)
                        lista_valorizacion = lista.id
                        puntuacion = valor
                        local = Local.objects.get(id= lista.local.id)
                        fecha_registro = date.today()
                        comentarios = comentarios
                        Valorizacion_pedidos.objects.create(user=cliente, lista=lista_valorizacion, local=local,
                                                            puntuacion=puntuacion, fecha_registro=fecha_registro,
                                                            comentarios=comentarios)
                        cambiar_lista = Listas.objects.get(id = lista.id)
                        cambiar_lista.valorizacion = True
                        cambiar_lista.save()
                        return redirect(reverse('cliente:detalle_lista_ok', args=[id]))
                    else:
                        mensaje_error = "Debe seleccionar un valor valido de las opciones de valorizacion"
                        return render(request, 'cliente/detalle_lista.html',
                                      {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                                       'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                                       'mensaje_error': mensaje_error})
                else:
                    mensaje_error = "Debe seleccionar un valor valido de las opciones de valorizacion"
                    return render(request, 'cliente/detalle_lista.html',
                                  {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                                   'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                                   'mensaje_error': mensaje_error})

            elif mandar_pedido:
                #Validaciones de productos
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
                        mensaje = "El producto {}, no tiene stock para la cantidad que desea, actualmente quedan {} {} " \
                                  "modifique la cantidad del producto o eliminelo de la lista para continuar"\
                            .format(producto.productos.nombre, producto.productos.stock, producto.productos.unidad_medida.medida_plural)
                        mensaje_error.append(mensaje)

                if productos_lista.count() == 0:
                    mensaje = "El pedido debe tener almenos 1 producto para poder enviar la lista"
                    mensaje_error.append(mensaje)

                if lista.estado_lista != 'normal':
                    mensaje = "La Lista debe de estar en estado normal para enviarla, sino no se puede enviar el pedido"
                    mensaje_error.append(mensaje)

                #Verificar si hay mas de 1 lista enviada
                contador_de_listas = Listas.objects.filter(Q(local=lista.local.id), Q(user=request.user.id),
                                                           (Q(estado_lista='enviada') | Q(
                                                               estado_lista='armando_pedido'))).count()

                #Verificar si hay mas de 2 listas en espera de retiro
                contador_de_listas_espera = Listas.objects.filter(Q(local=lista.local.id), Q(user=request.user.id),
                                                                  Q(estado_lista='lista_retiro')).count()

                if contador_de_listas > 0:
                    mensaje = "Ya hay un pedido enviado o en proceso de armado, debe esperar a que ese pedido este listo para retirar " \
                              "para poder realizar otro pedido"
                    mensaje_error.append(mensaje)

                if contador_de_listas_espera > 1:
                    mensaje = "Ya hay 2 pedidos listos para retirar, debe retirar esos pedidos o esperar a que ese pedido finalize " \
                              "para poder realizar otro pedido"
                    mensaje_error.append(mensaje)

                #Se verifica si no hay errores, se marca la lista enviada y la fecha de envio.
                #Se marca cada producto en 0 y la oferta igual, se disminuye 1 punto las veces que se pueden cambiar
                if len(mensaje_error) == 0:
                    lista.estado_lista = 'enviada'
                    lista.fecha_enviado = time.strftime("%Y-%m-%d")
                    lista.save()
                    for producto in productos_lista:
                        producto.producto_marcado = 0
                        if producto.productos.oferta:
                            producto.oferta = 1
                        else:
                            producto.oferta = 0
                        producto.save()
                        producto_cambiar = Productos.objects.get(id=producto.productos.id)
                        producto_cambiar.stock -=producto.cantidad
                        producto_cambiar.save()
                    mensaje_ok = "La lista a sido enviada, su pedido sera revisado y procesado lo antes posible."
                    return render(request, 'cliente/detalle_lista.html',
                                  {'lista': lista, 'productos': productos_lista, 'total_aprox': total_lista_aprox,
                                   'tipo': tipo, 'total_marcado': total_lista_seleccionados,
                                   'mensaje_error': mensaje_error,'mensaje_ok': mensaje_ok})

            #Logica para cancelar el pedido
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

            #Logica para volver a estado normal el pedido
            elif volver_normal == 'cambiar_normal_completada':
                if lista.estado_lista == 'completada':
                    lista.estado_lista = 'normal'
                    lista.cancelaciones = 5
                    lista.valorizacion = False
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
                    mensaje_ok = "La lista volvio a el estado normal, el no retiro de los pedidos puede resultar con " \
                                 "penalizaciones para el cliente"

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

#Verficado
#Problema del form por defecto
@login_required(redirect_field_name='login')
def Agregar_Listas(request):

    tipo = buscar_tipo(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'cliente':
        form = FormListas()
        tiendas = Local.objects.all()
        if request.method == 'POST':
            form = FormListas(request.POST)
            try:
                id_persona = int(request.POST.get('user', None))
            except:
                id_persona = None
            if form.is_valid() and request.user.id == id_persona:
                form.save()
                return redirect(reverse('cliente:mis_listas', args=[request.user.id])+'?msg=form_ok')
            else:
                return redirect(reverse('cliente:agregar_lista', args=[request.user.id]) + '?msg=form_no_valid')
        return render(request, 'cliente/agregar_lista.html',{'form':form, 'tiendas':tiendas})
    else:
        return redirect('registration:sin_permiso')

#Verficado
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

#Verficiado
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

#Verificado
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

#Verificado
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

#Verficiado
#Seccion de Reportes
@login_required(redirect_field_name='login')
def Seleccion_Reportes(request, id_user):
    return render(request, 'cliente/seleccion_reportes.html', )

#Verficiado
#Reportes de pedidos para clientes
@login_required(redirect_field_name='login')
def Reporte_Pedidos(request, id_user):
    tipo = buscar_tipo(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'cliente' and request.user.id == id_user:
        diccionario_datos = {}
        tiendas_id = Reporte_listas.objects.filter(Q(cliente=request.user.id)).values('local').distinct()
        ##Agregar tiendas al sistema
        arr_tiendas = []
        for x in tiendas_id:
            dic_tiendas = {}
            temp = ""
            try:
                temp = Local.objects.get(id=x['local'])
            except:
                temp = None
            if temp:
                temp = {'id':x['local'], 'nombre_local':temp.nombre_local}
                arr_tiendas.append(temp)
        diccionario_datos['tiendas'] = arr_tiendas

        ##Total de pedidos, totales desde 0
        total = Reporte_listas.objects.filter(Q(cliente=request.user.id)).aggregate(total=Count('id'))
        total = total['total']
        diccionario_datos['total_pedidos'] = total
        if total > 0:
            diccionario_datos['total_pedidos_porcentaje'] = 100
        else:
            diccionario_datos['total_pedidos_porcentaje'] = 0

        ##Pedidos completados
        total_completados = Reporte_listas.objects.filter(Q(cliente=request.user.id), Q(estado='completada')). \
            aggregate(total_completados=Count('id'))
        total_completados = total_completados['total_completados']
        diccionario_datos['total_completados'] = total_completados
        diccionario_datos['total_completados_porcentaje'] = int((total_completados * 100) / total)

        ##Pedidos Cancelados
        total_cancelados = Reporte_listas.objects.filter(Q(cliente=request.user.id), Q(estado='cancelada')). \
            aggregate(total_canceladas=Count('id'))
        total_cancelados = total_cancelados['total_canceladas']
        diccionario_datos['total_cancelados'] = total_cancelados
        diccionario_datos['total_cancelados_porcentaje'] = int((total_cancelados * 100) / total)

        ##Pedidos No retirados
        total_no_retirados = Reporte_listas.objects.filter(Q(cliente=request.user.id), Q(estado='no_retirada')). \
            aggregate(total_no_retirada=Count('id'))
        total_no_retirados = total_no_retirados['total_no_retirada']
        diccionario_datos['total_no_retirados'] = total_no_retirados
        diccionario_datos['total_no_retirados_porcentaje'] = int((total_no_retirados * 100) / total)

        ##Veces compradas en cada tienda con el total, en el año actual
        arr_tienda_total = []
        for x in tiendas_id:
            info_tienda = {}
            try:
                temp = Local.objects.get(id=x['local'])
                suma = Reporte_listas.objects.filter(Q(cliente=request.user.id),Q(local__id=x['local']),
                                                     Q(estado='completada'), Q(fecha_registro__year=date.today().year)).\
                                                     aggregate(veces_compradas=Count('id'), total=Sum('total'))
            except:
                temp = None
                suma = None
            if temp and suma:
                info_tienda = {'tienda':temp.nombre_local, 'cantidad': suma['veces_compradas'], 'total':suma['total']}
                arr_tienda_total.append(info_tienda)
        diccionario_datos['veces_compradas_total'] = arr_tienda_total

        ##Compras mensuales del año actual
        año_actual = date.today().year
        compras_meses=[]
        for x in range(1,13):
            dic_meses = {}
            total_mes = Reporte_listas.objects.filter(Q(cliente=request.user.id),Q(fecha_registro__month=x),
                        Q(fecha_registro__year=año_actual)).aggregate(total_dinero=Sum('total'),
                                                                      total_productos=Sum('cantidad_productos'),
                                                                      total_items=Sum('cantidad_items'))
            mes = traer_mes(x)
            dic_meses = {'mes':mes, 'total_dinero':total_mes['total_dinero'], 'total_productos':total_mes['total_productos'],
                         'total_items':total_mes['total_items']}
            compras_meses.append(dic_meses)
        diccionario_datos['compras_mensuales'] = compras_meses

        ##Filtros
        if request.method == 'POST':
            buscar_tienda = request.POST.get('buscar_tienda', None)
            buscar_estado = request.POST.get('buscar_estado', None)
            buscar_fecha = request.POST.get('buscar_fecha', None)

            #Buscar la informacion de la tienda, del año actual
            if buscar_tienda:
                buscado = request.POST.get('tienda',None)
                try:
                    buscado = int(buscado)
                    temp = Local.objects.get(id=buscado)
                except:
                    buscado = None
                if buscado:
                    query = Reporte_listas.objects.filter(Q(cliente=request.user.id), Q(local=buscado),
                                                          Q(fecha_registro__year=date.today().year))
                    criterio = "Local {}".format(temp.nombre_local)
                    return render(request, 'cliente/reporte_pedidos.html',
                                  {'dic_datos': diccionario_datos, 'datos': query, 'criterio': criterio, 'titulo':criterio})
                else:
                    raise Http404

            #Busca los pedidos con el estado correspondiente, del año actual
            elif buscar_estado:
                buscado = request.POST.get('estado', None)
                query = Reporte_listas.objects.filter(Q(cliente=request.user.id), Q(estado=buscado),
                                                      Q(fecha_registro__year=date.today().year))
                criterio = "Pedidos {}".format(convertir_estado(buscado))
                return render(request, 'cliente/reporte_pedidos.html',
                              {'dic_datos': diccionario_datos, 'datos': query, 'criterio': criterio, 'titulo':criterio})

            #Buscar pedidos por fechas
            elif buscar_fecha:
                buscado1 = request.POST.get('fecha_inicio', None)
                buscado2 = request.POST.get('fecha_final', None)
                try:
                    buscado1 = datetime.datetime.strptime(buscado1, '%Y-%m-%d')
                    buscado1 = buscado1.date()

                    buscado2 = datetime.datetime.strptime(buscado2, '%Y-%m-%d')
                    buscado2 = buscado2.date()
                except:
                    buscado1 = None
                    buscado2 = None
                if buscado1 and buscado2:
                    query = None
                    mensaje_error = None
                    criterio = None
                    if buscado1 <= buscado2:
                        query = Reporte_listas.objects.filter(fecha_registro__range=(buscado1, buscado2))
                        criterio = "Datos desde {} hasta el {}".format(buscado1, buscado2)
                    else:
                        mensaje_error = "La fecha de inicio no puede ser mayor a la fecha final"

                    return render(request, 'cliente/reporte_pedidos.html',
                                  {'dic_datos':diccionario_datos, 'datos':query,'criterio':criterio, 'mensaje_error':
                                   mensaje_error})
                else:
                    raise Http404
        else:
            query = Reporte_listas.objects.filter(Q(cliente=request.user.id), Q(fecha_registro__month= date.today().month))
            titulo = "Pedidos del mes de {}".format(traer_mes(date.today().month))
            return render(request, 'cliente/reporte_pedidos.html',{'dic_datos':diccionario_datos, 'datos':query,
                                                                   'titulo':titulo})
    else:
        return redirect('registration:sin_permiso')


#FUNCIONES PERSONALIZADAS
def convertir_estado(estado):
    estado_final=None
    if estado == 'completada':
        estado_final="Completado"
    elif estado == 'no_retirada':
        estado_final = "No Retirado"
    elif estado == 'cancelada':
        estado_final = "Cancelado"
    return estado_final

def traer_mes(mes):
    mes_literal = None
    if mes ==1:
        mes_literal="Enero"
    elif mes == 2:
        mes_literal = "Febrero"
    elif mes == 3:
        mes_literal = "Marzo"
    elif mes == 4:
        mes_literal = "Abril"
    elif mes == 5:
        mes_literal = "Mayo"
    elif mes == 6:
        mes_literal = "Junio"
    elif mes == 7:
        mes_literal = "Julio"
    elif mes == 8:
        mes_literal = "Agosto"
    elif mes == 9:
        mes_literal = "Septiembre"
    elif mes == 10:
        mes_literal = "Octubre"
    elif mes == 11:
        mes_literal = "Noviembre"
    elif mes == 12:
        mes_literal = "Diciembre"
    return mes_literal

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
    x=0
    try:
        x = int(numero)
    except:
        x = None
    return x

def Imprimir_pdf_detalle_productos(datos):
    response = HttpResponse(content_type='application/pdf')
    #este es para descarga directa
    #response['Content-Disposition']= 'attachment; filename= TuVegaApp Reporte de Usuarios Premium.pdf'
    response['Content-Disposition'] = 'attachment;filename= cotizacion de producto.pdf'
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=60,
                            bottomMargin=18,)
    premium = []
    imagen = Image('media/core/Logo.webp', width=201, height=44)
    premium.append(imagen)
    styles = getSampleStyleSheet()
    header = Paragraph("Cotizacion de producto", styles['Heading2'])
    premium.append(header)

    headings = ('Nombre', 'Categoria', 'Oferta', Paragraph('Precio Oferta', styles['Normal']), 'Precio', 'Stock', 'Tienda', 'Medida')
    Datos = [(Paragraph(x['nombre'], styles['Normal']),Paragraph(x['categoria'], styles['Normal']), x['oferta'],
              x['precio_oferta'], x['precio'], x['stock'], Paragraph(x['tienda'], styles['Normal']),
              Paragraph(x['unidad_medida'], styles['Normal']))
                       for x in datos]
    t = Table([headings]+Datos, colWidths=[70,62,56,46,46,56,56,56])

    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (7, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ]
    ))

    premium.append(t)
    doc.build(premium)
    response.write(buff.getvalue())
    buff.close()

    return response

def convertir_datos_para_pdf(datos):
    arr = []
    for x in datos:
        dic = {}
        dic['nombre'] = x.nombre
        dic['categoria'] = x.categoria.categoria
        if x.oferta:
            dic['oferta'] = 'SI'
            dic['precio_oferta'] = x.precio_oferta
        else:
            dic['oferta'] = 'NO'
            dic['precio_oferta'] = 0
        dic['precio'] = x.precio
        dic['stock'] = x.stock
        dic['unidad_medida'] = x.unidad_medida.medida_plural
        nombre_local = ""
        for y in Local.objects.all():
            if y.user.id == x.user.id:
                nombre_local = y.nombre_local
                break
        dic['tienda'] = nombre_local
        arr.append(dic)
    return arr

def Imprimir_pdf_listas(datos):
    response = HttpResponse(content_type='application/pdf')
    #este es para descarga directa
    #response['Content-Disposition']= 'attachment; filename= TuVegaApp Reporte de Usuarios Premium.pdf'
    response['Content-Disposition'] = 'attachment; filename= cotizacion de producto.pdf'
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=60,
                            bottomMargin=18,)
    premium = []
    imagen = Image('media/core/Logo.webp', width=201, height=44)
    premium.append(imagen)
    styles = getSampleStyleSheet()
    header = Paragraph("Cotizacion de Locales", styles['Heading2'])
    premium.append(header)

    headings = (Paragraph('Nombre Local', styles['Normal']), Paragraph('Ubicacion Local', styles['Normal']),
                Paragraph('Productos vigentes', styles['Normal']), Paragraph('Productos en Oferta', styles['Normal']),
                Paragraph('Numero de Ofertas', styles['Normal']))
    Datos = [(Paragraph(x['nombre_local'], styles['Normal']),Paragraph(x['ubicacion_local'], styles['Normal']), x['productos'],
              x['productos_oferta'], x['numero_ofertas'])
                       for x in datos]
    t = Table([headings]+Datos, colWidths=[91,91,91,91,91])

    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (7, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ]
    ))

    premium.append(t)
    doc.build(premium)
    response.write(buff.getvalue())
    buff.close()

    return response
