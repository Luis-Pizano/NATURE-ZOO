from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages # type: ignore
from .models import TipoAnimal
from .forms import TipoAnimalForm
def agregar_tipo(request):
    if request.method =='POST':
        form = TipoAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de animal agregado exitosamente.')
            return redirect('listar_tipo_animal')
        else:
            messages.error(request,'Este tipo de animal ya esta registrado.')
    else:
        form = TipoAnimalForm()
    return render(request,'agregar_tipo_animal.html',{'form':form})

def listar_tipo_animal(request):
    tipos = TipoAnimal.objects.all()
    return render(request,'listar_tipos_animales.html',{'tipos':tipos})

def eliminar_tipo_animal (request,id):
    tipo = get_object_or_404(TipoAnimal,id_tipo_animal=id)
    if request.method =='POST':
        tipo.delete()
        messages.success(request,'Tipo de animal eliminado exitosamente.')
        return redirect('listar_tipo_animal')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el tipo de animal.')
    return render(request,'listar_tipos_animales.html')

def editar_tipo_animal (request,nombre):
    tipo = get_object_or_404(TipoAnimal,nombre_tipo_animal=nombre)
    if request.method =='POST':
        form = TipoAnimalForm(request.POST,instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de animal editado exitosamente.')
            return redirect('listar_tipo_animal')
        else:
            messages.error(request,'Este tipo de animal ya esta registrado.')
    else:
        form = TipoAnimalForm(instance=tipo)
    return render(request,'editar_tipo_animal.html',{'form':form})