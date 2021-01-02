from django.db import models
from django.utils import timezone


class Evolucion(models.Model):
    fecha_carga = models.DateField(default=timezone.now)
    hora_carga = models.TimeField(default=timezone.now)
    temperatura = models.DecimalField(max_digits=5, decimal_places=1)
    ta_sistolica = models.IntegerField()
    ta_diastolica = models.IntegerField()
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    mecanica_ventilatoria = models.CharField(max_length=255)
    requiere_o2_suplementario = models.BooleanField(default=False, null=True, blank=True)
    canula_nasal = models.IntegerField(null=True, blank=True)
    mascara_con_reservorio = models.IntegerField(null=True, blank=True)
    saturacion_o2 = models.IntegerField(null=True, blank=True)
    pafi = models.BooleanField(default=False, null=True, blank=True)
    pafi_valor = models.IntegerField(null=True, blank=True)
    prono_vigil = models.BooleanField(default=False, null=True, blank=True)
    tos = models.BooleanField(default=False, null=True, blank=True)
    disnea = models.IntegerField(null=True, blank=True)
    estabilidad_respiratoria = models.BooleanField(default=False, null=True, blank=True)
    somnolencia = models.BooleanField(default=False, null=True, blank=True)
    anosmia = models.BooleanField(default=False, null=True, blank=True)
    disgeusia = models.BooleanField(default=False, null=True, blank=True)
    rx_tx = models.BooleanField(default=False, null=True, blank=True)
    tipo_rx_tx = models.CharField(max_length=255, null=True, blank=True)
    descripcion_patologico_rx_tx = models.TextField(null=True, blank=True)
    tac_torax = models.BooleanField(default=False, null=True, blank=True)
    tipo_tac_torax = models.CharField(max_length=255, null=True, blank=True)
    descripcion_patologico_tac_torax = models.TextField(null=True, blank=True)
    ecg = models.BooleanField(default=False, null=True, blank=True)
    tipo_ecg = models.CharField(max_length=255, null=True, blank=True)
    descripcion_patologico_ecg = models.TextField(null=True, blank=True)
    pcr_covid = models.BooleanField(default=False, null=True, blank=True)
    tipo_pcr_covid = models.CharField(max_length=255, null=True, blank=True)
    descripcion_pcr_covid = models.TextField(null=True, blank=True)
    observacion = models.TextField()
    arm = models.BooleanField(default=False, null=True, blank=True)
    descripcion_arm = models.TextField(null=True, blank=True)
    traqueostomia = models.BooleanField(default=False, null=True, blank=True)
    vasopresores = models.BooleanField(default=False, null=True, blank=True)
    descripcion_vasopresores = models.TextField(null=True, blank=True)
    internacion = models.ForeignKey(
        to="pacientes.Internacion",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="evoluciones",
    )

    def __repr__(self):
        return f"Evolution for hospitalization {self.internacion.id}"

    def __str__(self):
        return f"Evolution for hospitalization {self.internacion.id}"
