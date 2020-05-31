from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_published']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
