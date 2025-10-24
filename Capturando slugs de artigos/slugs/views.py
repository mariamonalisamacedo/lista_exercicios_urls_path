from django.shortcuts import render
from django.http import HttpResponse

def artigo(request, slug):
    return HttpResponse("Título do artigo (slug): {slug.replace("-"," ").title()}")