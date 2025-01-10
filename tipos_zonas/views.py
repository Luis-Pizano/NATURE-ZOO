from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages # type: ignore
from .models import TiposZonas
from .forms import TiposZonasForm,TiposZonasEditForm

def agregar_tipo_zona (request):
    if request.method=='POST':
        form = TiposZonasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de zona agregada exitosamente.')
            return redirect('listar_tipos_zonas')
        else:
            messages.error(request,'Este tipo de zona ya esta registrada.')
    else:
        form = TiposZonasForm()
    return render(request,'agregar_tipo_zona.html',{'form':form})

def listar_tipos_zonas (request):
    tipos_zonas = TiposZonas.objects.all()
    return render(request,'listar_tipos_zonas.html',{'tipos_zonas':tipos_zonas})

def eliminar_tipo_zona (request,id):
    tipo_zona = get_object_or_404(TiposZonas,id_tipo_zona=id)
    if request.method =='POST':
        tipo_zona.delete()
        messages.success(request,'Tipo de zona eliminada exitosamente')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el tipo de zona.')
    return redirect('listar_tipos_zonas')

def editar_tipo_zona (request,nombre):
    tipo_zona = get_object_or_404(TiposZonas,nombre_tipo_zona=nombre)
    if request.method =='POST':
        form = TiposZonasEditForm(request.POST,instance=tipo_zona)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de zona actualizada exitosamente.')
            return redirect('listar_tipos_zonas')
        else:
            messages.error(request,'Ocurrio un error al intentar editar el tipo de zona.')
    else:
        form = TiposZonasEditForm(instance=tipo_zona)
    return render(request,'editar_tipo_zona.html',{'form':form})