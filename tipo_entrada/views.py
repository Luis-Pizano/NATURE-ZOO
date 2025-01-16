from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import TiposEntradas
from .forms import TiposEntradasForm,TiposEntradasEditForm

def agregar_tipo_entrada (request):
    if request.method =='POST':
        form = TiposEntradasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de entrada agregada exitosamente.')
            return redirect('listar_tipo_entrada')
        else:
            messages.error(request,'Este tipo de entrada ya esta registrada.')
    else:
        form = TiposEntradasForm()
    return render(request,'agregar_tipo_entrada.html',{'form':form})

def listar_tipo_entrada (request):
    tipos = TiposEntradas.objects.all()
    return render(request,'listar_tipos_entradas.html',{'tipos':tipos})

def eliminar_tipo_entrada (request,id):
    tipo = get_object_or_404(TiposEntradas,id_tipo_entrada = id)
    if request.method =='POST':
        tipo.delete()
        messages.success(request,'Tipo de entrada eliminada exitosamente.')
        return redirect('listar_tipo_entrada')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el tipo de entrada.')
    return render(request,'listar_tipos_entradas.html')

def editar_tipo_entrada (request,nombre):
    tipo = get_object_or_404(TiposEntradas,nombre_tipo_entrada=nombre)
    if request.method =='GET':
        form = TiposEntradasEditForm(request.GET,instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de entrada actualizada exitosamente.')
            return redirect('listar_tipo_entrada')
        else:
            messages.error(request,'Ocurrio un error al intentar editar el tipo de entrada.')
    else:
        form = TiposEntradasEditForm(instance=tipo)
    return render(request,'editar_tipo_entrada.html',{'form':form})
