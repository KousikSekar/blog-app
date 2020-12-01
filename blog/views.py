from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models
from django.contrib.auth.models import User

posts = [
    {
        'author': 'Kousik',
        'title': 'Blog Post 1',
        'Content': 'First post content',
        'date_posted': 'October 31, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'Content': 'Second post content',
        'date_posted': 'October 31, 2020'
    }
]


def home(request):
    context = {
        'posts': models.Post.objects.all()
    }
    # return HttpResponse('<h1>Blog home</h1>')
    return render(request, 'blog/home.html', context=context)


class PostListView(ListView):
    model = models.Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = models.Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return models.Post.objects.filter(author=user).order_by('-date_posted')
        

class PostDetailView(DetailView):
    model = models.Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


