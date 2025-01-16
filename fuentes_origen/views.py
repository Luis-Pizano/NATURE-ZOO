from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import FuentesOrigen
from .forms import FuentesOrigenForm,FuentesOrigenEditForm

def agregar_fuente_origen (request):
    if request.method =='POST':
        form = FuentesOrigenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Fuente de origen agregada exitosamente.')
            return redirect('listar_fuentes_origen')
        else:
            messages.error(request,'Esta fuente de origen ya esta registrada.')
    else:
        form = FuentesOrigenForm()
    return render(request,'agregar_fuente_origen.html',{'form':form})

def listar_fuentes_origen (request):
    fuentes = FuentesOrigen.objects.all()
    return render(request,'listar_fuentes_origen.html',{'fuentes':fuentes})

def eliminar_fuente_origen (request,id):
    fuente = get_object_or_404(FuentesOrigen,id_fuente_origen=id)
    if request.method =='POST':
        fuente.delete()
        messages.success(request,'Fuente de origen eliminada exitosamete.')
        return redirect('listar_fuentes_origen')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar la fuente de origen.')
    return render(request,'listar_fuentes_origen.html')

def editar_fuente_origen (request,nombre):
    fuente = get_object_or_404(FuentesOrigen,nombre_fuente_origen=nombre)
    if request.method =='POST':
        form = FuentesOrigenEditForm(request.POST,instance=fuente)
        if form.is_valid():
            form.save()
            messages.success(request,'Fuente de origen actualizado exitosamente.')
            return redirect('listar_fuentes_origen')
        else:
            messages.error(request,'Ocurrio un error al intentar actualizar la fuente de origen.')
    else:
        form = FuentesOrigenEditForm(instance=fuente)
    return render(request,'editar_fuente_origen.html',{'form':form})