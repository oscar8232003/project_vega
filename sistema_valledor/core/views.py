from django.shortcuts import render
from registration.models import Tipo_usuarios, Log_Acceso
from django.contrib.auth.models import User
import datetime
#Sirve para consumir apis
#import requests


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

    """
    token = requests.post('http://127.0.0.1:8000/api/v4/login/',
                          {"username": "oskar82320033", "password": "oskar8232003"})

    token_json = token.json()

    headers = headers = {'Authorization': 'Token {}'.format(token_json['token'])}

    r = requests.get('http://127.0.0.1:8000/api/v2/productos/2/', headers=headers)

    r_json = r.json()

    print(r_json)
    """
    return render(request, 'core/index.html')

def contactanos(request):
    return render(request, 'core/contactanos.html',)