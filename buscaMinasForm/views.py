from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def crea_tablero(request):
    return render(request, 'crea_tablero.html')