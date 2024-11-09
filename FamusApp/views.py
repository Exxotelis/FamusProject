from django.shortcuts import render
from .models import Product


def home(request):
    
    return render(request, 'FamusApp/home.html')

def contact(request):

    return render(request, 'FamusApp/contact.html')

def game_tips(request):
    
    return render(request, 'FamusApp/game_tips.html')

def games(request):
    Argames = [
        {
            'name': 'Pac-Man',
            'category': 'Classic Arcade',
            'image': 'images/PacMan.jpg',
            'slug': 'pacman'
        },
        {
            'name': 'Asteroids',
            'category': 'Classic Arcade',
            'image': 'images/asteroids.jpg',
            'slug': 'asteroids'
        },
        {
            'name': 'Tetris',
            'category': 'Puzzle',
            'image': 'images/tetris.jpg',
            'slug': 'tetris'
        },
        {
            'name': 'Space Invaders',
            'category': 'Classic Shooter',
            'image': 'images/SpaceInvaders.jpg',
            'slug': 'space_invaders'
        },
    ]

    # Corrected line for extracting unique categories
    categories = list(set(item['category'] for item in Argames))

    return render(request, 'FamusApp/games.html', {'Argames': Argames, 'categories': categories})



def pacman(request):
    # Example 5x5 grid, update it with your logic
    grid = [
        ['wall', 'pac-dot', 'wall', 'wall', 'wall'],
        ['wall', 'wall', 'pac-man', 'pac-dot', 'wall'],
        ['wall', 'pac-dot', 'wall', 'wall', 'wall'],
        ['wall', 'power-pellet', 'wall', 'blinky', 'wall'],
        ['wall', 'wall', 'inky', 'wall', 'wall'],
    ]
    
    return render(request, 'FamusApp/pacman.html', {'grid': grid})

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

def game_detail(request, slug):
        Argames = [
        {
            'name': 'Pac-Man',
            'category': 'Classic Arcade',
            'image': 'images/PacMan.jpg',
            'slug': 'pacman'
        },
        {
            'name': 'Asteroids',
            'category': 'Classic Arcade',
            'image': 'images/asteroids.jpg',
            'slug': 'asteroids'
        },
        {
            'name': 'Tetris',
            'category': 'Puzzle',
            'image': 'images/tetris.jpg',
            'slug': 'tetris'
        },
        {
            'name': 'Space Invaders',
            'category': 'Classic Shooter',
            'image': 'images/SpaceInvaders.jpg',
            'slug': 'space_invaders'
        },
    ]
    # Retrieve the game based on the slug
        game = next((item for item in Argames if item['slug'] == slug), None)
        if not game:
            return render(request, '404.html', status=404)
        return render(request, 'FamusApp/game_detail.html', {'game': game})

