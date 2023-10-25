from django.shortcuts import render
from .forms import TableroForm


# Create your views here.
def index(request):
    return render(request, 'buscaMinasForm/index.html')


def crea_tablero(request):
    #Si se ha enviado el formulario
    if request.method == 'GET':
        form = TableroForm(request.GET)
        #Ejecutamos la validación
        if form.is_valid():
            #Los datos se cogen del diccionario cleaned_data
            columnas = form.cleaned_data['columnas']
            filas = form.cleaned_data['filas']
            return render(request, 'buscaMinasForm/muestra_tablero.html', {'filas': filas, 'columnas': columnas, 'rango_filas': range(filas), 'rango_columnas': range(columnas)})

    #Si se pide la página por primera vez
    form = TableroForm()
    return render(request, 'buscaMinasForm/crea_tablero.html', {'form': form})
