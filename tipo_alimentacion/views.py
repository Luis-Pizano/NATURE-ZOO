from django.shortcuts import redirect, render
from django.contrib import messages
from .models import TipoAlimentacion
from .forms import TipoAlimentacionForm

def agregar_tipo(request):
    if request.method == 'POST':
        form = TipoAlimentacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Tipo de alimentación agregada exitosamente.")
            return redirect('listar_alimentacion')
        else:
            messages.error(request,"Ocurrio un error al intentar agregar el tipo de aliemntación.")
    else:
        form = TipoAlimentacionForm()
    return render(request,'agregar_tipo_alimentacion.html',{'form':form})

def listar_tipo_alimentacion(request):
    tipos = TipoAlimentacion.objects.all()
    return render(request,'listar_tipos_alimentacion.html',{'tipos':tipos})
