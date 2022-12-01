from django.contrib import admin

from webapp.models import Persona

# Register your models here.

'''
Aqui se van regsitrando los modelos que vamos creando para poder usarlos desde el panel de administracion
'''
admin.site.register(Persona)