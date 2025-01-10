from django.shortcuts import render # type: ignore
from especies.models import Especies

def home(request):
    especies = Especies.objects.count()
    context = {
        'especies':especies
    }
    return render(request,'home.html',context)