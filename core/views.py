from django.shortcuts import render
from core.models import Evento


# Create your views here.

"""Cria uma função de index para redirecionamento"""
#def index(request):
#   return redirect('/agenda')

def lista_eventos(request):
    """
    Filtro de usuarios
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    """
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
