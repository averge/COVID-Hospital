# Generated by Django 3.1.2 on 2020-11-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evoluciones', '0004_auto_20201117_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evolucion',
            name='anosmia',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='arm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='descripcion_arm',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='descripcion_patologico_ecg',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='descripcion_patologico_rx_tx',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='descripcion_patologico_tac_torax',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='descripcion_pcr_covid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='descripcion_vasopresores',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='disgeusia',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='disnea',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='ecg',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='estabilidad_respiratoria',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='pafi',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='pafi_valor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='pcr_covid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='prono_vigil',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='rx_tx',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='somnolencia',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='tac_torax',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='tipo_ecg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='tipo_pcr_covid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='tipo_rx_tx',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='tipo_tac_torax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='tos',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='traqueostomia',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='vasopresores',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
