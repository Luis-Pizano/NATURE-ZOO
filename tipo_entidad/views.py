from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import TipoEntidad
from .forms import TipoEntidadForm,TipoEntidadEditForm

def agregar_tipo_entidad (request):
    if request.method =='POST':
        form = TipoEntidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de entidad agregada exitosamente.')
            return redirect('listar_tipo_entidad')
        else:
            messages.error(request,'Este tipo de entidad ya esta registrada.')
    else:
        form = TipoEntidadForm()
    return render(request,'agregar_tipo_entidad.html',{'form':form})

def listar_tipo_entidad (request):
    tipos = TipoEntidad.objects.all()
    return render(request,'listar_tipos_entidad.html',{'tipos':tipos})

def eliminar_tipo_entidad (request,id):
    tipo = get_object_or_404(TipoEntidad,id_tipo_entidad =id)
    if request.method =='POST':
        tipo.delete()
        messages.success(request,'Tipo de entidad eliminada exitosamente.')
        return redirect('listar_tipo_entidad')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el tipo de entidad.')
    return render(request,'listar_tipos_entidad.html')

def editar_tipo_entidad (request,nombre):
    tipo = get_object_or_404(TipoEntidad,nombre_tipo_entidad = nombre)
    if request.method =='GET':
        form = TipoEntidadEditForm(request.GET,instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de entidad actualizada exitosamente.')
            return redirect('listar_tipo_entidad')
        else:
            messages.error(request,'Ocurrio un error al intentar editar el tipo de entidad.')
    else:
        form = TipoEntidadEditForm(instance=tipo)
    return render(request,'editar_tipo_entidad.html',{'form':form})