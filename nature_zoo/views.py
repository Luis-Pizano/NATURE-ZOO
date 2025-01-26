from django.shortcuts import render # type: ignore
from especies.models import Especies
from animales.models import Animales

def home(request):
    especies = Especies.objects.count()
    animales = Animales.objects.count()
    context = {
        'especies':especies,
        'animales':animales,
    }
    return render(request,'home.html',context)