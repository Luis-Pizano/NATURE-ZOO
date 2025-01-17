from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Proveedores
from .forms import ProveedoresForm

def agregar_proveedor (request):
    if request.method =='POST':
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Proveedor agregado exitosamente.')
            return redirect('listar_proveedores')
        else:
            messages.error(request,'Ocurrio un error al intentar agregar el Proveedor.')
    else:
        form = ProveedoresForm()
    return render(request,'agregar_Proveedor.html',{'form':form})

def listar_proveedores (request):
     proveedores = Proveedores.objects.all()
     return render(request,'listar_proveedores.html',{'proveedores':proveedores})
 
def eliminar_proveedor (request,id):
    proveedor = get_object_or_404(Proveedores,id_proveedor=id)
    if request.method =='POST':
        proveedor.delete()
        messages.success(request,'Proveedor eliminado exitosamente.')
        return redirect('listar_proveedores')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar al proveedor.')
    return render(request,'listar_proveedores.html')

def editar_proveedor (request,id):
    proveedor = get_object_or_404(Proveedores,id_proveedor=id)
    if request.method =='POST':
        form = ProveedoresForm(request.POST,instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request,'Proveedor actualizado exitosamente.')
            return redirect('listar_proveedores')
        else:
            messages.error(request,'Ocurrio un error al intentar editar el Proveedor.')
    else:
        form = ProveedoresForm(instance=proveedor)
    return render(request,'editar_proveedor.html',{'form':form})