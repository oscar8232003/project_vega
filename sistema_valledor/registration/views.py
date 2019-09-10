from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import RegistrationForm, UpdateUserForm
from django.contrib.auth.models import User
from .models import Preguntas_secretas, Login_respuesta_secreta, Tipo_usuarios

# Create your views here.
def registro(request):
    form = RegistrationForm()
    preguntas = Preguntas_secretas.objects.all().exclude(id=2)
    if request.method == 'POST':
        form_registro = RegistrationForm(request.POST)
        validar = User.objects.filter(username = request.POST['username']).exists()
        try:
            id_pregunta = request.POST.get('pregunta_secreta', None)
        except:
            id_pregunta = None
        if not validar and id_pregunta != None:
            if form_registro.is_valid():
                form_registro.save()
                try:
                    persona_creada = User.objects.get(username = request.POST.get('username', None))
                    pregunta = Preguntas_secretas.objects.get(id = request.POST.get('pregunta_secreta', None))
                    respuesta = request.POST.get('respuesta_secreta', None)
                    Login_respuesta_secreta.objects.create(user = persona_creada, pregunta = pregunta, respuesta = respuesta)
                except:
                    pass
                return redirect(reverse('login')+"?msg=created_user")
            else:
                return redirect(reverse('registration:registro')+'?msg=error_form')
        else:
            return redirect(reverse('registration:registro') + "?msg=error_user")
    return render(request,'registration/registro.html',{'form':form, 'preguntas':preguntas})

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
                form_lleno.save()
                #print(form_lleno)
                redirect(reverse('registration:mi_perfil', kwargs={'id':request.user.id})+'?msg=update_ok')
            else:
                redirect(reverse('registration:actualizar_perfil', kwargs={'id':request.user.id})+'?msg=error_form')
        return render(request, 'registration/update_perfil.html',{'form':form})
    else:
        return redirect('registration:sin_permiso')

#Seleccion de usuario a recuperar contraseña
def seleccionar_usuario(request):
    return render(request, 'registration/seleccion_usuario.html',)

#Seleccion de usuario cliente
def seleccion_usuario_cliente(request):
    if request.method == 'POST':
        rut = request.POST.get('rut', None)
        respuesta_secreta = request.POST.get('respuesta_secreta', None)
        if respuesta_secreta:
            try:
                persona = User.objects.get(username=rut)
                tipo = Tipo_usuarios.objects.get(user_id=persona.id)
            except:
                persona = None
                tipo = None
            if persona:
                if tipo.tipo_usuario == 'cliente':
                    try:
                        pregunta = Login_respuesta_secreta.objects.get(user=persona.id)
                    except:
                        pregunta = None
                    if pregunta:
                        if pregunta.respuesta == respuesta_secreta:
                            nueva_password = "recuperacion {}".format(respuesta_secreta)
                            persona.set_password(nueva_password)
                            persona.save()
                            return render(request, 'registration/recuperacion_cliente.html',
                                          {'password':nueva_password})
                        else:
                            mensaje_error = "La respuesta secreta es incorrecta, si tiene problemas contacte al soporte"
                            return render(request, 'registration/recuperacion_cliente.html',
                                        {'rut': rut, 'pregunta': pregunta, 'mensaje_error':mensaje_error})
                    else:
                        mensaje_error = "La pregunta secreta no se encontro, por favor contacte al soporte"
                        return render(request, 'registration/recuperacion_cliente.html',
                                      {'mensaje_error': mensaje_error})
                else:
                    mensaje_error = "La persona encontrada es un vendedor, pertenece a otra categoria"
                    return render(request, 'registration/recuperacion_cliente.html', {'mensaje_error': mensaje_error})
            else:
                mensaje_error = "La persona con ese rut no se encontro"
                return render(request, 'registration/recuperacion_cliente.html', {'mensaje_error': mensaje_error})


        elif rut:

            try:
                persona = User.objects.get(username = rut)
                tipo = Tipo_usuarios.objects.get(user_id = persona.id)
            except:
                persona = None
                tipo = None
            if persona:
                if tipo.tipo_usuario == 'cliente':
                    try:
                        pregunta = Login_respuesta_secreta.objects.get(user = persona.id)
                    except:
                        pregunta = None
                    if pregunta:
                        return render(request, 'registration/recuperacion_cliente.html',{'rut':rut, 'pregunta':pregunta})
                    else:
                        mensaje_error = "La pregunta secreta no se encontro"
                        return render(request, 'registration/recuperacion_cliente.html',
                                      {'mensaje_error': mensaje_error})
                else:
                    mensaje_error = "La persona encontrada es un vendedor, pertenece a otra categoria"
                    return render(request, 'registration/recuperacion_cliente.html', {'mensaje_error': mensaje_error})
            else:
                mensaje_error = "La persona con ese rut no se encontro"
                return render(request, 'registration/recuperacion_cliente.html', {'mensaje_error':mensaje_error})
    else:
        return render(request, 'registration/recuperacion_cliente.html',)

