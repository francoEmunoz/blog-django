from django.shortcuts  import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def details(request, id):
    post = Post.objects.get(id= id)
    return render(request, 'blog/details.html', {'post': post})