# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    desc_servicio = models.CharField(max_length=50)
    valor_servicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'

class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    rut_empleado = models.IntegerField()
    dv_empleado = models.CharField(max_length=1)
    p_nombre_empleado = models.CharField(max_length=25)
    s_nombre_empleado = models.CharField(max_length=25)
    p_apellido_empleado = models.CharField(max_length=25)
    s_apellido_empleado = models.CharField(max_length=25)
    direccion_empleado = models.CharField(max_length=25)
    numeracion_empleado = models.CharField(max_length=6)
    depto_empleado = models.CharField(max_length=6, blank=True, null=True)
    fono_empleado = models.IntegerField()
    correo_empleado = models.CharField(max_length=25)
    nombre_usu_empleado = models.CharField(max_length=25)
    contrasena_empleado = models.CharField(max_length=25)
    id_comuna = models.IntegerField()
    id_taller = models.IntegerField()
    id_cargo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'empleado'        