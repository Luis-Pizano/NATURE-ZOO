from .models import Carrito, CarritoItem
from .views import carrito_id


def contar_items(request):
    carrito_contador = 0

    try:
        # Obtén el carrito basado en el carrito_id del usuario
        carrito = Carrito.objects.get(carrito_id=carrito_id(request))
        carrito_items = CarritoItem.objects.filter(carrito=carrito, is_activo=True)
        # Suma las cantidades de los items en el carrito
        for carrito_item in carrito_items:
            carrito_contador += carrito_item.cantidad
    except Carrito.DoesNotExist:
        # Si no hay carrito, el contador permanece en 0
        carrito_contador = 0

    return {'carrito_contador': carrito_contador}


def total_entradas(request):
    total_entradas = 0

    try:
        # Obtén el carrito basado en el carrito_id del usuario
        carrito = Carrito.objects.get(carrito_id=carrito_id(request))
        carrito_items = CarritoItem.objects.filter(carrito=carrito, is_activo=True)
        # Suma la cantidad total de entradas en el carrito
        total_entradas = sum(item.cantidad for item in carrito_items)
    except Carrito.DoesNotExist:
        # Si no hay carrito, imprime un mensaje de depuración (opcional)
        print("No hay entradas en el carrito")

    return {'total_entradas': total_entradas}
