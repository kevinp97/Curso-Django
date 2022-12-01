from django.forms import modelform_factory
from django.shortcuts import render

from clientes.models import Cliente

#metodo django para simular clases
# le tengo que decir de que clase tengo que crear el formulario, de esta forma se recoje automatico y no como hemos hecho nosotros
# si queremos quitar email, por ejemplo, pondriamos en exclude email
ClientForm = modelform_factory(Cliente, exclude=[])
def aniadir_clientes(request):
    mensaje = ''
    if request.method == 'POST':
        cliente_form = ClientForm(request.POST)
        cliente_form.save()
        mensaje = 'Cliente registrado'


    cliente_form = ClientForm() #para que devuelva vacio el formulario

    contexto = {"mensaje": mensaje, "cliente_form":cliente_form}
    return render(request, "clientes.html", contexto)

# Modo recogiendo datos
# def aniadir_clientes(request):
#     '''
#     HTML llama al action que se mira en url y desde ahi se llama a views
#     '''
#     mensaje = ''
#     if request.method == 'POST':
#         # recogemos los cambios
#         nombre = request.POST["nombre"]
#         apellidos = request.POST["apellidos"]
#         dni = request.POST["dni"]
#         email = request.POST["email"]
#         mensaje = 'Cliente registrado'
#         #creamos el objeto con la clase de models
#         cliente = Cliente(nombre=nombre, apellidos=apellidos, dni=dni, email=email)
#         cliente.save()
#
#     contexto = {"mensaje": mensaje}
#     return render(request, "clientes.html", contexto)