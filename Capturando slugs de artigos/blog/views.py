from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

# Tentamos importar um modelo Article se o projeto já o tiver definido.
try:
    from .models import Article
except Exception:
    Article = None

# View que mostra o título do artigo a partir do slug.
def artigo(request, slug):
    """Retorna o título do artigo correspondente ao slug.

    - Se houver um modelo `Article` em `blog.models`, faz `get_object_or_404(Article, slug=slug)`.
    - Caso contrário, usa um dicionário estático (útil para projetos simples ou para teste).
    """
    if Article:
        article = get_object_or_404(Article, slug=slug)
        return HttpResponse(article.title)

    # Fallback estático
    ARTICLES = {
        'djangopara-iniciantes': 'Django para Iniciantes',
        # Adicione outros slugs e títulos aqui conforme necessário
    }

    title = ARTICLES.get(slug)
    if not title:
        raise Http404('Artigo não encontrado')
    return HttpResponse(title)
