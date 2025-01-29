from django.shortcuts import get_object_or_404,redirect, render

from habitats.models import Habitats
from .forms import EspeciesEditForm, EspeciesForm
from .models import Especies
from django.contrib import messages
from django.core.paginator import Paginator


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
            messages.error(request, 'Ocurrio un error al intentar editar la especie.')
    else:
        form = EspeciesEditForm(instance=especie)
    
    return render(request, 'editar_especie.html', {'form': form})

def presentar_especies (request):
    especies = Especies.objects.all().order_by('nombre_especie')
    especies_pages = pagination(request,especies,1)
    return render(request,'presentar_especies.html',{'especies':especies_pages})

def pagination(request,especies,num_pages):
    paginator = Paginator(especies,num_pages)
    pagina = request.GET.get('pagina')
    pagina_especies = paginator.get_page(pagina)
    return pagina_especies

def search(request):
    query = request.GET.get('q', '')
    especies_resultado = Especies.objects.filter(nombre_especie__icontains=query).order_by('nombre_especie') if query else []
    habitats_resultado = Habitats.objects.filter(nombre_habitat__icontains=query).order_by('nombre_habitat') if query else []
    total_resultados = len(especies_resultado) + len(habitats_resultado)
    
    return render(request, 'search.html', {
        'especies_resultado': especies_resultado,
        'habitats_resultado': habitats_resultado,
        'total_resultados': total_resultados,
        'query': query
    })