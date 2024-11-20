# search/urls.py
from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('search/', views.get_queryset, name='post_search'),  
]
