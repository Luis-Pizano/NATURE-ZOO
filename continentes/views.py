from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages # type: ignore
from .forms import ContinentesForm
from .models import Continentes

def agregar_continentes(request):
    if request.method =='POST':
        form = ContinentesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Continente agregado exitosamente.')
            return redirect('listar_continentes')
        else:
            messages.error(request,'Este continente ya esta registrado.')
    else:
        form = ContinentesForm()
    return render(request,'agregar_continentes.html',{'form':form})

def listar_continentes(request):
    continentes = Continentes.objects.all()
    return render(request,'listar_continentes.html',{'continentes':continentes})

def eliminar_continente(request,id):
    continente = get_object_or_404(Continentes,id_continente = id)
    if request.method =='POST':
        continente.delete()
        messages.success(request,'Continente eliminado exitosamente.')
        return redirect('listar_continentes')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el continente.')
    return render(request,'listar_continentes.html')

def editar_continente(request,nombre):
    continente = get_object_or_404(Continentes, nombre_continente=nombre)
    if request.method =='POST':
        form = ContinentesForm(request.POST,instance=continente)
        if form.is_valid():
            form.save()
            messages.success(request,'Continente actualizado exitosamente.')
            return redirect('listar_continentes')
        else:
            messages.error(request,'Este continente ya esta registrado.')
    else:
        form = ContinentesForm(instance=continente)
    return render(request,'editar_continente.html',{'form':form})