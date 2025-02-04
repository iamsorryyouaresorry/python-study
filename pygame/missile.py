#미사일 발사하기1


def initGame():
    global gamePad, clock, background, fighter, missile
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    clock = pygame.time.Clock()
    
    
def runGame():
    glocbal gamepad, clock, background, fighter, missile
    
    
    missileXY = []
    
    