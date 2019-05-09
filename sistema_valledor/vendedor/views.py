from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from .models import Local, Productos, Categoria_Productos, Oferta
from registration.models import Tipo_usuarios
from .forms import Productos_form, Local_form, Ofertas_form
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required(redirect_field_name='login')
def Panel_de_vendedor(request, id):
    #Falta arreglar el tema de los alerts
    #falta poner el sistemas de puntos
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
    except:
        tipo = None
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

    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None
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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None
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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None
    if tipo is not None and tipo.tipo_usuario == 'vendedor' and local.activado == True:

        objeto = Productos.objects.get(id=id)
        if request.user.id == objeto.user.id:
            form = Productos_form(instance=objeto)
            if request.method == 'POST':
                form_llenado = Productos_form(request.POST, request.FILES, instance=objeto)
                id_user = int(request.POST['user'])
                if form_llenado.is_valid() and (id_user == request.user.id):
                    form_llenado.save()
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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None
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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None

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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None

    if tipo is not None and tipo.tipo_usuario == 'vendedor' and request.user.id == id and local.activado == True:
        local = Local.objects.get(user=id)
        local_form = Local_form(instance=local)
        if request.method == 'POST':
            form = Local_form(request.POST, request.FILES, instance=local)
            id_user = int(request.POST['user'])
            if form.is_valid() and (id_user == request.user.id):
                print(form)
                form.save()
                return redirect(reverse('vendedor:mi_tienda', args=[request.user.id]) + '?msg=act_ok')
            else:
                return redirect(reverse('vendedor:actualizar_mi_tienda', args=[request.user.id]) + '?msg=act_error')
        return render(request, 'vendedor/actualizar_mi_tienda.html',{'form':local_form})
    else:
        return redirect('registration:sin_permiso')

def Panel_Listas(request, id):
    return render(request, 'vendedor/mis_pedidos.html',)

def Detalle_Listas(request, id):
    return render(request, 'vendedor/detalle_mis_pedidos.html', )

def Revisar_Listas(request, id):
    return render(request, 'vendedor/revisar_mis_pedidos.html',)

@login_required(redirect_field_name='login')
def Mis_Ofertas(request, id):
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None
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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
        local = Local.objects.get(user=request.user.id)
    except:
        tipo = None
        local = None
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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
    except:
        tipo = None

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
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
    except:
        tipo = None

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

