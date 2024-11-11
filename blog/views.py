# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  # Retrieve the post based on its slug
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


