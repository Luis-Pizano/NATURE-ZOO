from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages

from especies.models import Especies # type: ignore
from .forms import HabitatsEditForms, HabitatsForms
from .models import Habitats
from django.core.paginator import Paginator


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
            messages.error(request, 'Ocurrio un error al intentar editar el habitat.')
    else:
        form = HabitatsEditForms(instance=habitat)
    return render(request, 'editar_habitat.html', {'form': form})

def presentacion_habitats (request):
    habitats = Habitats.objects.all()
    cant_habitat = pagination(request,habitats,1)
    return render(request, 'presentar_habitats.html', {'habitats': cant_habitat})

def pagination(request,habitat,num_pages):
    paginator = Paginator(habitat,num_pages)
    pagina = request.GET.get('pagina')
    pagina_habitat = paginator.get_page(pagina)
    return pagina_habitat

def search(request):
    query = request.GET.get('q', '')  # Obtener el valor de la búsqueda desde el query string
    especies_resultado = Especies.objects.filter(nombre_especie__icontains=query) if query else []
    habitats_resultado = Habitats.objects.filter(nombre_habitat__icontains=query) if query else []
    
    return render(request, 'search.html', {
        'especies_resultado': especies_resultado,
        'habitats_resultado': habitats_resultado,
        'query': query
    })