# Generated by Django 3.1.2 on 2020-12-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionRegla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'configuracion_reglas',
            },
        ),
    ]
