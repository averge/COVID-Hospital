# Generated by Django 3.1.2 on 2020-10-24 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20201022_1816'),
        ('sistemas', '0004_auto_20201024_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cama',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pacientes.paciente'),
        ),
    ]
