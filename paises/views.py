from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages  # type: ignore
from .forms import PaisesForm
from .models import Paises

def agregar_pais(request):
    if request.method =='POST':
        form = PaisesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'País agregado exitosamente.')
            return redirect('listar_paises')
        else:
            messages.error(request,'Este país ya esta registrado.')
    else:
        form = PaisesForm()
    return render(request,'agregar_paises.html',{'form':form})

def listar_paises(request):
    paises = Paises.objects.all()
    return render(request,'listar_paises.html',{'paises':paises})

def eliminar_pais(request,id):
    pais = get_object_or_404(Paises,id_pais=id)
    if request.method =='POST':
        pais.delete()
        messages.success(request,'País eliminado exitosamente.')
        return redirect('listar_paises')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el país.')
    return render(request,'listar_paises.html')

def editar_pais(request,nombre):
    pais = get_object_or_404(Paises,nombre_pais = nombre)
    if request.method =='POST':
        form = PaisesForm(request.POST,instance=pais)
        if form.is_valid():
            form.save()
            messages.success(request,'País editado exitosamente.')
            return redirect('listar_paises')
        else:
            messages.error(request,'Este país ya esta registrado.')
    else:
        form = PaisesForm(instance=pais)
    return render(request,'editar_pais.html',{'form':form})