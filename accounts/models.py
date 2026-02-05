from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Relaciona com o usuário padrão do Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Requisitos do perfil: bio e avatar
    biografia = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    site_web = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"