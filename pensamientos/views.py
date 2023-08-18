from django.shortcuts import render
import datetime  # Modulo de Python


# Creando mis vistas para la Aplicación 'pensamientos'
my_path_url = "pages"


def inicio(request):
    return render(request, 'base.html')


def saludar(request, nombre):
    context = {'name': nombre}
    return render(request, f'{my_path_url}/saludar.html', context)


def moneda(request):
    num = 1
    context = {'num': num}
    return render(request, f'{my_path_url}/moneda.html', context)


def contacto(request):
    fecha = datetime.datetime.now()
    return render(request, f'{my_path_url}/contacto.html', {'fecha': fecha})


def nosotros(request):
    return render(request, f'{my_path_url}/nosotros.html')
