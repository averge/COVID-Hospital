from django.urls import path

from .views import paciente, internacion
from evoluciones import views as v_evoluciones

urlpatterns = [
    path('<int:id_>/show/', paciente.show, name='pacientes.show'),
    path('create/', paciente.create, name='pacientes.create'),
    path('api/patient_exists/<int:dni>', paciente.patient_exists, name='pacientes.patient_exists'),
    path('<int:id_>/assign_doctors/', paciente.assign_doctors, name='pacientes.assign_doctors'),
    path('<int:id_>/generate_pdf/', paciente.generate_pdf, name='pacientes.generate_pdf'),
    path('<int:id_>/unassign_doctors/<int:id_medic>/', paciente.unassign_doctors, name='pacientes.unassign_doctors'),
    path('<int:id_>/change_system/', paciente.change_system, name='pacientes.change_system'),
    path('<int:id_>/drop/', paciente.drop, name='pacientes.drop'),
    path('<int:id_>/obito/', paciente.obito, name='pacientes.obito'),
    path('<int:id_>/hospitalization/create/', internacion.create, name="internaciones.create"),
    path('<int:id_>/hospitalization/<int:id_2>/show/', internacion.show, name="internaciones.show"),
    path('<int:id_p>/hospitalization/<int:id_i>/evoluciones/create/', v_evoluciones.create, name="evoluciones.create"),
]