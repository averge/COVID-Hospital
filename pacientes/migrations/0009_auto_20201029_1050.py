# Generated by Django 3.1.2 on 2020-10-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0008_auto_20201029_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='alta',
            field=models.CharField(blank=True, choices=[('E', 'epidemiologica'), ('C', 'curado')], max_length=1, null=True),
        ),
    ]
