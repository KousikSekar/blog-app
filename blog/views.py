from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from . import models

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


class PostDetailView(DetailView):
    model = models.Post


class PostCreateView(CreateView):
    model = models.Post
    fields = ['title', 'content']


def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


