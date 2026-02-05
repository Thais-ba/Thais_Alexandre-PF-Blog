from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post

# 1. Visualização da lista (Páginas) - CBV 1
class PostList(ListView):
    model = Post
    template_name = 'blog/pages.html' # Onde mostra todos os posts
    context_object_name = 'posts'

# 2. Detalhe do objeto - CBV 2
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# 3. Criação (Protegida por LoginRequiredMixin conforme requisito)
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'corpo', 'imagem']
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# View simples para o "Sobre Mim" (Requisito About)
def about(request):
    return render(request, 'blog/about.html')