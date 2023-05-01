from django.shortcuts import render
from .models import Autor, Editorial, Libro
from .forms import AutorForm, LibroForm, EditorialForm

def autor_form(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            form = AutorForm()
    else:
        form = AutorForm()
    return render(request, r'C:\Users\Danie\Desktop\python tercera pre-entrega_Olivier\Proyecto3\Proyecto3\templates\autor\autor_form.html', {'form': form})

def libro_form(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            form = LibroForm()
    else:
        form = LibroForm()
    return render(request, r'C:\Users\Danie\Desktop\python tercera pre-entrega_Olivier\Proyecto3\Proyecto3\templates\libros\libro_form.html', {'form': form})

def editorial_form(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            form = EditorialForm()
    else:
        form = EditorialForm()
    return render(request, r'C:\Users\Danie\Desktop\python tercera pre-entrega_Olivier\Proyecto3\Proyecto3\templates\editorial\editorial_form.html', {'form': form})

def busqueda_form(request):
    return render(request, r'C:\Users\Danie\Desktop\python tercera pre-entrega_Olivier\Proyecto3\Proyecto3\templates\busqueda\busqueda_form.html')

def busqueda(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        libros = Libro.objects.filter(title__icontains=query)
        autores = Autor.objects.filter

