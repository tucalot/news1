# Create your models here.
from django.db import models

# Create your models here.

CATEGORIAS = [
    ('noticias', 'Notícias'),
    ('politica', 'Política'),
    ('negocios', 'Negócios'),
    ('esportes', 'Esportes'),
    ('cultura', 'Cultura'),
    ('tecnologia', 'Tecnologia'),
    ('educacao', 'Educação'),  # 👈 adicionando edução
]

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    # Campo para vídeo do YouTube
    video_url = models.URLField(
        blank=True,
        null=True,
        max_length=500,
        help_text="Cole a URL do vídeo do YouTube (ex: https://youtu.be/ID ou https://www.youtube.com/watch?v=ID)"
    )

    def save(self, *args, **kwargs):
        if self.video_url:
            video_id = None

            if 'youtube.com/watch?v=' in self.video_url:
                video_id = self.video_url.split('watch?v=')[-1].split('&')[0]

            elif 'youtu.be/' in self.video_url:
                video_id = self.video_url.split('youtu.be/')[-1].split('?')[0]

            elif 'youtube.com/embed/' in self.video_url:
                video_id = self.video_url.split('embed/')[-1].split('?')[0]

            # Gera URL segura com youtube-nocookie
            if video_id:
                self.video_url = f'https://www.youtube-nocookie.com/embed/{video_id}'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo