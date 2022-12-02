from django.db import models

# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    equipo = models.CharField(max_length=40)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.id} {self.nombre} {self.equipo} {self.edad} {self.posicion} {self.nacionalidad}'

