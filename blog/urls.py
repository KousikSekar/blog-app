from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    # path('', views.home, name='blog-home'),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
=======
    path('', views.home, name='blog-home'),
    path('post', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new', views.PostCreateView.as_view(), name='post-create'),
>>>>>>> f99a36e29daf09a57d73702899369a4393f9a6a1
    path('about', views.about, name='blog-about')
]