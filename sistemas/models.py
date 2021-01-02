from django.db import models
from django.utils import timezone

permitted_systems = {
    "ER": ["ICU", "COVID floor"],
    "COVID floor": ["Hotel", "Residence", "ICU"],
    "ICU": ["COVID floor"],
    "Hotel": ["COVID floor"],
    "Residence": ["COVID floor"],
}


class Sistema(models.Model):
    name = models.CharField(max_length=255)
    camas_infinitas = models.BooleanField(default=False)

    def camas_totales(self):
        total = 0
        for sala in self.sala_set.all():
            total += len(sala.cama_set.all())
        return total

    def camas_ocupadas(self):
        total = 0
        for sala in self.sala_set.all():
            for cama in sala.cama_set.all():
                if cama.paciente:
                    total += 1
        return total

    def camas_libres(self):
        total = 0
        for sala in self.sala_set.all():
            for cama in sala.cama_set.all():
                if not cama.paciente:
                    total += 1
        return total

    def get_free_bed(self):
        if not self.camas_infinitas:
            for ward in self.sala_set.all():
                for bed in ward.cama_set.all():
                    if not bed.paciente:
                        return bed
        else:
            ward = self.sala_set.first()
            if ward:
                for bed in ward.cama_set.all():
                    if not bed.paciente:
                        return bed
                cant_camas = len(ward.cama_set.all())
                bed = Cama(name="cama " + str(cant_camas), sala=ward)
                bed.save()
                return bed
            else:
                ward = Sala(name="sala", sistema=self)
                ward.save()
                bed = Cama(name="cama 1", sala=ward)
                bed.save()
                return bed

    def get_permitted_system(self):
        return permitted_systems[str(self.name)]

    def __repr__(self):
        return f"{self.name} system"

    def __str__(self):
        return f"{self.name} system"

    class Meta:
        db_table = "sistemas"


class Sala(models.Model):
    name = models.CharField(max_length=255)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.name} in {self.sistema.name} system"

    def __str__(self):
        return f"{self.name} in {self.sistema.name} system"

    class Meta:
        db_table = "salas"


class Cama(models.Model):
    name = models.CharField(max_length=255)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    paciente = models.ForeignKey(
        to='pacientes.Paciente',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def get_sistema(self):
        return self.sala.sistema

    def __repr__(self):
        return f"{self.name} in {self.sala.name} ward"

    def __str__(self):
        return f"{self.name} in {self.sala.name} ward"

    class Meta:
        db_table = "camas"


class CambioSistema(models.Model):
    sistema_origen = models.ForeignKey(
        to='sistemas.Sistema',
        on_delete=models.DO_NOTHING,
        related_name="sistema_origen",
    )
    sistema_destino = models.ForeignKey(
        to='sistemas.Sistema',
        on_delete=models.DO_NOTHING,
        related_name="sistema_destino",
    )
    fecha_cambio = models.DateField(default=timezone.now)
    hora_cambio = models.TimeField(default=timezone.now)
    internacion = models.ForeignKey(
        to='pacientes.Internacion',
        on_delete=models.CASCADE,
        related_name="cambio_de_sistema",
    )

    def __repr__(self):
        return f"Change from system {self.sistema_origen.name} to {self.sistema_destino.name}"

    def __str__(self):
        return f"Change from system {self.sistema_origen.name} to {self.sistema_destino.name}"

    class Meta:
        db_table = "cambio_sistema"
