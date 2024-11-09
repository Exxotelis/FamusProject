# myapp/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        # List all static URLs you want to include in the sitemap
        return [
            'home',      # Name of the URL pattern for your homepage
            'about',     # Name of the URL pattern for your about page
            'contact',   # Name of the URL pattern for your contact page
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
