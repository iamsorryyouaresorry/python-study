#게임 사운드 넣기2


def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('explosion.png')
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('missile.wav')
    gameOverSound = pygame.mixer.Sound('gameover.wav')
    clock = pygame.time.Clock()
    
    
def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound
    
    
elif event.key == pygame.K_SPACE:
    missileSound.play()
    missileX = x +fighterWidth/2
    missileY = y - fighterHeight
    missileXY.append([missileX, missileY])
    
    