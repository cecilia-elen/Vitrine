from django.shortcuts import render
from usuario.models import Usuario


def Controle_adm_usuarios(request):
    lista_usuarios = Usuario.objects.all()
    context = {
        'usuarios': lista_usuarios
    }
    return render(request, 'ADM/Controle_adm_usuarios.html', context)