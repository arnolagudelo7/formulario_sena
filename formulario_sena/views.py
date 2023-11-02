from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.template import Template
from formulario_sena.models import Lugar
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

#region formulario principal
def Index(request):
    return render(request, "Index.html")
#endregion


#region Ingreso login
def Registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            #redirigir
            return redirect(to="Index")
        data["form"] = formulario
    
    return render(request, "registration/registro.html", data)
#endregion


#region lugar evento
def LugarEventoCrear(request):
    if request.method == "POST":
        lugar = Lugar()
        lugar.LugarEvento = request.POST.get('LugarEvento')
        lugar.save()
        
        return redirect("/VerLugar/")
    else:
        return render(request, "Lugar/CrearLugar.html")
    
    
    
def VerLugar(request):
    lugar = Lugar.objects.all()
    return render(request, "Lugar/VerLugar.html", {'lugar':lugar})

def ActualizarLugar(request, Id_Lugar):
    lugar = get_object_or_404(Lugar, Id_Lugar=Id_Lugar)
    
    if request.method == 'POST':
        LugarEvento = request.POST['LugarEvento']

        # Obtener otros campos del formulario según sea necesario
        
        # Actualizar los campos del objeto lugar
        lugar.LugarEvento = LugarEvento

        # Actualiza otros campos del modelo Lugar según sea necesario
        lugar.save()
        
        # Redirigir a una página de éxito o renderizar un template de éxito
        return redirect("/")
    
    # Si la solicitud no es POST, mostrar el formulario para editar el lugar
    context = {
        'lugar': lugar
    }
    return render(request, "Lugar/ActualizarLugar.html", context)
    
    

#endregion