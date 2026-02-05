from django.urls import path
from .views import login_request, register
from .views import login_request, register, perfil_view, editar_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('signup/', register, name='signup'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # ... importações anteriores
    path('profile/', perfil_view, name='profile'),
    path('profile/edit/', editar_perfil, name='edit_profile'),
]
