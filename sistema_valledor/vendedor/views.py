from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .models import Local, Productos, Categoria_Productos
from registration.models import Tipo_usuarios
from .forms import Productos_form
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required(redirect_field_name='login')
def Panel_de_vendedor(request, id):
    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
    except:
        tipo = None
    if tipo is not None and (tipo.tipo_usuario == 'vendedor' or tipo.tipo_usuario == 'administrador') and request.user.id == id:
        dic_productos = {}

        try:
            vendedor = Local.objects.get(user=id)
            total_productos = Productos.objects.filter(user=id).count()
            productos_vigentes = Productos.objects.filter(Q(user = id) , Q(activado = True)).exclude(stock = 0).count()
            productos_desactivados = Productos.objects.filter(Q(user=id), Q(activado=False)).count()
            productos_sin_stock = Productos.objects.filter(Q(user=id), Q(stock=0), Q(activado=True)).count()
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
                            'prod_sin_stock_por': productos_sin_stock_por}
        except:
            vendedor = None

        return render(request, 'vendedor/panel_vendedor.html',{'vendedor':vendedor, 'prod':dic_productos})
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def Listar_Productos(request,id):

    try:
        tipo = Tipo_usuarios.objects.get(user_id=request.user.id)
    except:
        tipo = None
    if tipo is not None and (tipo.tipo_usuario == 'vendedor' or tipo.tipo_usuario == 'administrador') and request.user.id == id:
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
                categoria = request.GET.get('categoria');
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
    except:
        tipo = None
    if tipo is not None and (tipo.tipo_usuario == 'vendedor' or tipo.tipo_usuario == 'administrador') and request.user.id == id:

        form = Productos_form()
        if request.method == 'POST':
            form_llenado = Productos_form(request.POST, request.FILES)
            id_user = int(request.POST['user'])
            if form_llenado.is_valid() and (id_user == id):
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
    except:
        tipo = None
    if tipo is not None and (tipo.tipo_usuario == 'vendedor' or tipo.tipo_usuario == 'administrador'):

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
    except:
        tipo = None
    if tipo is not None and (tipo.tipo_usuario == 'vendedor' or tipo.tipo_usuario == 'administrador'):

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

def Detalle_Local(request, id):
    return render(request, 'vendedor/mi_tienda.html',)

def Actualizar_Local(request, id):
    return render(request, 'vendedor/actualizar_mi_tienda.html',)

def Panel_Listas(request, id):
    return render(request, 'vendedor/mis_pedidos.html',)

def Detalle_Listas(request, id):
    return render(request, 'vendedor/detalle_mis_pedidos.html', )

def Revisar_Listas(request, id):
    return render(request, 'vendedor/revisar_mis_pedidos.html',)

def Mis_Ofertas(request, id):
    return render(request, 'vendedor/mis_ofertas.html', )

def Agregar_Ofertas(request, id):
    return render(request, 'vendedor/agregar_oferta.html',)

def Actualizar_Ofertas(request, id):
    return render(request, 'vendedor/actualizar_oferta.html',)

def Eliminar_Ofertas(request, id):
    return render(request, 'vendedor/eliminar_oferta.html',)
