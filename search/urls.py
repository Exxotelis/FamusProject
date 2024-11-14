# search/urls.py
from django.urls import path
from .views import SearchPostView

app_name = 'search'

urlpatterns = [
    path('', SearchPostView.as_view(), name='post_search'),  # Now accessible at /search/
]
