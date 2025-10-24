from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def produto(request, categoria, nome):
    return HttpResponse(f'Categoria: {categoria}, Produto: {nome}')
