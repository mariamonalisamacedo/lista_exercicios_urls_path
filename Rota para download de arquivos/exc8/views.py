import mimetypes
from django.http import HttpResponse


def download(request, nome, ext):
	"""View que recebe nome e extensão e retorna uma mensagem com o tipo do arquivo.

	Exemplo: /download/relatorio.pdf/  -> "Baixando: relatorio.pdf - Tipo: application/pdf"
	"""
	filename = f"{nome}.{ext}"
	mime_type, _ = mimetypes.guess_type(filename)
	tipo = mime_type if mime_type else "desconhecido"
	return HttpResponse(f"Baixando: {filename} - Tipo: {tipo}")
