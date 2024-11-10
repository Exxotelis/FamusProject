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
            'slug': 'pacman',
            'is_external': False
        },
        {
            'name': 'Asteroids',
            'category': 'Classic Arcade',
            'image': 'images/asteroids.jpg',
            'slug': 'asteroids',
            'is_external': False
        },
        {
            'name': 'Tetris',
            'category': 'Puzzle',
            'image': 'images/tetris.jpg',
            'slug': 'tetris',
            'is_external': False
        },
        {
            'name': 'Space Invaders',
            'category': 'Classic Shooter',
            'image': 'images/SpaceInvaders.jpg',
            'slug': 'space_invaders',
            'is_external': False
        },
        {
            'name': 'Bubble Tower 3D',
            'category': '3D Puzzle',
            'image': 'images/3Dteasers/BubbleTower.jpg',
            'external_link': 'https://play.famobi.com/bubble-tower-3d',
            'is_external': True
        },
        {
            'name': 'CannonBalls',
            'category': '3D',
            'image': 'images/3Dteasers/CannonBalls.jpg',
            'external_link': 'https://play.famobi.com/cannon-balls-3d',
            'is_external': True
        },
        {
            'name': 'Solitaire Klondike',
            'category': 'Card Game',
            'image': 'images/3Dteasers/SolitaireKlondike.jpg',
            'external_link': 'https://play.famobi.com/solitaire-klondike',
            'is_external': True
        },
        {
            'name': '8 Ball Billiards Classic',
            'category': 'Sports',
            'image': 'images/3Dteasers/8BallBilliardsClassic.jpg',
            'external_link': 'https://play.famobi.com/8-ball-billiards-classic',
            'is_external': True
        },
        {
            'name': 'Rising Squares',
            'category': 'Puzzle Arcade',
            'image': 'images/3Dteasers/RisingSquares.jpg',
            'external_link': 'https://play.famobi.com/rising-squares',
            'is_external': True
        },
        {
            'name': 'Block Painter',
            'category': 'Creative Puzzle',
            'image': 'images/3Dteasers/BlockPainter.jpg',
            'external_link': 'https://play.famobi.com/block-painter',
            'is_external': True
        },
        {
            'name': 'Speed Master',
            'category': 'Racing Arcade',
            'image': 'images/3Dteasers/SpeedMaster.jpg',
            'external_link': 'https://play.famobi.com/speed-master',
            'is_external': True
        },
        {
            'name': 'Crazy Caves',
            'category': 'Adventure Arcade',
            'image': 'images/3Dteasers/CrazyCaves.jpg',
            'external_link': 'https://play.famobi.com/crazy-caves',
            'is_external': True
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
            'slug': 'pacman',
            'is_external': False
        },
        {
            'name': 'Asteroids',
            'category': 'Classic Arcade',
            'image': 'images/asteroids.jpg',
            'slug': 'asteroids',
            'is_external': False
        },
        {
            'name': 'Tetris',
            'category': 'Puzzle',
            'image': 'images/tetris.jpg',
            'slug': 'tetris',
            'is_external': False
        },
        {
            'name': 'Space Invaders',
            'category': 'Classic Shooter',
            'image': 'images/SpaceInvaders.jpg',
            'slug': 'space_invaders',
            'is_external': False
        },
        {
            'name': 'Bubble Tower 3D',
            'category': '3D Puzzle',
            'image': 'images/3Dteasers/BubbleTower.jpg',
            'external_link': 'https://play.famobi.com/bubble-tower-3d',
            'is_external': True
        },
        {
            'name': 'CannonBalls',
            'category': '3D',
            'image': 'images/3Dteasers/CannonBalls.jpg',
            'external_link': 'https://play.famobi.com/cannon-balls-3d',
            'is_external': True
        },
        {
            'name': 'Solitaire Klondike',
            'category': 'Card Game',
            'image': 'images/3Dteasers/SolitaireKlondike.jpg',
            'external_link': 'https://play.famobi.com/solitaire-klondike',
            'is_external': True
        },
        {
            'name': '8 Ball Billiards Classic',
            'category': 'Sports',
            'image': 'images/3Dteasers/8BallBilliardsClassic.jpg',
            'external_link': 'https://play.famobi.com/8-ball-billiards-classic',
            'is_external': True
        },
        {
            'name': 'Rising Squares',
            'category': 'Puzzle Arcade',
            'image': 'images/3Dteasers/RisingSquares.jpg',
            'external_link': 'https://play.famobi.com/rising-squares',
            'is_external': True
        },
        {
            'name': 'Block Painter',
            'category': 'Creative Puzzle',
            'image': 'images/3Dteasers/BlockPainter.jpg',
            'external_link': 'https://play.famobi.com/block-painter',
            'is_external': True
        },
        {
            'name': 'Speed Master',
            'category': 'Racing Arcade',
            'image': 'images/3Dteasers/SpeedMaster.jpg',
            'external_link': 'https://play.famobi.com/speed-master',
            'is_external': True
        },
        {
            'name': 'Crazy Caves',
            'category': 'Adventure Arcade',
            'image': 'images/3Dteasers/CrazyCaves.jpg',
            'external_link': 'https://play.famobi.com/crazy-caves',
            'is_external': True
        },

        
        
    ]
    # Retrieve the game based on the slug
    game = next((item for item in Argames if item['slug'] == slug), None)
    if not game:
        return render(request, '404.html', status=404)
    return render(request, 'FamusApp/game_detail.html', {'game': game})

# About Page
def about(request):
    return render(request, 'FamusApp/about.html')

# Privacy Policy Page
def privacy_policy(request):
    return render(request, 'FamusApp/privacy_policy.html')

# Terms of Service Page
def terms_of_service(request):
    return render(request, 'FamusApp/terms_of_service.html')

