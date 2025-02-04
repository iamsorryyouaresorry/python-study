#미사일로 운석 파괴하기1


def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('missile.png')
    clock = pygame.time.Clock()
    
    
def runGame():
    global gamepad, clock, backkground, fighter, missile, explosion
    
    
    isShot = False
    shotCount = 0
    rockPassed = 0
    
    onGame = False
    while not onGame: