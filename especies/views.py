from django.shortcuts import get_object_or_404,redirect, render
from .forms import EspeciesEditForm, EspeciesForm
from .models import Especies
from django.contrib import messages

def agregar_especies(request):
    if request.method == 'POST':
        form = EspeciesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Especie agregada exitosamente.')
            return redirect('listar_especies')
        else:
            messages.error(request,'Esta especie ya esta registrada.')
    else:
        form = EspeciesForm()
    return render(request,'agregar_especie.html',{'form':form})

def listar_especies(request):
    especies = Especies.objects.all()
    return render(request,'listar_especies.html',{'especies':especies})

def eliminar_especie(request,id):
    especie = get_object_or_404(Especies,id_especie = id)
    if request.method =='POST':
        especie.delete()
        messages.success(request,'Especie eliminada exitosamente.')
        return redirect('listar_especies')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar la especie.')
    return render(request,'listar_especies.html')

def editar_especie(request, nombre):
    # Busca la especie una sola vez
    especie = get_object_or_404(Especies, nombre_especie=nombre)
    
    if request.method == 'POST':
        form = EspeciesEditForm(request.POST, request.FILES, instance=especie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especie actualizada exitosamente.')
            return redirect('listar_especies')
        else:
            messages.error(request, 'Esta especie ya esta registrada.')
    else:
        form = EspeciesEditForm(instance=especie)
    
    return render(request, 'editar_especie.html', {'form': form})
