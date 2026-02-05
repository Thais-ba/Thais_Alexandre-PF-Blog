from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 

class Post(models.Model):
    # Requisito: 2 Charfields
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    
    # Requisito: Texto enriquecido (CKEditor)
    corpo = RichTextField()
    
    # Requisito: Data e Imagem
    data = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='blog_pics/', null=True, blank=True)
    
    # Autor do post
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo