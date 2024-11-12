from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_detail(request, slug):
    """Retrieve a single post based on its slug and render the detail view."""
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    """Retrieve a list of posts and paginate them for easier navigation."""
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  # Show 5 posts per page

    # Get the page number from the query parameters
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'page_obj': page_obj,
        'paginator': paginator,
        'page_number': page_number,
    }

    return render(request, 'blog/post_list.html', context)
