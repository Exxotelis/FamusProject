# search/views.py
from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post
from django.db.models import Q

class SearchPostView(ListView):
    model = Post
    template_name = "search/search_results.html"
    context_object_name = "results"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return Post.objects.none()  # Return empty queryset if no query
