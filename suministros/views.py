from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Suministros
from .forms import SuministrosForm,SuministrosEditForm

def agregar_suministro (request):
    if request.method =='POST':
        form = SuministrosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Suministro agregado exitosamente.')
            return redirect('listar_suministros')
        else:
            messages.error(request,'Ocurrio un error al intentar agregar el suministro.')
    else:
        form = SuministrosForm()
    return render(request,'agregar_suministros.html',{'form':form})

def listar_suministros (request):
    suministros = Suministros.objects.all()
    return render(request,'listar_suministros.html',{'suministros':suministros})

def eliminar_suministro (request,id):
    suministro = get_object_or_404(Suministros,id_suministro=id)
    if request.method =='POST':
        suministro.delete()
        messages.success(request,'Suministro eliminado exitosamente.')
        return redirect('listar_suministros')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el suministro.')
    return render(request,'listar_suministros.html')

def editar_suministro (request,id):
    suministro = get_object_or_404(Suministros,id_suministro=id)
    if request.method =='POST':
        form = SuministrosEditForm(request.POST,instance=suministro)
        if form.is_valid():
            form.save()
            messages.success(request,'Suministro actualizado exitosamente.')
            return redirect('listar_suministros')
        else:
            messages.error(request,'Ocurrio un error al intentar editar el suministro.')
    else:
        form = SuministrosEditForm(instance=suministro)
    return render(request,'editar_suministro.html',{'form':form})