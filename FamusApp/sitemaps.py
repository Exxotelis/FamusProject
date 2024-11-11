# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly" 
    priority = 0.8 

    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at  # Ensure 'updated_at' is a valid field in your Post model

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'home',      
            'about',     
            'contact',  
            'games', 
            'asteroids',
            'game_details',
            'game_tips',
            'pacman',
            'space_invaders',
            'tetris',
        ]
    
    def location(self, item):
        return reverse(item)
