# from distutils.command.upload import upload  # esta instrucción es para subir imagenes
from email.policy import default
from django.db import models

# Create your models here.

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    habitacion = models.IntegerField(verbose_name='Habitación',null=True)
    cama = models.IntegerField(verbose_name='Cama',null=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=40)
    apellido = models.CharField(verbose_name='Apellido', max_length=30)
    diagnostico = models.CharField(verbose_name='Diagnóstico', max_length=30)
    observaciones = models.TextField(verbose_name='Observaciones')
    desayuno = models.CharField(verbose_name='Desayuno', null=True, max_length=50)
    colacion_maniana = models.CharField(verbose_name='Colación M', null=True, max_length=50)
    almuerzo = models.CharField(verbose_name='Almuerzo', null=True, max_length=50)
    merienda = models.CharField(verbose_name='Merienda', null=True, max_length=50)
    colacion_tarde = models.CharField(verbose_name='Colación T', null=True, max_length=50)
    cena = models.CharField(verbose_name='Cena', null=True, max_length=50)
    postre = models.CharField(verbose_name='Postre', null=True, max_length=30)
    comida_familiar = models.CharField(verbose_name='Comida Familiar', null=True, max_length=30)
    comentarios = models.TextField(verbose_name='Comentarios')

    def __str__(self):
        fila="Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    