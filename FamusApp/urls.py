from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from FamusApp.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('game_tips/', views.game_tips, name='game_tips'), # Product Details page
    path('games/', views.games, name='games'),  # Games Gallery page
    path('pacman/', views.pacman, name='pacman'), 
    path('asteroids/', views.asteroids_view, name='asteroids'),
    path('tetris/', views.tetris_view, name='tetris'),
    path('space_invaders/', views.space_invaders, name='space_invaders'),
    path('game_details', views.game_details, name='game_details'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_of_service, name='terms_of_service'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),  # Direct game detail page without /games/


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
