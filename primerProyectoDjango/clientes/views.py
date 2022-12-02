from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404

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

def delete_client_template(request):
    if request.method == "POST":
        id = request.POST['id_cliente']
        # cliente = Cliente.objects.get(pk=id_cliente) #devuelve el cliente que tiene ese identificador
        cliente = get_object_or_404(Cliente, pk=id) #para que duvuelva un error si no existe el id
        cliente.delete()

    print('Cliente borrado desde formulario')
    return render(request, 'delete_client.html')

def delete_client(request,id):
    print(f'{id}')
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    print('Cliente borrado desde url')
    return render(request, 'delete_client.html')

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