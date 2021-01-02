from django.db import models
from pacientes.models import Paciente


class ConfiguracionRegla(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __repr__(self):
        return f"{self.key} {self.value}"

    def __str__(self):
        return f"{self.key} {self.value}"

    @staticmethod
    def get_frecuencia_respiratoria():
        valor = ConfiguracionRegla.objects.get(key="frecuencia_respiratoria").value
        if valor:
            return int(valor)

    @staticmethod
    def get_saturacion_oxigeno():
        valor = ConfiguracionRegla.objects.get(key="saturacion_oxigeno").value
        if valor:
            return int(valor)

    class Meta:
        db_table = "configuracion_reglas"


class Alerta(models.Model):
    texto = models.CharField(max_length=255)
    condicion = models.CharField(max_length=255, blank=True, null=True)
    vista = models.BooleanField(default=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='alertas')

    def __repr__(self):
        return f"{self.texto} for patient {self.paciente.nombre_y_apellido}"

    def __str__(self):
        return f"{self.texto} for patient {self.paciente.nombre_y_apellido}"

    class Meta:
        db_table = "alertas"
