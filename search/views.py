# search/views.py
from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post
from django.db.models import Q


def get_queryset(request):
    query = request.GET.get("q")
    
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return render(request, 'search/search_results.html', {'posts':posts})
    return Post.objects.none()  # Return empty queryset if no query
