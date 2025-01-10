from django.shortcuts import get_object_or_404,redirect,render # type: ignore
from django.contrib import messages # type: ignore
from .models import TipoProveedor
from .forms import TipoProveedorForm

def agregar_tipo_proveedor (request):
    if request.method =='POST':
        form = TipoProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de proveedor agregado exitosamente.')
            return redirect('listar_tipo_proveedor')
        else:
            messages.error(request,'Este tipo de proveedor ya esta registrado.')
    else:
        form = TipoProveedorForm()
    return render(request,'agregar_tipo_proveedor.html',{'form':form})

def listar_tipo_proveedor(request):
    tipos = TipoProveedor.objects.all()
    return render(request,'listar_tipos_proveedores.html',{'tipos':tipos})

def eliminar_tipo_proveedor (request,id):
    tipo = get_object_or_404(TipoProveedor,id_tipo_proveedor=id)
    if request.method =='POST':
        tipo.delete()
        messages.success(request,'Tipo de proveedor eliminado exitosamente.')
        return redirect('listar_tipo_proveedor')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el tipo de proveedor.')
    return render(request,'listar_tipos_proveedores.html')

def editar_tipo_proveedor (request,nombre):
    tipo = get_object_or_404(TipoProveedor,nombre_tipo_proveedor=nombre)
    if request.method =='GET':
        form = TipoProveedorForm(request.GET,instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request,'Tipo de proveedor actualizado exitosamente.')
            return redirect('listar_tipo_proveedor')
        else:
            messages.error(request,'Este tipo de proveedor ya esta registrado.')
    else:
        form = TipoProveedorForm(instance=tipo)
    return render(request,'editar_tipo_proveedor.html',{'form':form})