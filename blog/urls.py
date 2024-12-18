# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
