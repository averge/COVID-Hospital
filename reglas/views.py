from django.shortcuts import render, redirect
from .models import Alerta
from medicos.models import TrabajadorHospital
from django.contrib import messages


def index(request):
    current_user = request.session["username"]
    medico = TrabajadorHospital.objects.get(usuario=current_user)
    alertas = []
    for paciente in medico.paciente_set.all():
        for alerta in paciente.alertas.all():
            if not alerta.vista:
                alertas.append(alerta)
    return render(request, "reglas/index.html", {'alertas': alertas})


def marcar_vista(request, id_a):
    alerta = Alerta.objects.get(id=id_a)
    alerta.vista = True
    alerta.save()
    messages.success(request, "The alert was marked as seen")
    return redirect('alertas.index')
