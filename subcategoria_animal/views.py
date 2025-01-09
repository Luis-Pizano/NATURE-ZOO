from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import SubcategoriasAnimales
from .forms import SubcategoriasEditForm, SubcategoriasForm

def agregar_sub_categoria (request):
    if request.method =='POST':
        form = SubcategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Subcategoría agregada exitosamente.')
            return redirect('listar_sub_categorias')
        else:
            messages.error(request,'Esta subcategoría ya esta registrada.')
    else:
        form = SubcategoriasForm()
    return render(request,'agregar_sub_categorias.html',{'form':form})

def listar_sub_categorias (request):
    sub_categorias = SubcategoriasAnimales.objects.all()
    return render(request,'listar_sub_categorias.html',{'sub_categorias':sub_categorias})

def eliminar_sub_categoria (request,id):
    sub_categoria = get_object_or_404(SubcategoriasAnimales,id_subcategoria_animal=id)
    if request.method =='POST':
        sub_categoria.delete()
        messages.success(request,'Subcategoría eliminada exitosamente.')
        return redirect('listar_sub_categorias')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar la subcategoría.')
    return render(request,'listar_sub_categorias.html')

def editar_sub_categoria (request,nombre):
    sub_categoria = get_object_or_404(SubcategoriasAnimales,nombre_subcategoria=nombre)
    if request.method =='POST':
        form = SubcategoriasEditForm(request.POST,instance=sub_categoria)
        if form.is_valid():
            form.save()
            messages.success(request,'Subcategoría actualizada exitosamente.')
            return redirect('listar_sub_categorias')
        else:
            messages.error(request,'Esta subcategoría ya esta registrada.')
    else:
        form = SubcategoriasEditForm(instance=sub_categoria)
    return render(request,'editar_sub_categoria.html',{'form':form})
