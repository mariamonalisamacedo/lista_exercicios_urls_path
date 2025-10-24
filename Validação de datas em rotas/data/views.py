from django.http import HttpResponse, HttpResponseBadRequest

def data(request, ano, mes):
    if not (1 <= mes <= 12):
        return HttpResponseBadRequest('Mês inválido. Deve estar entre 1 e 12.')
    return HttpResponse(f'Ano: {ano}, Mês: {mes:02d}')