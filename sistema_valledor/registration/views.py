from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import RegistrationForm, UpdateUserForm
from django.contrib.auth.models import User


# Create your views here.
def registro(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form_registro = RegistrationForm(request.POST)
        validar = User.objects.filter(username = request.POST['username']).exists()
        if not validar:
            if form_registro.is_valid():
                form_registro.save()
                return redirect(reverse('login')+"?msg=created_user")
            else:
                return redirect(reverse('registration:registro')+'?msg=error_form')
        else:
            return redirect(reverse('registration:registro') + "?msg=error_user")
    return render(request,'registration/registro.html',{'form':form})

def mi_perfil(request, id):
    if request.user.id == id:
        datos=None
        try:
            datos = User.objects.get(pk = id)
            return render(request, 'registration/mi_perfil.html', {'perfil': datos})
        except:
            return render(request, 'registration/mi_perfil.html',{'perfil':datos})
    else:
        return redirect('registration:sin_permiso')

#IDEA SOBRE ACTUALIZACION DEL PERFIL PERO NO RESULTO
def actualizar_perfil(request, id):
    if request.user.id == id:
        datos = User.objects.get(pk = id)
        form = UpdateUserForm(instance=datos)
        if request.method == 'POST':
            form_lleno = UpdateUserForm(request.POST)
            if form_lleno.is_valid():
                #form_lleno.save()
                print(form_lleno)
                redirect(reverse('registration:mi_perfil', kwargs={'id':request.user.id})+'?msg=update_ok')
            else:
                redirect(reverse('registration:actualizar_perfil', kwargs={'id':request.user.id})+'?msg=error_form')
        return render(request, 'registration/update_perfil.html',{'form':form})
    else:
        return redirect('registration:sin_permiso')

def sin_permiso(request):
    return render(request, 'registration/sin_permiso.html')