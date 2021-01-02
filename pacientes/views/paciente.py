from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse
from pacientes.forms import PacienteForm
from pacientes.models import Paciente, Internacion
from medicos.models import Medico, JefeSistema, TrabajadorHospital
from sistemas.models import Sistema, Cama, CambioSistema
from django.contrib import messages
from proyecto_covid.helpers import login_required
from datetime import datetime
from reportlab.pdfgen.canvas import Canvas
from ..helpers import PdfPrinter


@login_required
def create(request):
    if request.method == "POST":
        er = Sistema.objects.filter(name="ER").first()
        form = PacienteForm(request.POST)
        free_bed = er.get_free_bed()
        if free_bed and form.is_valid():
            if request.POST["new_patient"] == "false":
                p = Paciente.objects.get(dni=form.cleaned_data['dni'])
                for internacion in p.internacion_set.all():
                    if internacion.fecha_obito:
                        messages.error(request, 'The patient has passed away')
                        return redirect ('sistemas.index')
                if not p.esta_internado():
                    p.telefono = form.cleaned_data['telefono']
                    p.mail = form.cleaned_data['mail']
                    p.obra_social = form.cleaned_data['obra_social']
                    p.domicilio = form.cleaned_data['domicilio']
                    p.antecedentes_personales = form.cleaned_data['antecedentes_personales']
                    p.nombre_contacto = form.cleaned_data['nombre_contacto']
                    p.apellido_contacto = form.cleaned_data['apellido_contacto']
                    p.telefono_contacto = form.cleaned_data['telefono_contacto']
                    p.parentesco_contacto = form.cleaned_data['parentesco_contacto']
                else:
                    messages.error(request, 'The patient is already hospitalized')
                    return render(
                        request,
                        "pacientes/create.html",
                        {'form': form, 'new_patient': request.POST["new_patient"]}
                    )
            else:
                form.save()

            paciente = Paciente.objects.get(dni=form.cleaned_data['dni'])

            jefe = JefeSistema.objects.filter(sistema__name="ER").first()
            paciente.medicos.add(jefe)
            paciente.save()

            free_bed.paciente = paciente
            free_bed.save()
            messages.success(request, 'Patient saved')
            return redirect("internaciones.create", id_=paciente.id)
        else:
            messages.error(request, "There are no available beds")
            render(request, "pacientes/create.html", {'form': form, 'new_patient': request.POST["new_patient"]})
    else:
        form = PacienteForm()

    return render(request, "pacientes/create.html", {'form': form, 'new_patient': "true"})


@login_required
def show(request, id_):
    current_user = request.session["username"]
    current_doctor = TrabajadorHospital.objects.get(usuario=current_user)
    paciente = Paciente.objects.get(id=id_)
    assigned_doctors = paciente.medicos.all()
    not_assigned_doctors = []
    if paciente.get_sistema():
        not_assigned_doctors = paciente.get_sistema().medico_set.all()
    has_unassigned_doctors = not all(elem in assigned_doctors for elem in not_assigned_doctors)
    internaciones = Internacion.objects.filter(paciente__id=id_).all()
    return render(
        request,
        "pacientes/show.html",
        {
            'paciente': paciente,
            "assigned_doctors": assigned_doctors,
            "not_assigned_doctors": not_assigned_doctors,
            "has_unassigned_doctors": has_unassigned_doctors,
            "internaciones": internaciones,
            "current_doctor": current_doctor,
        }
    )


@login_required
def assign_doctors(request, id_):
    paciente = Paciente.objects.get(id=id_)
    for key, value in request.POST.items():
        if key.startswith("medico"):
            medico = Medico.objects.get(id=value)
            paciente.medicos.add(medico)
    if len(paciente.medicos.all()) > 1:
        jefe = JefeSistema.objects.filter(sistema__id=paciente.get_sistema().id).first()
        if jefe in paciente.medicos.all():
            paciente.medicos.remove(jefe)
    paciente.save()
    return redirect("pacientes.show", id_=id_)


@login_required
def unassign_doctors(request, id_, id_medic):
    paciente = Paciente.objects.get(id=id_)
    medico = Medico.objects.get(id=id_medic)
    paciente.medicos.remove(medico)
    if len(paciente.medicos.all()) == 0:
        jefe = JefeSistema.objects.filter(sistema__id=paciente.get_sistema().id).first()
        if not (jefe in paciente.medicos.all()):
            paciente.medicos.add(jefe)
    paciente.save()
    return redirect("pacientes.show", id_=id_)


