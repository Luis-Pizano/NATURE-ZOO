from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Visitantes
from .forms import VisitantesForm,VisitantesEditForm

def agregar_visitante (request):
    if request.method =='POST':
        form = VisitantesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Visitante agregado exitosamente.')
            return redirect('listar_visitantes')
        else:
            messages.error(request,'El correo o telefono ya estan registrados.')
    else:
        form = VisitantesForm()
    return render(request,'agregar_visitantes.html',{'form':form})

def listar_visitantes (request):
    visitantes = Visitantes.objects.all()
    return render(request,'listar_visitantes.html',{'visitantes':visitantes})

def eliminar_visitante (request,id):
    visitante = get_object_or_404(Visitantes,id_visitante=id)
    if request.method =='POST':
        visitante.delete()
        messages.success(request,'Visitante eliminado exitosamente')
        return redirect('listar_visitantes')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar al visitante.')
    return render(request,'listar_visitantes.html')

def editar_visitante (request,id):
    visitante = get_object_or_404(Visitantes,id_visitante=id)
    if request.method =='POST':
        form = VisitantesEditForm(request.POST,instance=visitante)
        if form.is_valid():
            form.save()
            messages.success(request,'Visitante editado exitosamente.')
            return redirect('listar_visitantes')
        else:
            messages.error(request,'Ocurrio un error al intentar editar al visitante.')
    else:
        form = VisitantesEditForm(instance=visitante)
    return render(request,'editar_visitante.html',{'form':form})