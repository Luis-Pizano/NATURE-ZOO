from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Entradas
from .forms import EntradasForm,EntradasEditForm

def agregar_entrada (request):
    if request.method =='POST':
        form = EntradasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Entrada agregada exitosamente.')
            return redirect('listar_entradas')
        else:
            messages.error(request,'Esta entrada ya esta registrada.')
    else:
        form = EntradasForm()
    return render(request,'agregar_entradas.html',{'form':form})

def listar_entradas (request):
    entradas = Entradas.objects.all()
    return render(request,'listar_entradas.html',{'entradas':entradas})

def eliminar_entrada (request,id):
    entrada = get_object_or_404(Entradas,id_entrada=id)
    if request.method =='POST':
        entrada.delete()
        messages.success(request,'Entrada eliminada exitosamente.')
        return redirect('listar_entradas')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar la entrada.')
    return render(request,'listar_entradas.html')

def editar_entrada (request,id):
    entrada = get_object_or_404(Entradas,id_entrada=id)
    if request.method =='POST':
        form = EntradasEditForm(request.POST,instance=entrada)
        if form.is_valid():
            form.save()
            messages.success(request,'Entrada actualizada exitosamente.')
            return redirect('listar_entradas')
        else:
            messages.error(request,'Ocurrio un error al intentar editar la entrada.')
    else:
        form = EntradasEditForm(instance=entrada)
    return render(request,'editar_entrada.html',{'form':form})

def comprar_entradas (request):
    entradas = Entradas.objects.all()
    return render(request,'comprar_entradas.html',{'entradas':entradas})