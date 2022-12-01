from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40) #nombre con 40 caracteres como maximo
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    '''
    python manage.py makemigrations para mirar modelos que hemos migrado y crea un 
    fichero con los campos que hay que aplicar cambios en la base de datos
    El nuevo fichero no se refresca automaticamente, sino que hay que ejecutar de nuevo el comando
    pero antes hay que eliminar el fichero que se ha creado o pasarlo a la base de datos antes de volver a añadirlo
    para actualizar la base de datos 
    Si queremos ver lo que va a generar hay que hacer lo siguiente:
    python manage.py sqlmigrate webapp 0001 0001 es los cambios que migran
    Para ejecutar los cambios en la base de datos: python manage.py migrate 
    '''
    email = models.CharField(max_length=100)
    '''
    Para crear un superusuario de admin de django: python manage.py createsuperuser
    Desde ahi, una vez añadido en admin.py lo veremos en el panel y podemos rellenar los datos de la tabla
    '''

    def __str__(self):
        return f'{self.id} {self.nombre} {self.apellidos} {self.dni} {self.email}'