from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import MetodosPago
from .forms import MetodosPagoForm

def agregar_metodo_pago (request):
    if request.method =='POST':
        form = MetodosPagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Metodo de pago agregado exitosamente.')
            return redirect('listar_metodos_pago')
        else:
            messages.error(request,'Este metodo de pago ya esta registrado.')
    else:
        form = MetodosPagoForm()
    return render(request,'agregar_metodo_pago.html',{'form':form})

def listar_metodos_pago (request):
    metodos = MetodosPago.objects.all()
    return render(request,'listar_metodos_pago.html',{'metodos':metodos})

def eliminar_metodo_pago (request,id):
    metodo = get_object_or_404(MetodosPago,id_metodo_pago=id)
    if request.method =='POST':
        metodo.delete()
        messages.success(request,'Metodo de pago eliminado exitosamente.')
        return redirect('listar_metodos_pago')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el metodo de pago.')
    return render(request,'listar_metodos_pago.html')

def editar_metodo_pago (request,nombre):
    metodo = get_object_or_404(MetodosPago,nombre_metodo_pago = nombre)
    if request.method =='POST':
        form = MetodosPagoForm(request.POST,instance=metodo)
        if form.is_valid():
            form.save()
            messages.success(request,'Metodo de pago actualizado exitosamente.')
            return redirect('listar_metodos_pago')
        else:
            messages.error(request,'Este metodo de pago ya esta registrado.')
    else:
        form = MetodosPagoForm(instance=metodo)
    return render(request,'editar_metodo_pago.html',{'form':form})