@login_required
def change_system(request, id_):
    paciente = Paciente.objects.get(id=id_)
    sistema = paciente.get_sistema()
    permitted_systems = sistema.get_permitted_system()
    if request.method == "POST":
        sistema_name = request.POST["sistema_name"]
        sistema_destino = Sistema.objects.get(name=sistema_name)
        free_bed = sistema_destino.get_free_bed()
        if not free_bed and sistema_destino.name == "ICU" and sistema_name == "COVID floor":
            sistema_destino = Sistema.objects.filter(name="ER").first()
            free_bed = sistema_destino.get_free_bed()
        internacion = paciente.get_internacion_activa()
        if free_bed:
            paciente.liberar_cama()
            free_bed.paciente = paciente
            free_bed.save()
            try:
                cambio_sistema = CambioSistema(
                    sistema_origen=sistema,
                    sistema_destino=sistema_destino,
                    internacion=internacion,
                )
                cambio_sistema.save()
                messages.success(request, "The system was changed succesfully")
                if request.session.get("tipo_medico") == "jefe":
                    return redirect('pacientes.show', id_=id_)
                else:
                    usuario = request.session.get("username")
                    medico = Medico.objects.get(usuario=usuario)
                    return redirect("sistemas.show", medico.sistema.name)
            except Exception:
                messages.error(request, "The patient is not hospitalized")
        else:
            messages.error(request, "There are no available beds")
            print(len(permitted_systems))
            if len(permitted_systems) == 1:
                return redirect ('internaciones.show', id_=paciente.id, id_2=internacion.id)
    return render(
        request,
        'pacientes/change_system.html',
        {"paciente": paciente, "permitted_systems": permitted_systems}
    )


@login_required
def patient_exists(request, dni):
    paciente = get_object_or_404(Paciente, dni=dni)
    result = {
        "data": {
            "nombre_y_apellido": paciente.nombre_y_apellido,
            "telefono": paciente.telefono,
            "mail": paciente.mail,
            "obra_social": paciente.obra_social,
            "domicilio": paciente.domicilio,
            "fecha_nacimiento": paciente.fecha_nacimiento,
            "nombre_contacto": paciente.nombre_contacto,
            "apellido_contacto": paciente.apellido_contacto,
            "telefono_contacto": paciente.telefono_contacto,
            "parentesco_contacto": paciente.parentesco_contacto,
            "antecedentes_personales": paciente.antecedentes_personales,
        }
    }
    return JsonResponse(result)


@login_required
def drop(request, id_):
    paciente = Paciente.objects.get(id=id_)
    internacion = paciente.get_internacion_activa()
    internacion.fecha_egreso = datetime.now()
    internacion.save()
    for medico in paciente.medicos.all():
        paciente.medicos.remove(medico)
    paciente.liberar_cama()
    paciente.alta = request.POST['tipo_alta'].capitalize()
    paciente.save()
    return redirect("pacientes.show", id_=id_)


@login_required
def obito(request, id_):
    paciente = Paciente.objects.get(id=id_)
    internacion = paciente.get_internacion_activa()
    if internacion:
        internacion.fecha_obito = datetime.now()
        internacion.save()
    for medico in paciente.medicos.all():
        paciente.medicos.remove(medico)
    paciente.liberar_cama()
    paciente.alta = "Dead"
    paciente.obito = True
    paciente.save()
    return redirect("pacientes.show", id_=id_)


@login_required
def generate_pdf(request, id_):
    paciente = Paciente.objects.get(id=id_)
    nombre = "Patient-" + paciente.nombre_y_apellido.replace(" ", "_") + ".pdf"
    c = Canvas(nombre)
    p = PdfPrinter(c, 60, 120)
    c.setTitle("Patient information")
    p.create_header("Patient " + paciente.nombre_y_apellido)
    p.horizontal_line()
    p.create_text_line("DNI", paciente.dni)
    p.create_text_line("Email", paciente.mail)
    p.create_text_line("Residence", paciente.domicilio)
    p.create_text_line("Phone number", paciente.telefono)
    p.create_text_line("Date of birth", paciente.fecha_nacimiento)
    if paciente.obra_social:
        p.create_text_line("Healthcare", paciente.obra_social)
    p.create_text_line("Personal history", paciente.antecedentes_personales + " ")
    if paciente.obito:
        p.create_text_line("Passed away", "Yes")
    p.horizontal_line()
    c.setFont("Helvetica-Bold", 16)
    c.drawString(350, 723, 'Contact information')
    p.create_contact_line("First name", paciente.nombre_contacto)
    p.create_contact_line("Last name", paciente.apellido_contacto)
    p.create_contact_line("Phone number", paciente.telefono)
    p.create_contact_line("Kinship", paciente.parentesco_contacto)
    p.create_half_title("Hospitalizations")
    for hospitalization in paciente.internacion_set.all():
        p.create_hospitalization(hospitalization)
    c.showPage()
    c.save()
    return FileResponse(open(nombre, 'rb'), content_type='application/pdf')
