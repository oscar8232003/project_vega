from django.shortcuts import render
from registration.models import Tipo_usuarios


# Create your views here.
def index(request):
    if request.user.id is not None:
        try:
            persona = Tipo_usuarios.objects.get(user_id = request.user.id)
            request.session['tipo'] = persona.tipo_usuario
            request.session['premium'] = persona.tipo_premium
        except:
            request.session['tipo']=None
            request.session['premium']=0
    else:
        request.session['tipo']=None
        request.session['premium'] = 0
    return render(request, 'core/index.html')

def contactanos(request):
    return render(request, 'core/contactanos.html',)