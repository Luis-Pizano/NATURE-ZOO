from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Empleados
from .forms import EmpleadosForm

def agregar_empleado (request):
    if request.method =='POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Empleado agregado exitosamente.')
            return redirect('listar_empleados')
        else:
            messages.error(request,'El correo o telefono ya han sido registrados.')
    else:
        form = EmpleadosForm()
    return render(request,'agregar_empleado.html',{'form':form})

def listar_empleados (request):
    empleados = Empleados.objects.all()
    return render(request,'listar_empleados.html',{'empleados':empleados})

def eliminar_empleado (request,id):
    empleado = get_object_or_404(Empleados,id_empleado=id)
    if request.method =='POST':
        empleado.delete()
        messages.success(request,'Empleado eliminado exitosamente.')
        return redirect('listar_empleados')
    else:
        messages.error(request,f'Ocurrio un error al intentar eliminar al empleado de ID {id}.')
    return render(request,'listar_empleados.html')

def editar_empleado (request,id):
    empleado = get_object_or_404(Empleados,id_empleado=id)
    if request.method =='POST':
        form = EmpleadosForm(request.POST,instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request,'Empleado actualizado exitosamente.')
            return redirect('listar_empleados')
        else:
            messages.error(request,f'Ocurrio un error al intentar editar al empleado de ID {id}.')
    else:
        form = EmpleadosForm(instance=empleado)
    return render(request,'editar_empleado.html',{'form':form})