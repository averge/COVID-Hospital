from django.db import models

from evoluciones.forms import EvolucionForm
from evoluciones.models import Evolucion
from pacientes.models import Internacion
from .models import ConfiguracionRegla, Alerta
from datetime import date
from datetime import datetime
from evoluciones import forms


# Si somnolencia => Evaluar pase a UTI
def tiene_somnolencia(somnolencia):
    if somnolencia:
        return "Somnolence. Evaluate transfer to UTI"
    else:
        return "No action required"


# Si tiene mecanica ventilatoria regular o mala => Mecánica ventilatoria {valor}, evaluar pase a UTI
def mecanica_ventilatoria (valor):
    if valor == "regular":
        return "Regular respiratory mechanics. Evaluate transfer to UTI"
    elif valor == "bad":
        return "Bad respiratory mechanics. Evaluate transfer to UTI"
    else:
        return "No action required"


# Si FR > 30 minutos (configurable) => Frecuencia respiratoria mayor a 30, evaluar pase a UTI
def frecuencia_respiratoria (valor):
    configurable = ConfiguracionRegla.get_frecuencia_respiratoria()
    if configurable is None:
        return "No hay configurada una regla"
    if valor > configurable:
        return "Respiratory rate more than optimal (" + str(configurable) + "). Evaluate transfer to UTI"
    else:
        return "No action required"


# Si pasaron 10 dias desde el inicio de los sintomas => Pasaron 10 dias del inicio de los sintomas, evaluar alta
def diez_dias (inicio):
    hoy = datetime.today().date()
    datediff = hoy - inicio
    days = datediff.days
    if days >= 10:
        return "10 days passed from the onset of symptoms. Evaluate discharge"
    else:
        return "No action required"


# Si saturacion de oxigeno < 92% (configurable) => Saturación de oxigeno menor a 92%, evaluar oxigeno, terapia y prono
def saturacion_oxigeno (valor):
    configurable = ConfiguracionRegla.get_saturacion_oxigeno()
    if configurable is None:
        return "No hay configurada una regla"
    if valor:
        if valor < configurable:
            return "Oxygen saturation less than optimal (" + str(configurable) + "). Evaluate oxygen, therapy and prono"
    return "No action required"


# Si saturacion de oxigeno bajo 3% respecto de la evolucion anterior y no salto la regla 5 (no se debe usar un o logico
# corriendo la regla anterior) => Saturacion de oxigeno bajo un 3%, evaluar oxigeno, terapia y prono
def evolucion_oxigeno (anterior, valor, regla_saturacion_oxigeno_valor):
    if anterior and valor:
        if (((anterior - valor)/anterior)*100) >= 3 and regla_saturacion_oxigeno_valor:
            return "Oxygen saturation dropped more than 3%. Evaluate oxygen, therapy and prono"
    return "No action required"


# Para ejecutar las funciones crear alerta, habria que importar el modulo alerta, se puede cambiar el orden de los
# parametros, es para tener una idea el print esta para que no tire error, despues habria que borrarlos
def correr_reglas(form, paciente):
    internacion = paciente.get_internacion_activa()

    regla_somnolencia = tiene_somnolencia(form.somnolencia)
    if regla_somnolencia != "No action required":
        a = Alerta(texto=regla_somnolencia, condicion="Tiene somnolencia", paciente=paciente)
        a.save()

    regla_mecanica_ventilaoria = mecanica_ventilatoria(form.mecanica_ventilatoria)
    if regla_mecanica_ventilaoria != "No action required":
        a = Alerta(texto=regla_mecanica_ventilaoria, condicion="Mecanica ventilatoria regular o mala", paciente=paciente)
        a.save()

    regla_frecuencia_respiratoria = frecuencia_respiratoria(form.frecuencia_respiratoria)
    if regla_frecuencia_respiratoria != "No action required":
        a = Alerta(texto=regla_frecuencia_respiratoria, condicion="Frecuencia respiratoria alta", paciente=paciente)
        a.save()

    inicio = internacion.fecha_inicio_sintomas
    regla_diez_dias = diez_dias(inicio)
    if regla_diez_dias != "No action required":
        a = Alerta(texto=regla_diez_dias, condicion="Diez dias desde el inicio de los sintomas", paciente=paciente)
        a.save()

    regla_saturacion_oxigeno = saturacion_oxigeno(form.saturacion_o2)
    regla_saturacion_oxigeno_valor = False
    if regla_saturacion_oxigeno != "No action required":
        regla_saturacion_oxigeno_valor = True
        a = Alerta(texto=regla_saturacion_oxigeno, condicion="Saturacion de oxigeno baja", paciente=paciente)
        a.save()

    evoluciones = Evolucion.objects.filter(internacion=internacion).order_by("-fecha_carga", "-hora_carga")
    evolucion = None
    if len(evoluciones.all()) > 1:
        evolucion = evoluciones[1]
    if evolucion:
        anterior = evolucion.saturacion_o2
        regla_evolucion_oxigeno = evolucion_oxigeno(anterior, form.saturacion_o2, regla_saturacion_oxigeno_valor)
        if regla_evolucion_oxigeno != "No action required":
            a = Alerta(texto=regla_evolucion_oxigeno, condicion="Evolucion de oxigeno baja", paciente=paciente)
            a.save()
