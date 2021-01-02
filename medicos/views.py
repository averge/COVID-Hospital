from django.shortcuts import render, redirect
from sistemas.models import Sistema
from .models import Medico, JefeSistema


def index(request, name):
    sistema = Sistema.objects.get(name=name)
    medicos = sistema.medico_set.all()
    return render(request, "medicos/index.html", {"medicos": medicos, "name": name})


def change_system(request, name, id_m):
    if request.method == "POST":
        medico = Medico.objects.get(id=id_m)
        sistema_name = request.POST["sistema_name"]
        sistema_destino = Sistema.objects.get(name=sistema_name)
        sistema_actual = Sistema.objects.get(name=name)
        jefe_sistema = JefeSistema.objects.filter(sistema__id=sistema_actual.id).first()
        for paciente in medico.paciente_set.all():
            paciente.medicos.remove(medico)
            if not paciente.medicos.all():
                paciente.medicos.add(jefe_sistema)
            paciente.save()
        medico.sistema = sistema_destino
        medico.save()
        return redirect("medicos.index", name=name)

    sistemas = Sistema.objects.exclude(name=name)
    return render(request, "medicos/change_system.html", {"sistemas": sistemas, "name": name, "id_m": id_m})
