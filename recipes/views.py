from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name' : 'Maurício Casagrande'
    })

def sobre(request):
    return HttpResponse('SOBRE')

def contato(request):
    return HttpResponse('CONTATO')
