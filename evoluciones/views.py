from django.shortcuts import render, redirect
from .forms import EvolucionForm
from proyecto_covid.helpers import login_required
from pacientes.models import Internacion, Paciente
from reglas.helpers import correr_reglas


@login_required
def create(request, id_p, id_i):
    if request.method == "POST":
        form = EvolucionForm(request.POST)
        if form.is_valid():
            internacion = Internacion.objects.get(id=id_i)
            evolucion = form.save()
            evolucion.internacion = internacion
            evolucion.save()
            paciente = Paciente.objects.get(id=id_p)
            correr_reglas(evolucion, paciente)
            return redirect("internaciones.show", id_=id_p, id_2=id_i)
    else:
        form = EvolucionForm()

    return render(request, "evoluciones/create.html", {'form': form, 'id_p': id_p, 'id_i': id_i})
