from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Zonas
from .forms import ZonasForm,ZonasEditForm

def agregar_zona (request):
    if request.method =='POST':
        form = ZonasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Zona agregada exitosamente.')
            return redirect('listar_zonas')
        else:
            messages.error(request,'Esta zona ya esta registrada.')
    else:
        form = ZonasForm()
    return render(request,'agregar_zona.html',{'form':form})

def listar_zonas (request):
    zonas = Zonas.objects.all()
    return render(request,'listar_zonas.html',{'zonas':zonas})

def eliminar_zona (request,id):
    zona = get_object_or_404(Zonas,id_zona=id)
    if request.method =='POST':
        zona.delete()
        messages.success(request,'Zona eliminada exitosamente.')
        return redirect('listar_zonas')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar la zona.')
    return render(request,'listar_zonas.html',)

def editar_zona (request,nombre):
    zona = get_object_or_404(Zonas,nombre_zona=nombre)
    if request.method =='POST':
        form = ZonasEditForm(request.POST,instance=zona)
        if form.is_valid():
            form.save()
            messages.success(request,'Zona actualizada exitosamemte.')
            return redirect('listar_zonas')
        else:
            messages.error(request,'Ocurrio un error al intentar editar la zona')
    else:
        form = ZonasEditForm(instance=zona)
    return render(request,'editar_zona.html',{'form':form})