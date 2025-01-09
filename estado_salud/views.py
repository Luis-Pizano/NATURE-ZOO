from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages # type: ignore
from .models import EstadoSalud
from .forms import EstadoSaludForm,EstadoSaludEditForm

def agregar_estado_salud(request):
    if request.method =='POST':
        form = EstadoSaludForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Estado de salud agregado exitosamente.')
            return redirect('listar_estados_salud')
        else:
            messages.error(request,'Este estado de salud ya esta registrado.')
    else:
        form = EstadoSaludForm()
    return render(request,'agregar_estado_salud.html',{'form':form})

def listar_estado_salud (request):
    estados = EstadoSalud.objects.all()
    return render(request,'listar_estados_salud.html',{'estados':estados})

def eliminar_estado_salud (request,id):
    estado = get_object_or_404(EstadoSalud,id_estado_salud=id)
    if request.method =='POST':
        estado.delete()
        messages.success(request,'Estado de salud eliminado exitosamente.')
        return redirect('listar_estados_salud')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el estado de salud.')
    return redirect('listar_estados_salud')

def editar_estado_salud(request,nombre):
    estado = get_object_or_404(EstadoSalud,nombre_estado_salud=nombre)
    if request.method =='POST':
        form = EstadoSaludEditForm(request.POST,instance=estado)
        if form.is_valid():
            form.save()
            messages.success(request,'Estado de salud actualizado exitosamente.')
            return redirect('listar_estados_salud')
        else:
            messages.error(request,'Ocurrio un error al intentar actualizar el estado de salud.')
    else:
        form = EstadoSaludEditForm(instance=estado)
    return render(request,'editar_estado_salud.html',{'form':form})