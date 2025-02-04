#게임 사운드 넣기3


def writeMessage(text):
    global gamePad, gameOverSound
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameoverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGeme()
    
    
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))
    
    
if isShot:
    
    drawObject(explosion, rockX, rockY)
    
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))
    isShot = False