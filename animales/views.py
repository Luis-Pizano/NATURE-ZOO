from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Animales
from .forms import AnimalesForm

def agregar_animales (request):
    if request.method =='POST':
        form = AnimalesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Animal agregado exitosamente.')
            return redirect('listar_animales')
        else:
            messages.error(request,'Ocurrio un error al intentar agregar al animal.')
    else:
        form = AnimalesForm()
    return render(request,'agregar_animales.html',{'form':form})

def listar_animales (request):
    animales = Animales.objects.all()
    return render(request,'listar_animales.html',{'animales':animales})

def eliminar_animal (request,id):
    animal = get_object_or_404(Animales,id_animal=id)
    if request.method =='POST':
        animal.delete()
        messages.success(request,'Animal eliminado exitosamente.')
        return redirect('listar_animales')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar al animal.')
    return render(request,'listar_animales.html')

def editar_animal (request,id):
    animal = get_object_or_404(Animales,id_animal=id)
    if request.method =='POST':
        form = AnimalesForm(request.POST,instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request,'Animal actualizado exitosamente.')
            return redirect('listar_animales')
        else:
            messages.error(request,'Ocurrio un error al intentar editar al animal.')
    else:
        form = AnimalesForm(instance=animal)
    return render(request,'editar_animal.html',{'form':form})