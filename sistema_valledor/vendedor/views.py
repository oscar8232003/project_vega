from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.db.models import Q
from .models import Local, Productos, Categoria_Productos, Oferta
from registration.models import Tipo_usuarios
from .forms import Productos_form, Local_form, Ofertas_form
from django.contrib.auth.decorators import login_required
from cliente.views import paginador_propio, buscar_tipo
from cliente.models import Listas, Productos_listas, Registro_listas, Registro_premium
from django.http import HttpResponse
import datetime
from django.core.paginator import Paginator

#GENERAR PDFS
import io
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

# Create your views here.

@login_required(redirect_field_name='login')
def Panel_de_vendedor(request, id):
    #Falta arreglar el tema de los alerts
    #falta poner el sistemas de puntos
    tipo = buscar_tipo(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id:
        dic_productos = {}

        try:
            vendedor = Local.objects.get(user=id)
            total_productos = Productos.objects.filter(user=id).count()
            productos_vigentes = Productos.objects.filter(Q(user = id) , Q(activado = True)).exclude(stock = 0).count()
            productos_desactivados = Productos.objects.filter(Q(user=id), Q(activado=False)).count()
            productos_sin_stock = Productos.objects.filter(Q(user=id), Q(stock=0), Q(activado=True)).count()
            tipo_premium = tipo.tipo_premium
            fecha_caducidad_premium = tipo.fecha_caducidad
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
        except:
            vendedor = None

        return render(request, 'vendedor/panel_vendedor.html',{'vendedor':vendedor, 'prod':dic_productos,
                                                               'tipo': tipo, 'general': general, 'temporada': temporada,
                                                               'rango_plata': rango_plata, 'rango_oro': rango_oro,
                                                               'rango_diamante': rango_diamante,
                                                               'convencional': convencional, 'tipo':tipo
                                                               })
    else:
        return redirect('registration:sin_permiso')

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

@login_required(redirect_field_name='login')
def Agregar_Productos(request,id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:

        form = Productos_form()
        if request.method == 'POST':
            form_llenado = Productos_form(request.POST, request.FILES)
            id_user = int(request.POST['user'])
            if form_llenado.is_valid() and id_user == id:
                form_llenado.save()
                return redirect(reverse('vendedor:listar_productos', args=[request.user.id])+ '?msg=form_ok')
            else:
                return redirect(reverse('vendedor:agregar_productos', args=[request.user.id])+ '?msg=form_no_valid')
        return render(request, 'vendedor/agregar_productos.html',{'form':form})
    else:
        return redirect('registration:sin_permiso')


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
                form_llenado = Productos_form(request.POST, request.FILES, instance=objeto)
                id_user = int(request.POST['user'])
                if form_llenado.is_valid() and (id_user == request.user.id):
                    form_llenado.save()
                    if stock_antiguo != int(request.POST['stock']):
                        prod_max = int(int(request.POST['stock']) * 0.1)
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


@login_required(redirect_field_name='login')
def Actualizar_Local(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:
        local = Local.objects.get(user=id)
        local_form = Local_form(instance=local)
        if request.method == 'POST':
            form = Local_form(request.POST, request.FILES, instance=local)
            id_user = int(request.POST['user'])
            if form.is_valid() and (id_user == request.user.id):
                form.save()
                return redirect(reverse('vendedor:mi_tienda', args=[request.user.id]) + '?msg=act_ok')
            else:
                return redirect(reverse('vendedor:actualizar_mi_tienda', args=[request.user.id]) + '?msg=act_error')
        return render(request, 'vendedor/actualizar_mi_tienda.html',{'form':local_form})
    else:
        return redirect('registration:sin_permiso')

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
                return redirect(reverse('vendedor:detalle_mis_pedidos', args=[id])+'?msg=estado_cambiado')
            else:
                return redirect(reverse('vendedor:revisar_mis_pedidos', args=[id]) + '?msg=form_error')
        return render(request, 'vendedor/revisar_mis_pedidos.html',{'lista':lista, 'id':id})
    else:
        return redirect('registration:sin_permiso')


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

@login_required(redirect_field_name='login')
def Agregar_Ofertas(request, id):

    tipo = buscar_tipo(request.user.id)
    local = buscar_local(request.user.id)

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:
        local = get_object_or_404(Local, user=request.user.id)
        form = Ofertas_form()
        if request.method == 'POST':
            form = Ofertas_form(request.POST)
            id_local = int(request.POST['local'])
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

@login_required(redirect_field_name='login')
def Eliminar_Ofertas(request, id_oferta):

    tipo = buscar_tipo(request.user.id)

    oferta = get_object_or_404(Oferta,id = id_oferta)
    local = get_object_or_404(Local,id = int(oferta.local.id))
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == local.user.id:
        if request.method == 'POST':
            if oferta.delete():
                return redirect(reverse('vendedor:mis_ofertas', args=[request.user.id])+'?msg=del_ok')
            else:
                return redirect(reverse('vendedor:mis_ofertas', args=[request.user.id]) + '?msg=del_error')
        return render(request, 'vendedor/eliminar_oferta.html', )
    else:
        return redirect('registration:sin_permiso')

def Reportes_Registro_Listas(request, id_user):
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

#FUNCIONES PERSONALIZADAS
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
    response['Content-Disposition'] = 'filename= TuVegaApp Reporte de Usuarios Premium.pdf'
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=60,
                            bottomMargin=18,)
    premium = []
    imagen = Image('media/core/Logo.png', width=201, height=44)
    premium.append(imagen)
    styles = getSampleStyleSheet()
    header = Paragraph("Informe de Usuarios Premium", styles['Heading2'])
    premium.append(header)

    headings = ('Cliente', 'Tipo de Premium', 'Fecha de Inicio', 'Fecha de Caducidad')
    Datos = [(x.user.username, x.premium, x.fecha_inicio, x.fecha_caducidad)
                       for x in datos]
    t = Table([headings]+Datos, colWidths=[155,100,100,100])

    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
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
    response['Content-Disposition'] = 'filename= TuVegaApp Reporte de pedidos.pdf'
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=60,
                            bottomMargin=18,)
    premium = []
    imagen = Image('media/core/Logo.png', width=201, height=44)
    premium.append(imagen)
    styles = getSampleStyleSheet()
    header = Paragraph("Informe de Pedidos", styles['Heading2'])
    premium.append(header)

    headings = ('Cliente', 'Fecha de Registro', 'Total', 'Cantidad de Productos', 'Estado del Pedido')
    Datos = [(x.cliente.username, x.fecha_registro, x.total, x.cantidad_productos, x.estado)
                       for x in datos]
    t = Table([headings]+Datos, colWidths=[91,91,71,111,91])

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

