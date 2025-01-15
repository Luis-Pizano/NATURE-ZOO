from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Sexo
from .forms import SexoForm

def agregar_sexo (request):
    if request.method =='POST':
        form = SexoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Sexo agregado exitosamente.')
            return redirect('listar_sexos')
        else:
            messages.error(request,'Este sexo ya esta registrado.')
    else:
        form = SexoForm()
    return render(request,'agregar_sexo.html',{'form':form})

def listar_sexos (request):
    sexos = Sexo.objects.all()
    return render(request,'listar_sexos.html',{'sexos':sexos})

def eliminar_sexo (request,id):
    sexo = get_object_or_404(Sexo,id_sexo=id)
    if request.method =='POST':
        sexo.delete()
        messages.success(request,'Sexo eliminado exitosamente.')
        return redirect('listar_sexos')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el sexo.')
    return render(request,'listar_sexos.html')

def editar_sexo (request,nombre):
    sexo = get_object_or_404(Sexo,nombre_sexo=nombre)
    if request.method =='POST':
        form = SexoForm(request.POST,instance=sexo)
        if form.is_valid():
            form.save()
            messages.success(request,'Sexo actualizado exitosamente.')
            return redirect('listar_sexos')
        else:
            messages.error(request,'Este sexo ya esta registrado.')
    else:
        form = SexoForm(instance=sexo)
    return render(request,'editar_sexo.html',{'form':form})