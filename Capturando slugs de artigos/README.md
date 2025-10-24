# Capturando slugs de artigos — rota /artigo/<slug:slug>/

Este pequeno app `blog` fornece uma rota para exibir o título de um artigo a partir do seu slug.

Arquivos criados:
- `blog/views.py` — view `artigo(request, slug)` que retorna o título.
- `blog/urls.py` — inclui a rota `artigo/<slug:slug>/`.
- `blog/models.py` — modelo `Article` (opcional) com `title`, `slug` e `content`.

Como usar:
1. Copie a pasta `blog` para o seu projeto Django ou coloque-a no root do seu projeto.
2. Se quiser usar o modelo `Article`, adicione `'blog'` em `INSTALLED_APPS` e rode `makemigrations`/`migrate`.

Incluindo as URLs do app no `urls.py` do projeto (exemplo `project/urls.py`):

from django.urls import include, path

urlpatterns = [
    # outras rotas
    path('', include('blog.urls')),
]

Exemplo de acesso:
- http://localhost:8000/artigo/djangopara-iniciantes/  -> exibirá "Django para Iniciantes"

Notas:
- A view usa um fallback estático quando não há um modelo `Article` disponível, para facilitar testes rápidos.
- Se você usar o modelo `Article`, o slug deve existir na base de dados para que a página seja servida.
