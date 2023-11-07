from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.template import Template
from formulario_sena.models import Lugar,Formulario
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q






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


def EdicionLugar(request, Id_Lugar):
    lugar = Lugar.objects.get(Id_Lugar=Id_Lugar)
    context = {
        'lugar':lugar
    }
    return render(request, "Lugar/ActualizarLugar.html", context)

def EdtitarLugar(request):
    id = int(request.POST['Id'])
    LugarEvento = request.POST['LugarEvento']
    
    lugar = Lugar.objects.get(Id_Lugar = id)
    lugar.LugarEvento = LugarEvento
    lugar.save()
    
    return redirect('/VerLugar/')

def EliminarLugar(request, Id_Lugar):
    lugar = Lugar.objects.get(Id_Lugar=Id_Lugar)
    lugar.delete()
    return redirect('/VerLugar/')
    

#endregion

#region formulario principal
def Index(request):
    if request.method == "POST":
        NombreCompleto = request.POST.get('NombreCompleto')
        NumeroDocumento = request.POST.get('NumeroDocumento')
        Planta = request.POST.get('Planta')
        Dependencia = request.POST.get('Dependencia')
        Correo = request.POST.get('Correo')
        Telefono = request.POST.get('Telefono')
        Autorizacion = request.POST.get('Autorizacion')
        LugarEvento_Id = request.POST.get('LugarEvento_Id')
        
        lugar = Lugar.objects.get(Id_Lugar=LugarEvento_Id)
  
        formulario = Formulario.objects.create(
    NombreCompleto=NombreCompleto,
    NumeroDocumento=NumeroDocumento,
    Planta=Planta,
    Dependencia=Dependencia,
    Correo=Correo,
    Telefono=Telefono,
    Autorizacion=Autorizacion,
    LugarEvento_Id=lugar  # Asigna la instancia de Lugar, no solo el ID
)
        
        return redirect('/Index')     
    else:
        lugar = Lugar.objects.filter()   
        return render(request, "Index.html",{'lugar' : lugar})
    
    
def VerFormulario(request):
    busqueda = request.POST.get("Buscador")
    formulario = Formulario.objects.all()
    
    if busqueda:
            formulario = Formulario.objects.filter(
            Q(NombreCompleto__icontains = busqueda) |
            Q(NumeroDocumento__icontains = busqueda) |
            Q(Correo__icontains = busqueda) |
            Q(Telefono__icontains = busqueda) |
            Q(LugarEvento_Id__LugarEvento__icontains = busqueda)
            ).distinct()
    
    return render(request, "Formulario/VerFormulario.html", {'formulario':formulario})

def EdicionFormulario(request, Id_Formulario):
    lugar = Lugar.objects.all()
    formulario = Formulario.objects.get(Id_Formulario=Id_Formulario)
    
    context = {
        'formulario':formulario,
        'lugar':lugar
    }
    return render(request, "Formulario/ActualizarFormulario.html", context)

def EdtitarFormulario(request):
    id = int(request.POST['Id'])
    NombreCompleto = request.POST['NombreCompleto']
    NumeroDocumento = request.POST['NumeroDocumento']
    Planta = request.POST['Planta']
    Dependencia = request.POST['Dependencia']
    Correo = request.POST['Correo']
    Telefono = request.POST['Telefono']
    Autorizacion = request.POST['Autorizacion']
    
    form = Formulario.objects.get(Id_Formulario = id)
    form.NombreCompleto = NombreCompleto
    form.NumeroDocumento = NumeroDocumento
    form.Planta = Planta
    form.Dependencia = Dependencia
    form.Correo = Correo
    form.Telefono = Telefono
    form.Autorizacion = Autorizacion
    form.save()
    
    return redirect('/VerFormulario/')

def EliminarFormulario(request, Id_Formulario):
    form = Formulario.objects.get(Id_Formulario=Id_Formulario)
    form.delete()
    return redirect('/VerFormulario/')
#endregion