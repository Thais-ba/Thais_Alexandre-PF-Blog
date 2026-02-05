from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                login(request, user)
                return redirect("pages")
    
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "accounts/signup.html", {"form": form})

from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import UserEditForm, PerfilForm

@login_required
def perfil_view(request):
    # Garante que o perfil existe antes de mostrar
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)
        
    return render(request, 'accounts/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })