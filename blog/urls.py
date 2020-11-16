from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new', views.PostCreateView.as_view(), name='post-create'),
    path('about', views.about, name='blog-about')
]