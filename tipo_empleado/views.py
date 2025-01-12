from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import TipoEmpleado
from .forms import TipoEmpleadoForm

def agregar_tipo_empleado (request):
    if request.method =='POST':
        form = TipoEmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de empleado agregado exitosamente.')
            return redirect('listar_tipo_empleado')
        else:
            messages.error(request,'Este tipo de empleado ya esta registrado.')
    else:
        form = TipoEmpleadoForm()
    return render(request,'agregar_tipo_empleado.html',{'form':form})

def listar_tipo_empleado (request):
    tipos = TipoEmpleado.objects.all()
    return render(request,'listar_tipo_empleado.html',{'tipos':tipos})

def eliminar_tipo_empleado (request,id):
    tipo = get_object_or_404(TipoEmpleado,id_tipo_empleado=id)
    if request.method == 'POST':
        tipo.delete()
        messages.success(request,'Tipo de empleado eliminado exitosamente.')
        return redirect('listar_tipo_empleado')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el tipo de empleado.')
    return render(request,'listar_tipo_empleado.html')

def editar_tipo_empleado (request,nombre):
    tipo = get_object_or_404(TipoEmpleado,nombre_tipo_empleado=nombre)
    if request.method =='POST':
        form = TipoEmpleadoForm(request.POST,instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de empleado actualizado exitosamente.')
            return redirect('listar_tipo_empleado')
        else:
            messages.error(request,'Ocurrio un error al intentar editar el tipo de empleado.')
    else:
        form = TipoEmpleadoForm(instance=tipo)
    return render(request,'editar_tipo_empleado.html',{'form':form})