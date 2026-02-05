from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensagem
from django import forms

# Criando um formulário rápido para a mensagem
class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['destinatario', 'assunto', 'corpo']

@login_required
def inbox(request):
    # Mostra as mensagens que o usuário logado recebeu
    mensagens = Mensagem.objects.filter(destinatario=request.user).order_by('-data_envio')
    return render(request, 'messenger/inbox.html', {'mensagens': mensagens})

@login_required
def enviar_mensagem(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            nova_msg = form.save(commit=False)
            nova_msg.remetente = request.user  
            nova_msg.save()
            return redirect('messenger:inbox')
    else:
        form = MensagemForm()
    
    return render(request, 'messenger/enviar.html', {'form': form})