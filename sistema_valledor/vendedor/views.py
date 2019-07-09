from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.db.models import Q, Count, Sum, Max, Min
from .models import Local, Productos, Categoria_Productos, Oferta, Puntos
from registration.models import Tipo_usuarios
from .forms import Productos_form, Local_form, Ofertas_form
from django.contrib.auth.decorators import login_required
from cliente.views import paginador_propio, buscar_tipo
from cliente.models import Listas, Productos_listas, Registro_premium, Reporte_productos
from django.http import HttpResponse, Http404
import datetime
from datetime import date
from django.contrib.auth.models import User
from django.core.paginator import Paginator

#GENERAR PDFS
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


#Verificado
@login_required(redirect_field_name='login')
def Contacto_vendedor(request):
    return render(request, 'vendedor/contacto_vendedor.html',)

#Verficado
@login_required(redirect_field_name='login')
def Panel_de_vendedor(request, id):
    tipo = buscar_tipo(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id:
        dic_productos = {}
        arr_productos = []
        arr_pedidos = []
        arr_ofertas = []
        try:
            vendedor = Local.objects.get(user=id)
            total_productos = Productos.objects.filter(user=id).count()
            productos_vigentes = Productos.objects.filter(Q(user = id) , Q(activado = True)).exclude(stock = 0).count()
            productos_desactivados = Productos.objects.filter(Q(user=id), Q(activado=False)).count()
            productos_sin_stock = Productos.objects.filter(Q(user=id), Q(stock=0), Q(activado=True)).count()
            listas_pendiendtes = Listas.objects.filter(Q(local=vendedor.id), Q(estado_lista='enviada')).count()
            tipo_premium = tipo.tipo_premium
            fecha_caducidad_premium = tipo.fecha_caducidad
            #SECCION DE ALERTAS PARA PRODUCTOS
            if productos_sin_stock != 0:
                mensaje="Tienes {} productos sin stock, ve a echarle una mirada, sino desactivalo.".format(productos_sin_stock)
                arr_productos.append(mensaje)
            if productos_vigentes == 0:
                mensaje = "No tienes productos para mostrar, ve a crear o modifica algunos productos para tu tienda!"
                arr_productos.append(mensaje)
            #SECCION DE ALERTAS PARA PEDIDOS
            if listas_pendiendtes != 0:
                mensaje = "Tienes {} pedidos pendientes para completar, ve a terminarlos!".format(listas_pendiendtes)
                arr_pedidos.append(mensaje)

            if total_productos != 0:
                productos_vigentes_por = int((productos_vigentes*100)/total_productos)
                productos_desactivados_por = int((productos_desactivados * 100) / total_productos)
                productos_sin_stock_por = int((productos_sin_stock * 100) / total_productos)
            else:
                productos_vigentes_por = 0
                productos_desactivados_por = 0
                productos_sin_stock_por = 0

            dic_productos= {'prod_total':total_productos, 'prod_total_por':100, 'prod_vigentes':productos_vigentes,
                            'prod_vigentes_por':productos_vigentes_por, 'prod_desactivados': productos_desactivados,
                            'prod_desactivados_por': productos_desactivados_por, 'prod_sin_stock': productos_sin_stock,
                            'prod_sin_stock_por': productos_sin_stock_por,'tipo_premium':tipo_premium, 'fecha_caducidad':
                            fecha_caducidad_premium}
            general = Oferta.objects.filter(Q(local=vendedor.id), Q(tipo_oferta='general'), Q(activado = True))
            temporada = Oferta.objects.filter(Q(local=vendedor.id), Q(tipo_oferta='temporada'), Q(activado = True))
            rango_plata = Oferta.objects.filter(Q(local=vendedor.id), Q(tipo_oferta='rango_plata'), Q(activado = True))
            rango_oro = Oferta.objects.filter(Q(local=vendedor.id), Q(tipo_oferta='rango_oro'), Q(activado = True))
            rango_diamante = Oferta.objects.filter(Q(local=vendedor.id), Q(tipo_oferta='rango_diamante'), Q(activado = True))
            convencional = Oferta.objects.filter(Q(local=vendedor.id), Q(tipo_oferta='convencional'), Q(activado = True))
            total_ofertas = Oferta.objects.filter(Q(local=vendedor.id), Q(activado= True)).count()
            # SECCION DE ALERTAS PARA OFERTAS
            if total_ofertas != 0:
                if tipo_premium != 0:
                    if general.count() == 0:
                        mensaje="No tienes ofertas generales, recuerda que una oferta general es la mejor forma de atraer nuevos clientes"
                        arr_ofertas.append(mensaje)
                if rango_plata.count() == 0:
                    mensaje = "No tienes ofertas para el rango Plata, recuerda entre mas beneficios tienen tus clientes, mas ventas tendras!"
                    arr_ofertas.append(mensaje)
                if rango_oro.count() == 0:
                    mensaje = "No tienes ofertas para el rango Oro, recuerda entre mas beneficios tienen tus clientes, mas ventas tendras!"
                    arr_ofertas.append(mensaje)
                if rango_diamante.count() == 0:
                    mensaje = "No tienes ofertas para el rango Diamante, recuerda entre mas beneficios tienen tus clientes, mas ventas tendras!"
                    arr_ofertas.append(mensaje)
            else:
                mensaje = "No tienes ninguna ofertas a mostrar, ve y crea una oferta, recuerda, entre mas beneficios tienen tus clientes, tendras mas compradores en tu tienda"
                arr_ofertas.append(mensaje)

        except:
            vendedor = None

        return render(request, 'vendedor/panel_vendedor.html',{'vendedor':vendedor, 'prod':dic_productos,
                                                               'tipo': tipo, 'general': general, 'temporada': temporada,
                                                               'rango_plata': rango_plata, 'rango_oro': rango_oro,
                                                               'rango_diamante': rango_diamante,
                                                               'convencional': convencional, 'tipo':tipo, 'arr_ofertas': arr_ofertas,
                                                               'arr_productos': arr_productos, 'arr_pedidos': arr_pedidos
                                                               })
    else:
        return redirect('registration:sin_permiso')


#Verficado
@login_required(redirect_field_name='login')
def Listar_Productos(request,id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:
        if request.method == 'POST':
            buscar = request.POST['buscar']
            objetos = Productos.objects.filter(Q(user=id), (Q(nombre__contains = buscar) | Q(nombre__icontains = buscar)))
        else:
            if request.GET.get('filtro'):
                filtro = request.GET.get('filtro')
                if filtro == 'sin_stock':
                    objetos = Productos.objects.filter(Q(user=id), Q(stock=0))
                elif filtro == 'desactivados':
                    objetos = Productos.objects.filter(Q(user=id), Q(activado=False))
                elif filtro == 'oferta':
                    objetos = Productos.objects.filter(Q(user=id), Q(oferta=True))
                else:
                    objetos = Productos.objects.filter(user=id)
            elif request.GET.get('categoria'):
                categoria = request.GET.get('categoria')
                try:
                    id_categoria = Categoria_Productos.objects.get(id=categoria)
                except:
                    id_categoria = None

                if id_categoria:
                    objetos = Productos.objects.filter(Q(user=id), Q(categoria=id_categoria.id))
                else:
                    objetos = Productos.objects.filter(user=id)
            else:
                objetos = Productos.objects.filter(user=id)

        return render(request,'vendedor/listar_productos.html',{'productos':objetos})

    else:
        return redirect('registration:sin_permiso')

#Verificado
#Problemas con el form por defecto
@login_required(redirect_field_name='login')
def Agregar_Productos(request,id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:

        #verificador para productos por suscripcion
        cantidad_productos = Productos.objects.filter(Q(user=request.user.id)).count()
        premium = int(request.session['premium'])
        if verificar_suscripcion_productos(premium, cantidad_productos) is None:
            print(verificar_suscripcion_productos(premium, cantidad_productos))
            form = Productos_form()
            if request.method == 'POST':
                oferta_input = request.POST.get('oferta', None)
                #verificador de suscipcion productos en oferta
                if premium == 0 and oferta_input:
                    mensaje = "Lo siento, pero con su nivel de suscripcion, no puede poner productos en oferta."
                    return render(request, 'vendedor/agregar_productos.html',{'form':form, 'mensaje_error_oferta':mensaje})
                else:
                    form_llenado = Productos_form(request.POST, request.FILES)
                    try:
                        id_user = int(request.POST['user'])
                    except:
                        id_user = None
                    if form_llenado.is_valid() and id_user == id:
                        form_llenado.save()
                        return redirect(reverse('vendedor:listar_productos', args=[request.user.id])+ '?msg=form_ok')
                    else:
                        return redirect(reverse('vendedor:agregar_productos', args=[request.user.id])+ '?msg=form_no_valid')

            return render(request, 'vendedor/agregar_productos.html',{'form':form})
        else:
            mensaje_error = verificar_suscripcion_productos(premium, cantidad_productos)
            return render(request, 'vendedor/agregar_productos.html', {'mensaje_error': mensaje_error})
    else:
        return redirect('registration:sin_permiso')

#verificado
@login_required(redirect_field_name='login')
def Actualizar_Productos(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and local.activado == True:
        objeto = get_object_or_404(Productos, id=id)
        stock_antiguo = objeto.stock
        if request.user.id == objeto.user.id:
            form = Productos_form(instance=objeto)
            if request.method == 'POST':
                # verificador de suscipcion productos en oferta
                premium = int(request.session['premium'])
                if premium == 0 and request.POST['oferta'] == True:
                    mensaje = "Lo siento, pero con su nivel de suscripcion, no puede poner productos en oferta."
                    return render(request, 'vendedor/actualizar_productos.html',
                                  {'form': form, 'mensaje_error_oferta': mensaje})
                else:
                    form_llenado = Productos_form(request.POST, request.FILES, instance=objeto)
                    try:
                        id_user = int(request.POST['user'])
                    except:
                        id_user = None
                    if form_llenado.is_valid() and id_user == request.user.id:
                        form_llenado.save()
                        try:
                            stock = int(request.POST['stock'])
                        except:
                            stock=None
                        if stock and stock_antiguo != stock:
                            prod_max = int(stock * 0.1)
                            objeto.maximo_prod_comprar = prod_max
                            objeto.save()
                        return redirect(reverse('vendedor:listar_productos', args=[request.user.id])+ '?msg=act_ok')
                    else:
                        return redirect(reverse('vendedor:actualizar_productos', args=[id]) + '?msg=act_error')
            return render(request, 'vendedor/actualizar_productos.html',{'form':form})
        else:
            return redirect('registration:sin_permiso')

    else:
        return redirect('registration:sin_permiso')

#Verificado
@login_required(redirect_field_name='login')
def Eliminar_Productos(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and local.activado == True:

        producto = Productos.objects.get(id=id)
        if request.user.id == producto.user.id:
            if request.method == 'POST':
                if producto.delete():
                    return redirect(reverse('vendedor:listar_productos', args=[request.user.id]) + '?msg=elim_ok')
                else:
                    return redirect(reverse('vendedor:eliminar_productos', args=[id]) + '?msg=elim_error')
            else:
                return render(request, 'vendedor/eliminar_producto.html',{'producto':producto})
        else:
            return redirect('registration:sin_permiso')

    else:
        return redirect('registration:sin_permiso')

#Verificado
@login_required(redirect_field_name='login')
def Detalle_Local(request,id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id==id and local.activado == True:
        try:
            local = Local.objects.get(user=id)
        except:
            local = None
        return render(request, 'vendedor/mi_tienda.html',{'local':local})
    else:
        return redirect('registration:sin_permiso')


#Verificado
@login_required(redirect_field_name='login')
def Actualizar_Local(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:
        local = Local.objects.get(user=id)
        local_form = Local_form(instance=local)
        if request.method == 'POST':
            form = Local_form(request.POST, request.FILES, instance=local)
            try:
                id_user = int(request.POST['user'])
            except:
                id_user = None
            if form.is_valid() and id_user == request.user.id:
                form.save()
                local.activado=True
                local.save()
                return redirect(reverse('vendedor:mi_tienda', args=[request.user.id]) + '?msg=act_ok')
            else:
                return redirect(reverse('vendedor:actualizar_mi_tienda', args=[request.user.id]) + '?msg=act_error')
        return render(request, 'vendedor/actualizar_mi_tienda.html',{'form':local_form})
    else:
        return redirect('registration:sin_permiso')

#Verificado
@login_required(redirect_field_name='login')
def Panel_Listas(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and local.activado == True:
        listas = Listas.objects.filter(Q(local__user=request.user.id)).\
            exclude(Q(estado_lista='normal') | Q(estado_lista='cancelada') | Q(estado_lista='completada') | Q(estado_lista='no_retirada')).\
            order_by('-fecha_actualizacion')
        listas = paginador_propio(request, listas, 8)
        if request.method == 'POST':
            buscar= request.POST.get('buscar')
            listas = Listas.objects.filter(Q(local__user=request.user.id),(Q(nombre__contains=buscar) | Q(nombre__icontains=buscar))).\
                exclude(Q(estado_lista='normal') | Q(estado_lista='cancelada')).\
                order_by('-fecha_actualizacion')
        elif request.GET.get('estado_lista'):
            filtro = request.GET.get('estado_lista')
            if filtro == 'enviada':
                listas = buscar_lista(request, 'enviada')
            elif filtro == 'armando_pedido':
                listas = buscar_lista(request, 'armando_pedido')
            elif filtro == 'lista_retiro':
                listas = buscar_lista(request, 'lista_retiro')
            elif filtro == 'no_retirada':
                listas = buscar_lista(request, 'no_retirada')
        return render(request, 'vendedor/mis_pedidos.html', {'listas': listas})
    else:
        return redirect('registration:sin_permiso')

#verificado
@login_required(redirect_field_name='login')
def Detalle_Listas(request, id):
    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    lista = get_object_or_404(Listas, id=id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and local.activado == True and lista.local.id == local.id\
            and lista.estado_lista != 'normal':
        productos_lista = Productos_listas.objects.filter(Q(user=lista.user.id), Q(lista=id))
        total_lista_seleccionados = 0
        for productos in productos_lista:
            if productos.producto_marcado:
                total_lista_seleccionados+=int(productos.cantidad*productos.precio_producto)
        lista.total_marcado=total_lista_seleccionados
        lista.save()
        if request.method == 'POST':
            guardar_marcado = request.POST.get('Guardar_progreso', None)
            modificar_estado = request.POST.get('Modificar_estado', None)
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
                return redirect(reverse('vendedor:success_detalle_mis_pedidos', args=[id]))
            elif modificar_estado:
                return redirect(reverse('vendedor:revisar_mis_pedidos', args=[id]))
        return render(request, 'vendedor/detalle_mis_pedidos.html',{'lista':lista,'productos':productos_lista, 'tipo':tipo} )
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Detalle_pedidos_success(request, id):
    return render(request, 'vendedor/verificar_marcado_detalle_pedidos.html', {'id':id})

#Verificado
@login_required(redirect_field_name='login')
def Revisar_Listas(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    lista = get_object_or_404(Listas, id=id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and local.activado == True and lista.local.id == local.id \
            and lista.estado_lista != 'normal':
        if request.method == 'POST':
            estado = request.POST.get('lista')
            if estado != 'normal' and (estado == 'lista_retiro' or estado == 'armando_pedido' or estado == 'enviada'
                                       or estado == 'cancelada' or estado == 'no_retirada' or estado == 'completada'):
                lista.estado_lista = request.POST.get('lista')
                lista.comentario_vendedor = request.POST.get('comentarios')
                lista.save()
                #DEVOLVER STOCK SI SE CANCELA O NO SE RETIRA
                if estado == 'cancelada' or estado == 'no_retirada':
                    productos_lista = Productos_listas.objects.filter(Q(user=lista.user.id), Q(lista=id))
                    for producto in productos_lista:
                        producto_cambiar = Productos.objects.get(id=producto.productos.id)
                        producto_cambiar.stock += producto.cantidad
                        producto_cambiar.save()

                #SISTEMA DE PUNTOS y AGREGAR DATOS A REPORTERIA DE PRODUCTOS
                if estado == 'completada':
                    productos_lista = Productos_listas.objects.filter(Q(user=lista.user.id), Q(lista=id))
                    for prod in productos_lista:
                        client = User.objects.get(id = prod.user.id)
                        total = int(prod.cantidad * prod.precio_producto)
                        Reporte_productos.objects.create(cliente=client, lista=prod.lista.id, local=local,
                                                         producto=prod.productos.id, nombre_producto=prod.productos.nombre,
                                                         cantidad=prod.cantidad, oferta=prod.oferta, Total=total,
                                                         fecha_registro=date.today())

                    try:
                        persona_puntos = Puntos.objects.get(Q(user = lista.user.id), Q(local=local.id))
                    except:
                        persona_puntos = None
                    total_puntos = int(lista.total/10000)
                    if persona_puntos:
                        persona_puntos.puntos+=total_puntos
                        tipo_de_cuenta = calcular_puntos_persona(persona_puntos.puntos)
                        persona_puntos.tipo_cuenta = tipo_de_cuenta
                        persona_puntos.save()
                    else:
                        usuario_nuevo = User.objects.get(id = lista.user.id)
                        tipo_de_cuenta = calcular_puntos_persona(total_puntos)
                        Puntos.objects.create(user = usuario_nuevo, puntos = total_puntos, local = local, tipo_cuenta = tipo_de_cuenta)
                return redirect(reverse('vendedor:detalle_mis_pedidos', args=[id]) + '?msg=estado_cambiado')
            else:
                return redirect(reverse('vendedor:revisar_mis_pedidos', args=[id]) + '?msg=form_error')
        return render(request, 'vendedor/revisar_mis_pedidos.html',{'lista':lista, 'id':id})
    else:
        return redirect('registration:sin_permiso')

#Verificado
@login_required(redirect_field_name='login')
def Mis_Ofertas(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:
        local = get_object_or_404(Local, user = id)
        general = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='general'))
        temporada = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='temporada'))
        rango_plata = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_plata'))
        rango_oro = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_oro'))
        rango_diamante = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='rango_diamante'))
        convencional = Oferta.objects.filter(Q(local=local.id), Q(tipo_oferta='convencional'))
        return render(request, 'vendedor/mis_ofertas.html', {'tipo':tipo,'general':general,'temporada':temporada,
                                                             'rango_plata':rango_plata,'rango_oro':rango_oro,
                                                             'rango_diamante':rango_diamante,'convencional':convencional})
    else:
        return redirect('registration:sin_permiso')

#Verificar
@login_required(redirect_field_name='login')
def Agregar_Ofertas(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:
        local = get_object_or_404(Local, user=request.user.id)
        form = Ofertas_form()
        if request.method == 'POST':
            form = Ofertas_form(request.POST)
            try:
                id_local = int(request.POST['local'])
            except:
                id_local = None
            ofertas_general = Oferta.objects.filter(Q(local=local.id),Q(activado=True),Q(tipo_oferta='general'))

            if ofertas_general.count() >= 1 and request.POST['tipo_oferta'] == 'general':
                return redirect(reverse('vendedor:agregar_oferta', args=[request.user.id]) + '?msg=general_error')
            elif (request.POST['tipo_oferta']=='general' or request.POST['tipo_oferta']=='temporada') and tipo.tipo_premium==0:
                return redirect(reverse('vendedor:agregar_oferta', args=[request.user.id]) + '?msg=premium_error')
            elif form.is_valid() and id_local == local.id:
                form.save()
                return redirect(reverse('vendedor:mis_ofertas', args=[request.user.id]) + '?msg=form_ok')
            else:
                return redirect(reverse('vendedor:agregar_oferta', args=[request.user.id])+'?msg=form_error')
        return render(request, 'vendedor/agregar_oferta.html',{'form':form,'tipo':tipo, 'local':local})
    else:
        return redirect('registration:sin_permiso')

#Verificada
@login_required(redirect_field_name='login')
def Actualizar_Ofertas(request, id_oferta):

    tipo = buscar_tipo(request.user.id)
    oferta = get_object_or_404(Oferta,id = id_oferta)
    local = get_object_or_404(Local,id = int(oferta.local.id))
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == local.user.id and local.activado == True:
        form = Ofertas_form(instance=oferta)
        ofertas_general = Oferta.objects.filter(Q(local=local.id), Q(activado=True), Q(tipo_oferta='general'))
        if request.method == 'POST':
            if ofertas_general.count() >= 1 and request.POST['tipo_oferta'] == 'general':
                return redirect(reverse('vendedor:actualizar_oferta', args=[id_oferta]) + '?msg=general_error')
            elif (request.POST['tipo_oferta']=='general' or request.POST['tipo_oferta']=='temporada') and tipo.tipo_premium==0:
                return redirect(reverse('vendedor:actualizar_oferta', args=[id_oferta]) + '?msg=premium_error')
            elif oferta.id == int(request.POST['local']):
                form = Ofertas_form(request.POST, instance=oferta)
                if form.is_valid():
                    form.save()
                    return redirect(reverse('vendedor:mis_ofertas', args=[request.user.id])+'?msg=act_ok')
                else:
                    return redirect(reverse('vendedor:actualizar_oferta', args=[id_oferta]) + '?msg=act_error')
            else:
                return redirect(reverse('vendedor:actualizar_oferta', args=[id_oferta]) + '?msg=act_user_error')
        return render(request, 'vendedor/actualizar_oferta.html',{'form':form, 'tipo':tipo, 'tipo_oferta':oferta.tipo_oferta})
    else:
        return redirect('registration:sin_permiso')

#Verificado
@login_required(redirect_field_name='login')
def Eliminar_Ofertas(request, id_oferta):

    tipo = buscar_tipo(request.user.id)

    oferta = get_object_or_404(Oferta,id = id_oferta)
    try:
        local_id = int(oferta.local.id)
    except:
        local_id = None

    local = get_object_or_404(Local,id = local_id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == local.user.id:
        if request.method == 'POST':
            if oferta.delete():
                return redirect(reverse('vendedor:mis_ofertas', args=[request.user.id])+'?msg=del_ok')
            else:
                return redirect(reverse('vendedor:mis_ofertas', args=[request.user.id]) + '?msg=del_error')
        return render(request, 'vendedor/eliminar_oferta.html', )
    else:
        return redirect('registration:sin_permiso')

#Seccion de Reportes
@login_required(redirect_field_name='login')
def Seleccion_Reportes(request, id_user):
    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id_user and local.activado == True and tipo.tipo_premium != 0:
        return render(request, 'vendedor/seleccion_reportes.html', )
    else:
        return redirect('registration:sin_permiso')

#Auditoria para admin
def Reportes_Premium(request):
    #RENDER, ES PARA PASAR UN TEMPLATE, PUEDE SER TAMBIEN UN CONTENT-TYPE PERO PARA ESTE CASO NO
    #EL HTTPRESPONSE SIRVE PARA ESCRIBIR EN BLANCO, PARA UN PDF SIRVE MUCHO
    tipo = buscar_tipo(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'administrador':

        documento = request.GET.get('doc', None)
        all_document = request.GET.get('all', None)
        buscar_cliente = request.GET.get('buscar_cliente', None)
        buscar_premium = request.GET.get('buscar_premium', None)
        buscar_fecha = request.GET.get('buscar_fecha', None)
        mensaje_error = ""
        registros = Registro_premium.objects.all()

        if documento:
            datos = get_list_or_404(Registro_premium, id = documento)
            return Imprimir_pdf_premium(datos)

        elif all_document:
            datos = Registro_premium.objects.all()
            return Imprimir_pdf_premium(datos)

        elif buscar_cliente:
            buscado = request.GET.get('cliente',None)
            datos = Registro_premium.objects.filter(Q(user__username__contains=buscado) | Q(user__username__icontains = buscado))
            if request.GET.get('pdf', None):
                return Imprimir_pdf_premium(datos)
            return render(request, 'vendedor/reporte_premium.html', {'registros': datos})

        elif buscar_premium:
            buscado = request.GET.get('premium', None)
            if buscado == 1 or buscado == 2 or buscado == 3:
                datos = Registro_premium.objects.filter(premium = buscado)
                if request.GET.get('pdf', None):
                    return Imprimir_pdf_premium(datos)
                return render(request, 'vendedor/reporte_premium.html', {'registros': datos})
            else:
                mensaje_error="Seleccione una opcion valida de la lista"
                return render(request, 'vendedor/reporte_premium.html', {'registros': registros,
                                                                         'mensaje_error': mensaje_error})

        elif buscar_fecha:
            buscado1 = request.GET.get('fecha_inicio', None)
            buscado1 = datetime.datetime.strptime(buscado1, '%Y-%m-%d')
            buscado1 = buscado1.date()
            buscado2 = request.GET.get('fecha_final', None)
            buscado2 = datetime.datetime.strptime(buscado2, '%Y-%m-%d')
            buscado2 = buscado2.date()

            if buscado1 <= buscado2:
                fechas = Registro_premium.objects.filter(fecha_inicio__range=(buscado1, buscado2))
                datos = []
                for x in fechas:
                    if x.fecha_caducidad <= buscado2:
                        datos.append(x)

                if request.GET.get('pdf', None):
                    return Imprimir_pdf_premium(datos)
                return render(request, 'vendedor/reporte_premium.html', {'registros': datos})
            else:
                mensaje_error="La fecha de inicio no puede ser mayor a la fecha final"
                return render(request, 'vendedor/reporte_premium.html', {'registros': registros,
                                                                         'mensaje_error': mensaje_error})

        return render(request, 'vendedor/reporte_premium.html',{'registros':registros})
    else:
        return redirect('registration:sin_permiso')

#Verificado
#Reporteria para vendedor
def Reporte_Productos(request, id_user):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id_user and local.activado == True and tipo.tipo_premium != 0:
        diccionario = {}
        query=None
        ##Cantidad de Productos Totales Activados
        productos_totales = Productos.objects.filter(Q(user=id_user), Q(activado=True)).count()
        if productos_totales >=1:
            diccionario['productos_totales'] = productos_totales
            diccionario['productos_totales_porcentaje'] = 100
        else:
            diccionario['productos_totales'] = productos_totales
            diccionario['productos_totales_porcentaje'] = 0
            productos_totales = 1

        ##Cantidad de Producto con Stock y Activados
        productos_estado_normal = Productos.objects.filter(Q(user=id_user), Q(activado=True), Q(oferta=False)).exclude(stock=0)
        diccionario['productos_estado_normal'] = productos_estado_normal.count()
        diccionario['productos_estado_normal_porcentaje'] = int((productos_estado_normal.count()*100)/productos_totales)

        ##Cantidad de productos en oferta con stock
        productos_oferta = Productos.objects.filter(Q(user=id_user), Q(activado=True), Q(oferta=True)).exclude(stock=0)
        diccionario['productos_oferta'] = productos_oferta.count()
        diccionario['productos_oferta_porcentaje'] = int((productos_oferta.count()*100)/productos_totales)

        ##cantidad de productos Sin stock y Activados
        productos_sin_stock= Productos.objects.filter(Q(user=id_user), Q(activado=True), Q(stock=0))
        diccionario['productos_sin_stock'] = productos_sin_stock.count()
        diccionario['productos_sin_stock_porcentaje'] = int((productos_sin_stock.count()*100)/productos_totales)


        ##Info Producto mas vendido, son 3
        productos_diferentes = Reporte_productos.objects.filter(Q(local__user=id_user)).values('producto').distinct()
        arr_productos_mas_vendidos = []
        for x in productos_diferentes:
            diccionario_custom = {}
            nombre = ""
            nombre = Reporte_productos.objects.filter(producto=x['producto']).values('nombre_producto').order_by(
                '-fecha_registro')[0]
            nombre = nombre['nombre_producto']
            Sumas = ""
            Sumas = Reporte_productos.objects.filter(producto=x['producto']).aggregate(suma_cantidad=Sum('cantidad'),
                                                                                       suma_totales=Sum('Total'))
            diccionario_custom = {'nombre': nombre, 'cantidad': Sumas['suma_cantidad'], 'total': Sumas['suma_totales']}
            arr_productos_mas_vendidos.append(diccionario_custom)

            # Metodo burbuja para ordenar de mayor a menor
        if len(arr_productos_mas_vendidos) > 1:
            lista_ordenada = ordenar_listas(arr_productos_mas_vendidos, 'cantidad', 'mayor-menor')
            diccionario['productos_mas_vendidos'] = lista_ordenada[0:3]
        else:
            diccionario['productos_mas_vendidos'] = arr_productos_mas_vendidos[0:3]

        ##Productos de mayor valor en la tienda, son 5, no tienen que estar en oferta
        productos_mayor_valor = Productos.objects.filter(Q(user=id_user), Q(activado=True), Q(oferta=False)).order_by('-precio').exclude(stock=0)
        arr_productos_mayor_valor = []

        for x in productos_mayor_valor:
            if len(arr_productos_mayor_valor) < 5:
                arr_productos_mayor_valor.append(x)
            else:
                break
        diccionario['productos_mayor_valor'] = arr_productos_mayor_valor


        ##Productos mas baratos de la tienda, son 5, no tienen que estar en oferta
        productos_menor_valor = Productos.objects.filter(Q(user=id_user), Q(activado=True), Q(oferta=False)).order_by(
            'precio').exclude(stock=0)
        arr_productos_menor_valor = []
        for x in productos_menor_valor:
            if len(arr_productos_menor_valor) < 5:
                arr_productos_menor_valor.append(x)
            else:
                break
        diccionario['productos_menor_valor'] = arr_productos_menor_valor


        ##cantidad de productos vendidos totales
        productos_cantidad_tatales = Reporte_productos.objects.filter(Q(local__user=id_user)).aggregate(
            Suma=Sum('cantidad'))
        diccionario['productos_cantidad_totales'] = productos_cantidad_tatales['Suma']

        ##cantidad de productos vendidos sin oferta
        productos_cantidad = Reporte_productos.objects.filter(Q(local__user=id_user), Q(oferta=False)).aggregate(
            Suma=Sum('cantidad'))
        diccionario['productos_cantidad'] = productos_cantidad['Suma']

        ##cantidad de productos vendidos con oferta
        productos_cantidad_oferta = Reporte_productos.objects.filter(Q(local__user=id_user), Q(oferta=True)).aggregate(Suma=Sum('cantidad'))
        diccionario['productos_cantidad_oferta'] = productos_cantidad_oferta['Suma']


        if request.method == 'POST':
            buscar_producto= request.POST.get('buscar_producto', None)
            buscar_mes = request.POST.get('buscar_mes', None)
            buscar_fecha = request.POST.get('buscar_fecha', None)

            if buscar_producto:
                buscado = request.POST.get('nombre_prod', None)
                query = Reporte_productos.objects.filter(Q(local__user=id_user),
                                                         Q(fecha_registro__year=date.today().year),
                                                         (Q(nombre_producto__contains=buscado) | Q(nombre_producto__icontains = buscado)))
                return render(request, 'vendedor/reporte_productos.html',
                              {'dic_informacion': diccionario, 'datos': query, 'criterio':request.POST.get('nombre_prod', None)})

            elif buscar_mes:
                buscado = request.POST.get('estado', None)
                #Evitar que la pagina se caiga por valores literales
                try:
                    buscado = int(buscado)
                except:
                    buscado = 0

                if traer_mes(int(buscado)):
                    query = Reporte_productos.objects.filter(Q(local__user=id_user),
                                                             Q(fecha_registro__month=int(buscado))).values('producto').distinct()
                    productos_mes = []
                    for x in query:
                        diccionario_custom = {}
                        nombre = ""
                        nombre = \
                        Reporte_productos.objects.filter(producto=x['producto']).values('nombre_producto').order_by(
                            '-fecha_registro')[0]
                        nombre = nombre['nombre_producto']
                        Sumas = ""
                        Sumas = Reporte_productos.objects.filter(producto=x['producto']).aggregate(
                            suma_cantidad=Sum('cantidad'), suma_totales=Sum('Total'))
                        diccionario_custom = {'nombre': nombre, 'cantidad': Sumas['suma_cantidad'],
                                              'total': Sumas['suma_totales']}
                        productos_mes.append(diccionario_custom)

                    criterio = traer_mes(int(buscado))
                    return render(request, 'vendedor/reporte_productos.html',
                                  {'dic_informacion': diccionario, 'datos_mes': productos_mes,
                                   'criterio': criterio})
                else:
                    raise Http404
            elif buscar_fecha:
                buscado1 = request.POST.get('fecha_inicio', None)
                buscado2 = request.POST.get('fecha_final', None)
                try:
                    buscado1 = datetime.datetime.strptime(buscado1, '%Y-%m-%d')
                    buscado1 = buscado1.date()

                    buscado2 = datetime.datetime.strptime(buscado2, '%Y-%m-%d')
                    buscado2 = buscado2.date()
                except:
                    buscado1=None
                    buscado2=None
                if buscado1 and buscado2:
                    query = None
                    mensaje_error = None
                    criterio = None
                    if buscado1 <= buscado2:
                        query = Reporte_productos.objects.filter(fecha_registro__range=(buscado1, buscado2))
                        criterio = "Datos desde {} hasta el {}".format(buscado1, buscado2)
                    else:
                        mensaje_error = "La fecha de inicio no puede ser mayor a la fecha final"

                    return render(request, 'vendedor/reporte_productos.html',
                                  {'dic_informacion': diccionario, 'datos': query,
                                   'criterio': criterio, 'mensaje_error':mensaje_error})
                else:
                    raise Http404
        else:
            ##Productos del mes actual, pagina inicio
            mes_actual = date.today().month
            productos_del_mes = Reporte_productos.objects.filter(Q(local__user=id_user), Q(fecha_registro__month=mes_actual))
            query = productos_del_mes

        return render(request, 'vendedor/reporte_productos.html',{'dic_informacion':diccionario, 'datos':query})
    else:
        return redirect('registration:sin_permiso')

#FUNCIONES PERSONALIZADAS
def verificar_suscripcion_productos(suscripcion, cantidad_productos):
    verificado = None
    if suscripcion == 0:
        if cantidad_productos >= 20:
            verificado = "Lo siento pero alcanzo la capacidad maxima de 20 productos, para poder agregar mas productos, " \
                          "elimine algun producto existente o mejore su suscripcion."
    elif suscripcion == 1:
        if cantidad_productos >= 40:
            verificado = "Lo siento pero alcanzo la capacidad maxima de 40 productos, para poder agregar mas productos, " \
                         "elimine algun producto existente o mejore su suscripcion."
    elif suscripcion == 2:
        if cantidad_productos >= 60:
            verificado = "Lo siento pero alcanzo la capacidad maxima de 60 productos, para poder agregar mas productos, " \
                         "elimine algun producto existente o mejore su suscripcion."
    else:
        verificado = None

    return verificado


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

def buscar_local(id):
    try:
        local = Local.objects.get(user=id)
    except:
        local = None
    return local

def buscar_lista(request,estado):
    listas = Listas.objects.filter(Q(local__user=request.user.id), Q(estado_lista=estado)).order_by(
        '-fecha_actualizacion')
    return listas

def Imprimir_pdf_premium(datos):
    response = HttpResponse(content_type='application/pdf')
    #este es para descarga directa
    #response['Content-Disposition']= 'attachment; filename= TuVegaApp Reporte de Usuarios Premium.pdf'
    response['Content-Disposition'] = 'filename= TuVegaApp Registro de Usuarios Premium.pdf'
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
    header = Paragraph("Registro de Usuarios Premium", styles['Heading2'])
    premium.append(header)

    headings = (Paragraph("ID Cliente", styles['Normal']), 'Cliente', Paragraph("Tipo de Premium", styles['Normal']),
                Paragraph("Fecha de Inicio", styles['Normal']), Paragraph("Fecha de Caducidad", styles['Normal']))
    Datos = [(x.user.id, x.user.username, x.premium, x.fecha_inicio, x.fecha_caducidad)
                       for x in datos]
    t = Table([headings]+Datos, colWidths=[91, 91, 91, 91, 91])

    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (4, -1), 1, colors.dodgerblue),
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

def Imprimir_pdf_listas(datos):
    response = HttpResponse(content_type='application/pdf')
    #este es para descarga directa
    #response['Content-Disposition']= 'attachment; filename= TuVegaApp Reporte de Usuarios Premium.pdf'
    response['Content-Disposition'] = 'filename= TuVegaApp Registro de pedidos.pdf'
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
    header = Paragraph("Registro de Pedidos", styles['Heading2'])
    premium.append(header)
    headings = (Paragraph('ID Lista', styles['Normal']), Paragraph('ID Cliente', styles['Normal']),'Cliente',
                Paragraph('Fecha de Registro', styles['Normal']), 'Total', Paragraph('ID Local', styles['Normal']),
                Paragraph('Estado del Pedido', styles['Normal']))
    Datos = [(x.lista.id, x.cliente.id, x.cliente.username, Paragraph(str(x.fecha_registro), styles['Normal']), x.total,
              x.local.id, x.estado)
                       for x in datos]
    t = Table([headings]+Datos, colWidths=[65, 65, 65, 65, 65, 65, 65])

    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
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

def calcular_puntos_persona(datos):
    rango = ""
    if datos <= 200:
        rango = "Plata"
    elif datos >200 and datos <= 500:
        rango = "Oro"
    elif datos > 500:
        rango = "Diamante"
    return rango

def ordenar_listas(lista, campo, orden):
    lista_a_ordenar = lista
    if orden == 'mayor-menor':
        for num in range(len(lista_a_ordenar) - 1, 0, -1):
            for i in range(num):
                if lista_a_ordenar[i][campo] < lista_a_ordenar[i + 1][campo]:
                    temp = lista_a_ordenar[i]
                    lista_a_ordenar[i] = lista_a_ordenar[i + 1]
                    lista_a_ordenar[i + 1] = temp
    else:
        for num in range(len(lista_a_ordenar) - 1, 0, -1):
            for i in range(num):
                if lista_a_ordenar[i][campo] > lista_a_ordenar[i + 1][campo]:
                    temp = lista_a_ordenar[i]
                    lista_a_ordenar[i] = lista_a_ordenar[i + 1]
                    lista_a_ordenar[i + 1] = temp
    return lista_a_ordenar

'''''
#reporte_registro_listas.html template hay que eliminarlo o dejarlo en standby
def Reportes_Listas(request, id_user):
    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id_user and local.activado == True:

        documento = request.GET.get('doc', None)
        all_document = request.GET.get('all', None)
        buscar_cliente = request.GET.get('buscar_cliente', None)
        buscar_estado = request.GET.get('buscar_estado', None)
        buscar_fecha = request.GET.get('buscar_fecha', None)
        mensaje_error = ""
        registro = Registro_listas.objects.filter(local__user__id=request.user.id)

        if documento:
            datos = get_list_or_404(Registro_listas, id=documento)
            return Imprimir_pdf_listas(datos)

        elif all_document:
            datos = Registro_listas.objects.filter(local__user__id=request.user.id)
            return Imprimir_pdf_listas(datos)

        elif buscar_cliente:
            buscado = request.GET.get('cliente', None)
            datos = Registro_listas.objects.filter(
                Q(cliente__username__contains=buscado) | Q(cliente__username__icontains=buscado))
            if request.GET.get('pdf', None):
                return Imprimir_pdf_listas(datos)
            return render(request, 'vendedor/reporte_registro_listas.html', {'registros': datos})

        elif buscar_estado:
            buscado = request.GET.get('estado', None)
            if buscado == 'completada' or buscado == 'cancelada' or buscado == 'no_retirada':
                datos = Registro_listas.objects.filter(estado=buscado)
                if request.GET.get('pdf', None):
                    return Imprimir_pdf_listas(datos)
                return render(request, 'vendedor/reporte_registro_listas.html', {'registros': datos})
            else:
                mensaje_error = "Seleccione una opcion valida de la lista"
                return render(request, 'vendedor/reporte_registro_listas.html', {'registros': registro,
                                                                         'mensaje_error': mensaje_error})

        elif buscar_fecha:
            buscado1 = request.GET.get('fecha_inicio', None)
            buscado1 = datetime.datetime.strptime(buscado1, '%Y-%m-%d')
            buscado1 = buscado1.date()
            buscado2 = request.GET.get('fecha_final', None)
            buscado2 = datetime.datetime.strptime(buscado2, '%Y-%m-%d')
            buscado2 = buscado2.date()

            if buscado1 <= buscado2:
                datos = Registro_listas.objects.filter(fecha_registro__range=(buscado1, buscado2))

                if request.GET.get('pdf', None):
                    return Imprimir_pdf_listas(datos)
                return render(request, 'vendedor/reporte_registro_listas.html', {'registros': datos})
            else:
                mensaje_error = "La fecha de inicio no puede ser mayor a la fecha final"
                return render(request, 'vendedor/reporte_registro_listas.html', {'registros': registro,
                                                                         'mensaje_error': mensaje_error})

        return render(request, 'vendedor/reporte_registro_listas.html',{'registros':registro})

    else:
        return redirect('registration:sin_permiso')
'''''