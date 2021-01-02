from django.shortcuts import render
from .models import Sistema
from proyecto_covid.helpers import login_required, permiso_required


@login_required
@permiso_required
def index(request):
    sistemas = Sistema.objects.all()
    return render(request, "sistemas/index.html", {'sistemas': sistemas})


@login_required
def show(request, name):
    sistema = Sistema.objects.get(name=name)
    salas = {}
    for sala in sistema.sala_set.all():
        salas[sala] = sala.cama_set.all()
    return render(request, "sistemas/show.html", {'sistema': sistema, 'salas': salas})
