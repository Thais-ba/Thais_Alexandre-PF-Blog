from django.urls import path
from .views import PostList, PostDetail, PostCreate, about

urlpatterns = [
    path('pages/', PostList.as_view(), name='pages'),
    path('pages/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('pages/create/', PostCreate.as_view(), name='post_create'),
    path('about/', about, name='about'),
]