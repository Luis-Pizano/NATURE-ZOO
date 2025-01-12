from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import TipoSuministro
from .forms import TipoSuministroForm

def agregar_tipo_suministro (request):
    if request.method =='POST':
        form = TipoSuministroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de suministro agregado exitosamente.')
            return redirect('listar_tipo_suministro')
        else:
            messages.error(request,'Este tipo de suministro ya esta registrado.')
    else:
        form = TipoSuministroForm()
    return render(request,'agregar_tipo_suministro.html',{'form':form})

def listar_tipo_suministro (request):
    tipos = TipoSuministro.objects.all()
    return render(request,'listar_tipos_suministros.html',{'tipos':tipos})

def eliminar_tipo_suministro (request,id):
    tipo = get_object_or_404(TipoSuministro,id_tipo_suministro=id)
    if request.method =='POST':
        tipo.delete()
        messages.success(request,'Tipo de suministro eliminado exitosamente.')
        return redirect('listar_tipo_suministro')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el tipo de suministro.')
    return render(request,'listar_tipos_suministros')

def editar_tipo_suministro (request,nombre):
    tipo = get_object_or_404(TipoSuministro,nombre_tipo_suministro=nombre)
    if request.method =='GET':
        form = TipoSuministroForm(request.GET,instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de suministro actualizado exitosamente.')
            return redirect('listar_tipo_suministro')
        else:
            messages.error(request,'Este tipo de suministro ya esta registrado.')
    else:
        form = TipoSuministroForm(instance=tipo)
    return render(request,'editar_tipo_suministro.html',{'form':form})