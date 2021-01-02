# Generated by Django 3.1.2 on 2020-11-17 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0014_auto_20201113_1424'),
        ('evoluciones', '0006_auto_20201117_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evolucion',
            name='internacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evoluciones', to='pacientes.internacion'),
        ),
    ]