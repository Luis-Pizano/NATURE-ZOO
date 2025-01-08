from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages # type: ignore
from .forms import HabitatsEditForms, HabitatsForms
from .models import Habitats

def agregar_habitats(request):
    if request.method =='POST':
        form = HabitatsForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Habitat Agregado Exitosamente.')
            return redirect('listar_habitats')
        else:
            messages.error(request,'Este habitat ya esta registrado.')
    else:
        form = HabitatsForms()
    return render(request,'agregar_habitat.html',{'form':form})

def listar_habitats(request):
    habitats = Habitats.objects.all()
    return render(request,'listar_habitats.html',{'habitats':habitats})

def eliminar_habitat(request,id):
    habitat = get_object_or_404(Habitats,id_habitat = id)
    if request.method =='POST':
        habitat.delete()
        messages.success(request,'Habitat eliminado exitosamente.')
        return redirect('listar_habitats')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el habitat.')
    return render(request,'listar_habitats.html')

def editar_habitat(request,nombre):
    habitat = get_object_or_404(Habitats,nombre_habitat = nombre)
    if request.method =='POST':
        form = HabitatsEditForms(request.POST,request.FILES,instance=habitat)
        if form.is_valid():
            form.save()
            messages.success(request,'Habitat editado exitosamente.')
            return redirect('listar_habitats')
        else:
            messages.error(request, 'Este habitat ya esta registrado.')
    else:
        form = HabitatsEditForms(instance=habitat)
    return render(request, 'editar_habitat.html', {'form': form})