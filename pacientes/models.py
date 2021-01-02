from django.db import models
from medicos.models import TrabajadorHospital
from django.utils import timezone
from sistemas.models import Cama


class Paciente(models.Model):
    antecedentes_personales = models.TextField()
    alta = models.CharField(null=True, blank=True, max_length=255)
    obito = models.BooleanField(default=False)
    nombre_y_apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    mail = models.CharField(max_length=255)
    obra_social = models.TextField(null=True)
    dni = models.IntegerField()
    domicilio = models.TextField()
    nombre_contacto = models.CharField(max_length=255)
    apellido_contacto = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=255)
    parentesco_contacto = models.TextField()
    medicos = models.ManyToManyField(TrabajadorHospital)

    def get_sistema(self):
        cama = Cama.objects.filter(paciente__id=self.id).first()
        if cama:
            return Cama.objects.filter(paciente__id=self.id).first().get_sistema()

    def get_internacion_activa(self):
        internaciones = Internacion.objects.filter(paciente__id=self.id).all()
        for internacion in internaciones:
            if not internacion.fecha_egreso and not internacion.fecha_obito:
                return internacion

    def esta_internado(self):
        internaciones = Internacion.objects.filter(paciente__id=self.id).all()
        for internacion in internaciones:
            if not internacion.fecha_egreso and not internacion.fecha_obito:
                return True
        return False

    def liberar_cama(self):
        current_bed = Cama.objects.filter(paciente__id=self.id).first()
        current_bed.paciente = None
        current_bed.save()

    def __repr__(self):
        return f"Patient {self.nombre_y_apellido}"

    def __str__(self):
        return f"Patient {self.nombre_y_apellido}"

    class Meta:
        db_table = "pacientes"


class Internacion(models.Model):
    fecha_inicio_sintomas = models.DateField(blank=True, null=True)
    fecha_diagnostico = models.DateField(blank=True, null=True)
    enfermedad_actual = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_internacion = models.DateField(default=timezone.now)
    fecha_egreso = models.DateField(blank=True, null=True)
    fecha_obito = models.DateField(blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Hospitalization {self.fecha_inicio_sintomas}"

    def __str__(self):
        return f"Hospitalization {self.fecha_inicio_sintomas}"

    class Meta:
        db_table = "internaciones"
