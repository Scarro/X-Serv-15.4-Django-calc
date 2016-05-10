from django.shortcuts import render

# Create your views here.

def suma(request, numero1, numero2):
	suma = int(numero1) + int(numero2)
	context = {
		'operacion' : 'suma',
		'resultado' : suma,
	}
	return render(request, 'calc/index.html',context)

def resta(request, numero1, numero2):
	resta = int(numero1) - int(numero2)
	context = {
		'operacion' : 'resta',
		'resultado' : resta
	}
	return render(request, 'calc/index.html', context)

def multiplicacion(request, numero1, numero2):
	mult = int(numero1) * int(numero2)
	context = {
		'operacion' : 'multiplicacion',
		'resultado' : mult
	}
	return render(request, 'calc/index.html', context)

def division (request, numero1, numero2):
	try:
		division = int(numero1) / int(numero2)
		context = {
			'operacion': 'division',
			'resultado': division
		}
		template = 'calc/index.html'
	except ZeroDivisionError:
		context = {
			'error': 'Error: divides entre 0'
		}
		template = 'calc/error.html'
	return render(request, template, context)