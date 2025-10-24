from django.shortcuts import render
from django.http import HttpResponse

def perfil(request, nome=None):
    if nome:
        return HttpResponse(f'Perfil de {nome}')
    else:
        return HttpResponse('Perfil de visitante')