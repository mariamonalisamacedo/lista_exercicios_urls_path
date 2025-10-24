from django.http import HttpResponse

def soma(request, a, b):
    resultado = a + b
    return HttpResponse(str(resultado))