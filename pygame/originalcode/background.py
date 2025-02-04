#배경 그림 넣기기

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))
    
def initGame():
    global gamePad, clock, background
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')    
    background = pygame.image.load('background.png')
    clock = pygame.time.Clock()
    
def runGame():
    global gamepad, clock, background
    
    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
        drawObject(background, 0, 0)
        
        pygame.display.update()