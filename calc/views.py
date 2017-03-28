from django.shortcuts import render
from django.http import Http404

# Create your views here.

def calculadora(request):
    return render(request, 'calc/index.html')

def operacion(request, operando1, operacion, operando2):
    if operacion == '+':
        op = "Suma"
        resultado = int(operando1) + int(operando2)
    elif operacion == '-':
        op = "Resta"
        resultado = int(operando1) - int(operando2)
    elif operacion == '*':
        op = "Multiplicación"
        resultado = int(operando1) * int(operando2)
    else:
        try:
            resultado = int(operando1) / int(operando2)
        except ZeroDivisionError:
            raise Http404('Error: imposible dividir entre 0')
        op = "División"
    return render(request, 'calc/operacion.html', {
        'operacion': op,
        'simbolo': operacion,
        'operando1': operando1,
        'operando2': operando2,
        'resultado': resultado,
        })