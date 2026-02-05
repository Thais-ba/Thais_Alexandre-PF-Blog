from django.db import models
from django.contrib.auth.models import User

class Mensagem(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    assunto = models.CharField(max_length=200) # Verifique se esse nome existe
    corpo = models.TextField()                # Verifique se esse nome existe
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.remetente} -> {self.destinatario}: {self.assunto}"