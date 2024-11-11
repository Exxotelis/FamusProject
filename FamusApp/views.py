from django.shortcuts import render
from .models import Product
from blog.models import Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    
    return render(request, 'FamusApp/home.html', {'posts':posts})

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
        {
            'name': 'Mahjong3d',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/Mahjong3d.jpg',
            'external_link': 'https://play.famobi.com/mahjong-3d',
            'is_external': True
        },
        {
            'name': 'ElementBlocks',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/ElementBlocks.jpg',
            'external_link': 'https://play.famobi.com/element-blocks',
            'is_external': True
        },
        {
            'name': 'BlocksPuzzleZoo',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/BlocksPuzzleZoo.jpg',
            'external_link': 'https://play.famobi.com/blocks-puzzle-zoo',
            'is_external': True
        },
        {
            'name': '1000Blocks',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/1000Blocks.jpg',
            'external_link': 'https://play.famobi.com/1000-blocks',
            'is_external': True
        },
                {
            'name': 'PipePuzzle',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/PipePuzzle.jpg',
            'external_link': 'https://play.famobi.com/pipe-puzzle',
            'is_external': True
        },
        {
            'name': 'EmojiFun',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/EmojiFun.jpg',
            'external_link': 'https://play.famobi.com/emoji-fun',
            'is_external': True
        },
        {
            'name': 'FunnyFred',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/FunnyFred.jpg',
            'external_link': 'https://play.famobi.com/funny-fred',
            'is_external': True
        },
        {
            'name': 'ParkingJam',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/ParkingJam.jpg',
            'external_link': 'https://play.famobi.com/parking-jam',
            'is_external': True
        },
        {
            'name': 'KumbaKarate1',
            'category': 'Sports',
            'image': 'images/3Dteasers/KumbaKarate1.jpg',
            'external_link': 'https://play.famobi.com/kumba-karate',
            'is_external': True
        },
        {
            'name': 'SpeedBilliards',
            'category': 'Sports',
            'image': 'images/3Dteasers/SpeedBilliards.jpg',
            'external_link': 'https://play.famobi.com/speed-pool-king',
            'is_external': True
        },
        {
            'name': 'KatanaFruits',
            'category': 'Adventure Arcade',
            'image': 'images/3Dteasers/KatanaFruits.jpg',
            'external_link': 'https://play.famobi.com/katana-fruits',
            'is_external': True
        },        
        {
            'name': 'Sheepop',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/Sheepop.jpg',
            'external_link': 'https://play.famobi.com/sheepop',
            'is_external': True
        },
        {
            'name': 'RabbitPunch',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/RabbitPunch.jpg',
            'external_link': 'https://play.famobi.com/rabbit-punch',
            'is_external': True
        },
        {
            'name': 'Knightower',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/Knightower.jpg',
            'external_link': 'https://play.famobi.com/knightower',
            'is_external': True
        },
        {
            'name': 'SpectTeaser',
            'category': '3D',
            'image': 'images/3Dteasers/SpectTeaser.jpg',
            'external_link': 'https://play.famobi.com/spect',
            'is_external': True
        },        
        {
            'name': 'BurgerMaker',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/BurgerMaker.jpg',
            'external_link': 'https://play.famobi.com/burger-maker',
            'is_external': True
        },
        {
            'name': 'Bananamania',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/Bananamania.jpg',
            'external_link': 'https://play.famobi.com/bananamania',
            'is_external': True
        },
        {
            'name': 'GoldMine',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/GoldMine.jpg',
            'external_link': 'https://play.famobi.com/gold-mine',
            'is_external': True
        },
        {
            'name': 'TowerMania',
            'category': '3D',
            'image': 'images/3Dteasers/TowerMania.jpg',
            'external_link': 'https://play.famobi.com/tower-mania',
            'is_external': True
        },        
        {
            'name': 'TimberMan',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/TimberMan.jpg',
            'external_link': 'https://play.famobi.com/timber-man',
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
        {
            'name': 'Mahjong3d',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/Mahjong3d.jpg',
            'external_link': 'https://play.famobi.com/mahjong-3d',
            'is_external': True
        },
        {
            'name': 'ElementBlocks',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/ElementBlocks.jpg',
            'external_link': 'https://play.famobi.com/element-blocks',
            'is_external': True
        },
        {
            'name': 'BlocksPuzzleZoo',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/BlocksPuzzleZoo.jpg',
            'external_link': 'https://play.famobi.com/blocks-puzzle-zoo',
            'is_external': True
        },
        {
            'name': '1000Blocks',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/1000Blocks.jpg',
            'external_link': 'https://play.famobi.com/1000-blocks',
            'is_external': True
        },
                {
            'name': 'PipePuzzle',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/PipePuzzle.jpg',
            'external_link': 'https://play.famobi.com/pipe-puzzle',
            'is_external': True
        },
        {
            'name': 'EmojiFun',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/EmojiFun.jpg',
            'external_link': 'https://play.famobi.com/emoji-fun',
            'is_external': True
        },
        {
            'name': 'FunnyFred',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/FunnyFred.jpg',
            'external_link': 'https://play.famobi.com/funny-fred',
            'is_external': True
        },
        {
            'name': 'ParkingJam',
            'category': 'Puzzle',
            'image': 'images/3Dteasers/ParkingJam.jpg',
            'external_link': 'https://play.famobi.com/parking-jam',
            'is_external': True
        },
        {
            'name': 'KumbaKarate1',
            'category': 'Sports',
            'image': 'images/3Dteasers/KumbaKarate1.jpg',
            'external_link': 'https://play.famobi.com/kumba-karate',
            'is_external': True
        },
        {
            'name': 'SpeedBilliards',
            'category': 'Sports',
            'image': 'images/3Dteasers/SpeedBilliards.jpg',
            'external_link': 'https://play.famobi.com/speed-pool-king',
            'is_external': True
        },
        {
            'name': 'KatanaFruits',
            'category': 'Adventure Arcade',
            'image': 'images/3Dteasers/KatanaFruits.jpg',
            'external_link': 'https://play.famobi.com/katana-fruits',
            'is_external': True
        },        
        {
            'name': 'Sheepop',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/Sheepop.jpg',
            'external_link': 'https://play.famobi.com/sheepop',
            'is_external': True
        },
        {
            'name': 'RabbitPunch',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/RabbitPunch.jpg',
            'external_link': 'https://play.famobi.com/rabbit-punch',
            'is_external': True
        },
        {
            'name': 'Knightower',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/Knightower.jpg',
            'external_link': 'https://play.famobi.com/knightower',
            'is_external': True
        },
        {
            'name': 'SpectTeaser',
            'category': '3D',
            'image': 'images/3Dteasers/SpectTeaser.jpg',
            'external_link': 'https://play.famobi.com/spect',
            'is_external': True
        },        
        {
            'name': 'BurgerMaker',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/BurgerMaker.jpg',
            'external_link': 'https://play.famobi.com/burger-maker',
            'is_external': True
        },
        {
            'name': 'Bananamania',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/Bananamania.jpg',
            'external_link': 'https://play.famobi.com/bananamania',
            'is_external': True
        },
        {
            'name': 'GoldMine',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/GoldMine.jpg',
            'external_link': 'https://play.famobi.com/gold-mine',
            'is_external': True
        },
        {
            'name': 'TowerMania',
            'category': '3D',
            'image': 'images/3Dteasers/TowerMania.jpg',
            'external_link': 'https://play.famobi.com/tower-mania',
            'is_external': True
        },        
        {
            'name': 'TimberMan',
            'category': 'Classic Arcade',
            'image': 'images/3Dteasers/TimberMan.jpg',
            'external_link': 'https://play.famobi.com/timber-man',
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

