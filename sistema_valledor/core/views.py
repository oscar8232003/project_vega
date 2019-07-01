from django.shortcuts import render
from registration.models import Tipo_usuarios, Log_Acceso
from django.contrib.auth.models import User
import datetime


# Create your views here.
def index(request):

    ##for key, value in request.session.items():
        ##print('{} => {}'.format(key, value))


    antes =len(request.session.items())

    if request.user.id is not None:
        persona = Tipo_usuarios.objects.get(user_id = request.user.id)
        request.session['tipo'] = persona.tipo_usuario
        request.session['premium'] = persona.tipo_premium
        request.session['id_persona'] = request.user.id
        request.session['fecha'] = str(datetime.datetime.now())
        cliente = User.objects.get(id=request.user.id)
    else:
        request.session['tipo'] = None
        request.session['premium'] = 0

    despues = len(request.session.items())

    if antes == 5 and despues == 7:
        Log_Acceso.objects.create(user=cliente, fecha_registro=str(datetime.datetime.now()),
                                  tipo_cliente=persona.tipo_usuario)

    #print(request.session['tipo'])
    return render(request, 'core/index.html')

def contactanos(request):
    return render(request, 'core/contactanos.html',)