# Generated by Django 3.1.2 on 2020-11-07 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0013_auto_20201106_0011'),
        ('sistemas', '0006_cambiosistema'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambiosistema',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='pacientes.paciente'),
            preserve_default=False,
        ),
    ]
