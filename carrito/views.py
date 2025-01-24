from django.shortcuts import render, redirect # type: ignore
from entradas.models import Entradas
from .models import Carrito, CarritoItem

def carrito_id(request):
    try:
        print("creando carro")
        carrito = request.session.session_key
        print("carrito: ",carrito)
        if not carrito:
            carrito = request.session.create()
            
        return carrito
    except Exception as e:
        print(e)

def agregar_carrito(request, id):
    entrada = Entradas.objects.get(id_entrada=id)
    try:
        carrito = Carrito.objects.get(carrito_id=carrito_id(request))
    except Carrito.DoesNotExist:  # Asegúrate de usar "Carrito" con mayúscula
        carrito = Carrito.objects.create(carrito_id=carrito_id(request))
    
    carrito.save()
    
    try:
        carrito_item = CarritoItem.objects.get(entrada=entrada, carrito=carrito)
        carrito_item.cantidad += 1
        carrito_item.save()
    except CarritoItem.DoesNotExist:
        carrito_item = CarritoItem.objects.create(
            entrada=entrada,
            cantidad=1,
            carrito=carrito,
        )
        carrito_item.save()
    
    return redirect('carrito')



def carrito(request, total=0, cantidad=0, carrito_item=None):
    try:
        carrito = Carrito.objects.get(carrito_id=carrito_id(request))
        carrito_items = CarritoItem.objects.filter(carrito=carrito, is_activo=True)
        for carrito_item in carrito_items:
            total += (carrito_item.entrada.precio * carrito_item.cantidad)
            cantidad += carrito_item.cantidad
    except Carrito.DoesNotExist:
        carrito_items = []  # Si no existe, inicializa una lista vacía
    iva = total * 0.19
    context = {
        'total': f"{total:,.0f}".replace(",", "."),
        'cantidad': cantidad,
        'carrito_items': carrito_items,
        'IVA':f"{iva:,.0f}".replace(",", "."),  # Calcula el IVA basado en el total
    }
    
    return render(request, 'carrito.html', context)

def eliminar_carrito(request):
    try:
        carrito = Carrito.objects.get(carrito_id=carrito_id(request))
        
        carrito_items = CarritoItem.objects.filter(carrito=carrito)
        carrito_items.delete() 
        
    except Carrito.DoesNotExist:
        pass

    return redirect('carrito')



def eliminar_carrito_item(request,id):
    carrito = Carrito.objects.get(carrito_id=carrito_id(request))
    entrada = Entradas.objects.get(id_entrada=id)
    carrito_item = CarritoItem.objects.get(entrada=entrada, carrito=carrito)
    carrito_item.delete()
    return redirect('carrito')

def restar_item_carrito(request, id):
    entrada = Entradas.objects.get(id_entrada=id)
    try:
        carrito = Carrito.objects.get(carrito_id=carrito_id(request))
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(carrito_id=carrito_id(request))
    
    carrito.save()
    
    try:
        carrito_item = CarritoItem.objects.get(entrada=entrada, carrito=carrito)
        carrito_item.cantidad -= 1
        if carrito_item.cantidad == 0:
            carrito_item.delete()
        else:
            carrito_item.save()
    except CarritoItem.DoesNotExist:
        carrito_item = CarritoItem.objects.create(
            entrada=entrada,
            cantidad=1,
            carrito=carrito,
        )
        carrito_item.save()
    
    return redirect('carrito')