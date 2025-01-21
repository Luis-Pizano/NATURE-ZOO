from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Ventas
from .forms import VentasForm

def agregar_venta (request):
    if request.method =='POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Venta agregada exitosamente.')
            return redirect('listar_ventas')
        else:
            messages.error(request,'Ocurrio un error al intentar agregarla venta.')
    else:
        form = VentasForm()
    return render(request,'agregar_ventas.html',{'form':form})

def listar_ventas (request):
    ventas = Ventas.objects.all()
    return render(request,'listar_ventas.html',{'ventas':ventas})

def eliminar_venta (request,id):
    venta = get_object_or_404(Ventas,id_venta=id)
    if request.method =='POST':
        venta.delete()
        messages.success(request,'Venta eliminada exitosamente.')
        return redirect('listar_ventas')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar la venta.')
    return render(request,'listar_ventas.html')

def editar_venta (request,id):
    venta = get_object_or_404(Ventas,id_venta=id)
    if request.method =='POST':
        form = VentasForm(request.POST,instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request,'Venta actualizada exitosamente.')
            return redirect('listar_ventas')
        else:
            messages.error(request,'Ocurrio un error al intentar editar la venta.')
    else:
        form = VentasForm(instance=venta)
    return render(request,'editar_venta.html',{'form':form})