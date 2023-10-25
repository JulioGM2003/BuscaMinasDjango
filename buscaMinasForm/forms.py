from django import forms

class TableroForm(forms.Form):
    filas = forms.IntegerField(label='Número de Filas', min_value=1, max_value=20, initial=2)
    columnas = forms.IntegerField(label='Número de Columnas', min_value=1, max_value=15, initial=2)