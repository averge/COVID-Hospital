from django.shortcuts import render, redirect
from proyecto_covid.helpers import login_required
from ..models import Internacion, Paciente
from ..forms import InternacionForm
from django.contrib import messages
from datetime import datetime
from sistemas.models import Sistema


@login_required
def create(request, id_):
    if request.method == "POST":
        form = InternacionForm(request.POST)
        if form.is_valid():
            p = Paciente.objects.get(id=id_)
            for internacion in p.internacion_set.all():
                    if internacion.fecha_obito:
                        messages.error(request, 'The patient has passed away')
                        return redirect ('sistemas.index')
            i = Internacion(
                fecha_inicio_sintomas=form.cleaned_data['fecha_inicio_sintomas'],
                fecha_diagnostico=form.cleaned_data['fecha_diagnostico'],
                enfermedad_actual=form.cleaned_data['enfermedad_actual'],
                descripcion=form.cleaned_data['descripcion'],
                fecha_internacion=datetime.now(),
                paciente=p,
            )
            i.save()
            p.alta = None
            if not p.get_sistema():
                er = Sistema.objects.filter(name="ER").first()
                free_bed = er.get_free_bed()
                if free_bed:
                    free_bed.paciente = p
                    free_bed.save()
                else:
                    messages.error(request, 'There are no available beds')
                    return render(request, "internaciones/create.html", {"paciente_id": id_, "form": form})
            p.save()
            messages.success(request, 'Hospitalization saved')
            return redirect("sistemas.index")
    else:
        form = InternacionForm()
    return render(request, "internaciones/create.html", {"paciente_id": id_, "form": form})


@login_required
def show(request, id_, id_2):
    paciente = Paciente.objects.get(id=id_)
    internacion = Internacion.objects.get(id=id_2)
    permitted_systems = []
    if paciente.get_sistema() and (not internacion.fecha_egreso or internacion.fecha_obito):
        permitted_systems = paciente.get_sistema().get_permitted_system()
    evoluciones_y_cambios = {}
    lista_cambios = internacion.cambio_de_sistema.order_by("-fecha_cambio", "-hora_cambio")
    lista_evoluciones = internacion.evoluciones.order_by("-fecha_carga", "-hora_carga")
    for cambio in lista_cambios:
        if str(cambio.fecha_cambio) not in evoluciones_y_cambios:
            evoluciones_y_cambios[str(cambio.fecha_cambio)] = [{"cambio": cambio}]
        else:
            evoluciones_y_cambios[str(cambio.fecha_cambio)].append({"cambio": cambio})
    for evolucion in lista_evoluciones:
        if str(evolucion.fecha_carga) not in evoluciones_y_cambios:
            evoluciones_y_cambios[str(evolucion.fecha_carga)] = [{"evolucion": evolucion}]
        else:
            evoluciones_y_cambios[str(evolucion.fecha_carga)].append({"evolucion": evolucion})
    sorted_dict = dict(sorted(evoluciones_y_cambios.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'), reverse=True))
    return render(
        request,
        "internaciones/show.html",
        {
            "paciente": paciente,
            "internacion": internacion,
            "permitted_systems": permitted_systems,
            "sorted_dict": sorted_dict,
            "lista_cambios": lista_cambios,
            "lista_evoluciones": lista_evoluciones,
        }
    )