#Seleccion de usuario vendedor
def seleccion_usuario_vendedor(request):
    if request.method == 'POST':
        rut = request.POST.get('rut', None)
        respuesta_secreta = request.POST.get('respuesta_secreta', None)
        if respuesta_secreta:
            try:
                persona = User.objects.get(username=rut)
                tipo = Tipo_usuarios.objects.get(user_id=persona.id)
            except:
                persona = None
                tipo = None
            if persona:
                if tipo.tipo_usuario == 'vendedor':
                    try:
                        pregunta = Login_respuesta_secreta.objects.get(user=persona.id)
                    except:
                        pregunta = None
                    if pregunta:
                        if pregunta.respuesta == respuesta_secreta:
                            nueva_password = "recuperacion {}".format(respuesta_secreta)
                            persona.set_password(nueva_password)
                            persona.save()
                            return render(request, 'registration/recuperacion_vendedor.html',
                                          {'password': nueva_password})
                        else:
                            mensaje_error = "La respuesta secreta es incorrecta, si tiene problemas, por favor " \
                                            "contacte con el chat de soporte que se encuentra mas abajo"
                            return render(request, 'registration/recuperacion_vendedor.html',
                                          {'rut': rut, 'pregunta': pregunta, 'mensaje_error': mensaje_error})
                    else:
                        mensaje_error = "La pregunta secreta no se encontro, por favor contacte con el chat de soporte " \
                                        "que se encuentra mas abajo"
                        return render(request, 'registration/recuperacion_vendedor.html',
                                      {'mensaje_error': mensaje_error})
                else:
                    mensaje_error = "La persona encontrada es un vendedor, pertenece a otra categoria"
                    return render(request, 'registration/recuperacion_vendedor.html', {'mensaje_error': mensaje_error})
            else:
                mensaje_error = "La persona con ese rut no se encontro"
                return render(request, 'registration/recuperacion_vendedor.html', {'mensaje_error': mensaje_error})

        elif rut:

            try:
                persona = User.objects.get(username=rut)
                tipo = Tipo_usuarios.objects.get(user_id=persona.id)
            except:
                persona = None
                tipo = None
            if persona:
                if tipo.tipo_usuario == 'vendedor':
                    try:
                        pregunta = Login_respuesta_secreta.objects.get(user=persona.id)
                    except:
                        pregunta = None
                    if pregunta:
                        return render(request, 'registration/recuperacion_vendedor.html',
                                      {'rut': rut, 'pregunta': pregunta})
                    else:
                        mensaje_error = "La pregunta secreta no se encontro, por favor contacte con el chat de " \
                                        "soporte que se encuentra mas abajo"
                        return render(request, 'registration/recuperacion_vendedor.html',
                                      {'mensaje_error': mensaje_error})
                else:
                    mensaje_error = "La persona encontrada es un vendedor, pertenece a otra categoria"
                    return render(request, 'registration/recuperacion_vendedor.html', {'mensaje_error': mensaje_error})
            else:
                mensaje_error = "La persona con ese rut no se encontro"
                return render(request, 'registration/recuperacion_vendedor.html', {'mensaje_error': mensaje_error})
    else:
        return render(request, 'registration/recuperacion_vendedor.html', )

def sin_permiso(request):
    return render(request, 'registration/sin_permiso.html')