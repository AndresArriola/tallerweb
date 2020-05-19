# Generated by Django 2.2.12 on 2020-05-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('rut_empleado', models.IntegerField()),
                ('dv_empleado', models.CharField(max_length=1)),
                ('p_nombre_empleado', models.CharField(max_length=25)),
                ('s_nombre_empleado', models.CharField(max_length=25)),
                ('p_apellido_empleado', models.CharField(max_length=25)),
                ('s_apellido_empleado', models.CharField(max_length=25)),
                ('direccion_empleado', models.CharField(max_length=25)),
                ('numeracion_empleado', models.CharField(max_length=6)),
                ('depto_empleado', models.CharField(blank=True, max_length=6, null=True)),
                ('fono_empleado', models.IntegerField()),
                ('correo_empleado', models.CharField(max_length=25)),
                ('nombre_usu_empleado', models.CharField(max_length=25)),
                ('contrasena_empleado', models.CharField(max_length=25)),
                ('id_comuna', models.IntegerField()),
                ('id_taller', models.IntegerField()),
                ('id_cargo', models.BooleanField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
    ]
