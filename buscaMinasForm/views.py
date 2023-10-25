from django.shortcuts import render
from .forms import TableroForm


# Create your views here.
def index(request):
    return render(request, 'buscaMinasForm/index.html')


def crea_tablero(request):
    form = TableroForm()
    return render(request, 'buscaMinasForm/crea_tablero.html', {'form': form})
