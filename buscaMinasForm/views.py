from django.shortcuts import render
from .forms import TableroForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def crea_tablero(request):
    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            return render(request, 'crea_tablero.html', {
                'filas': filas,
                'columnas': columnas
            })
    else:
        form = TableroForm()
    return render(request, 'crea_tablero.html', {'form': form})