from django.shortcuts import render
from django.http.response import HttpResponse
<<<<<<< HEAD
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
=======
from django.views.generic import ListView, DetailView, CreateView
>>>>>>> f99a36e29daf09a57d73702899369a4393f9a6a1

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
<<<<<<< HEAD
    

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

=======


class PostDetailView(DetailView):
    model = models.Post


class PostCreateView(CreateView):
    model = models.Post
    fields = ['title', 'content']

>>>>>>> f99a36e29daf09a57d73702899369a4393f9a6a1

def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


