from django.shortcuts import render
from .models import Product


def home(request):
    
    return render(request, 'FamusApp/home.html')

def contact(request):

    return render(request, 'FamusApp/contact.html')

def game_tips(request):
    
    return render(request, 'FamusApp/game_tips.html')

def games(request):
    
    return render(request, 'FamusApp/games.html')

def pacman(request):
    # Example 5x5 grid, update it with your logic
    grid = [
        ['wall', 'pac-dot', 'wall', 'wall', 'wall'],
        ['wall', 'wall', 'pac-man', 'pac-dot', 'wall'],
        ['wall', 'pac-dot', 'wall', 'wall', 'wall'],
        ['wall', 'power-pellet', 'wall', 'blinky', 'wall'],
        ['wall', 'wall', 'inky', 'wall', 'wall'],
    ]
    
    return render(request, 'FamusApp/pacman.html', {'ggrid': grid})

def asteroids_view(request):
    """Render the Asteroids game page."""
    return render(request, 'FamusApp/asteroids.html')

def tetris_view(request):
    """Render the Tetris game page."""
    return render(request, 'FamusApp/tetris.html')

def space_invaders(request):
    return render(request, 'FamusApp/space_invaders.html')

def game_details(request):
    return render(request, 'FamusApp/game_details.html')