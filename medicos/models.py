from django.db import models
from polymorphic.models import PolymorphicModel


class TrabajadorHospital(PolymorphicModel):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    legajo = models.IntegerField()
    mail = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Medico(TrabajadorHospital):
    sistema = models.ForeignKey(to='sistemas.Sistema', on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"Doctor {self.nombre} in {self.sistema.name} system"

    def __str__(self):
        return f"Doctor {self.nombre} in {self.sistema.name} system"
    
    @property
    def es_jefe(self):
        return False

    class Meta:
        db_table = "medicos"


class JefeSistema(TrabajadorHospital):
    sistema = models.OneToOneField(
        to='sistemas.Sistema',
        on_delete=models.DO_NOTHING,
    )

    def __repr__(self):
        return f"Chief medical doctor {self.nombre} of {self.sistema.name} system"

    def __str__(self):
        return f"Chief medical doctor {self.nombre} of {self.sistema.name} system"

    @property
    def es_jefe(self):
        return True

    class Meta:
        db_table = "jefes"
