from django.shortcuts import get_object_or_404, redirect, render # type: ignore
from django.contrib import messages # type: ignore
from .models import TipoAlimentacion
from .forms import TipoAlimentacionForm

def agregar_tipo(request):
    if request.method == 'POST':
        form = TipoAlimentacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Tipo de alimentación agregada exitosamente.")
            return redirect('listar_alimentacion')
        else:
            messages.error(request,"Este tipo de alimentación ya está registrada.")
    else:
        form = TipoAlimentacionForm()
    return render(request,'agregar_tipo_alimentacion.html',{'form':form})

def listar_tipo_alimentacion(request):
    tipos = TipoAlimentacion.objects.all()
    return render(request,'listar_tipos_alimentacion.html',{'tipos':tipos})

def eliminar_tipo_alimentacion(request,id):
    tipo = get_object_or_404(TipoAlimentacion,id_tipo_alimentacion=id)
    if request.method =='POST':
        tipo.delete()
        messages.success(request,"Tipo de alimentación eliminada exitosamente.")
        return redirect('listar_alimentacion')
    else:
        messages.error(request,"Ocurrio un error al intentar eliminar el tipo de alimentación.")
    return render(request,'listar_tipos_alimentacion.html')

def editar_tipo_alimentacion(request, nombre):
    tipo = get_object_or_404(TipoAlimentacion, nombre_tipo_alimentacion=nombre)
    
    if request.method == 'POST':
        form = TipoAlimentacionForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de alimentación actualizada exitosamente.")
            return redirect('listar_alimentacion')
        else:
            messages.error(request, 'Ocurrió un error al intentar editar el tipo de alimentación.')
    else:
        form = TipoAlimentacionForm(instance=tipo)
    
    return render(request, 'editar_tipo_alimentacion.html', {'form': form})
