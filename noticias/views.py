from .models import Post
from django.shortcuts import render

def home(request):
    categorias = ['noticias', 'politica', 'negocios', 'esportes', 'cultura', 'tecnologia', 'educacao']
    
    # Determinando os posts conforme categoria
    contexto = {}

    for cat in categorias:
        if cat == 'tecnologia':
            contexto[cat] = Post.objects.filter(categoria=cat).order_by('-data_publicacao')[:5]
        else:
            contexto[cat] = Post.objects.filter(categoria=cat).order_by('-data_publicacao')[:4]

    # Vídeos
    contexto['videos'] = Post.objects.filter(video_url__isnull=False).order_by('-data_publicacao')[:7]

    # Últimas publicações gerais
    contexto['ultimas_publicacoes'] = Post.objects.all().order_by('-data_publicacao')[:5]

    return render(request, 'home.html', contexto)
