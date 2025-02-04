#전투기 넣기 1

def initGame():
    global gamePad, clock, background, fighter
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_cation('PyShooting')
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    clock = pygame.time.Clock()
    
def runGame():
    global gamepad, clock, background, fighter
    
    
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]
    
    
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
    

        
        