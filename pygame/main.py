import pygame
import sys
from time import sleep

BLACK = (0, 0, 0)
padWidth = 480
padHeight = 640

def initGame():
    global gamePad, clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    clock = pygame.time.Clock()
    
    
def runGame():
    global gamepad, clock
    
    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
        gamePad.fill(BLACK)
        
        pygame.display.update()
        
        clock.tick(60)
        
    pygame.quit()
    
initGame()
runGame()



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
        
        
#전투기 넣기

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
    

        
#전투기 넣기 2


    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
        drawObject(background, 0, 0)
        
        drawObject(fighter, x, y)
        
        
#전투기 움직이기

onGame = False
while not onGame:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()
            
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:
                fighterX -= 5
                
            elif event.key == pygame.K_RIGHT:
                fighterX += 5
                
        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key = pygame.K_RIGHT:
                fighterX = 0
                
    drawObject(background, 0, 0)                          
    
    
    x += fighterX
    if x < 0:
        x = 0
    elif x > padWidth - fighterWidth:
        x = padWidth = fighterWidth
        
        
        
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
    global gamepad, clock, background, fighter, missile
    
    
    missileXY = []
    


#미사일 발사하기2


onGame = False
while not onGame:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()
            
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:
                fighterX -= 5
                
            elif event.key == pygame.K_RIGHT:
                fighterX += 5
                
            elif event.key == pygame.K_SPACE:
                missileX = x + fighterWidth/2
                missileY = y - fighterHeight
                missileXY.append([missileX, missileY])
                
                
                
#미사일 발사하기3


drawObject(fighter, x, y)

if len(missileXY) !=0:
    for i, bxy in enumerate(missileXY):
        bxy[1] -= 10
        missileXY[i][1] = bxy[1]
        
        if bxy[1] <= 0:
            try:
                missileXY.remove(bxy)
            except:
                pass
            
if len(missileXY) != 0:
    for bx, by in missileXY:
        drawObject(missile, bx, by)
        
pygame.display.update()


#랜덤한 운석 떨어지기1


import pygame
import sys
import random
from time import sleep

padWidth = 480
padHeight = 640
rockImage = [
    'rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
    'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
    'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
    'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
    'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
    'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png'
]


#랜덤한 운석 떨어지기2


missileXY = []


rock = pygame.image.load(random.choice(rockImage))
rockSize = rock.get_rect().size
rockWidth = rockSize[0]
rockHeight = rockSize[1]


rockX = random.randrange(0, padWidht - rockWidth)
rockY = 0
rockSpeed = 2


#랜덤한 운석떨어지기3


if len(missileXY) != 0:
    for bx, by in missileXY:
        drawObject(missile, bx, by)
        
rockY += rockSpeed


if rockY > padHeight:
    
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidht - rockWidth)
    rockY = 0
    
drawObject(rock, rockX, rockY)

pygame.display.update()



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
        
        
#미사일로 운석 파괴하기 2


if len(missileXY) !=0:
    for i, bxy in enumerate(missileXY):
        bxy[1] -= 10
        missileXY[i][1] = bxy[1]
        
        
        if bxy[1] < rockY:
            if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                missileXY.remove(bxy)
                isShot = True
                shotCount += 1
                
            if bxy[1] <= 0:
                try:
                    missileXY.remove(bxy)
                except:
                    pass
                

#미사일로 운석파괴하기3


if isShot:
    
    drawObject(explosion, rockX, rockY)
    
    
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidht - rockWidth)
    rockY = 0
    isShot =False
    
drawObject(rock, rockX, rockY)


# 파괴한 운석 수와 놓친 운석 수 표시


def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:' + str(countr), True, (255,255,255))
    gamePad.blit(text,(10,0))
    
    
    
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('놓친 운석 :' + str(count), True, (255,0,0))
    gamePad.blit(text, (360,0))
    
    
#파괴한 운석 수와 놓친 운석 수 표시하기 2


writeScore(shotCount)

rockY += rockSpeed


if rockY > padHeight:
    
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockPassed += 1

writePassed(rockPassed)


# 운석 맞추면 운석 속도 증가하기

if isShot:
    
    drawObject(explosion, rockX, rockY)
    
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect()>rockSize
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    isShot = False
    
    rockSpeed += 0.02
    if rockSpeed >= 10:
        rockSpeed = 10
        
        
#전투기가 운석과 충돌하거나 운석을 놓치면 게임오버1
 
 
def writeMessage(text):
    global gamePad
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()
    
    
def crash():
    global gamePad
    writeMessage('전투기 파괴!')
    
    
def gameOver():
    global gamePad
    writeMessage('게임 오버!')
    


#전투기가 운석과 충돌하거나 운석을 놓치면 게임오버2


x += fighterX
if x < 0:
    x = 0
elif x > padWidth - fighterWidth:
    x = padWidth - fighterWidth
    
    
if y < rockY + rockHeight:
    if(rockX > x and rockX < x + fighterWidth) or \
        (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth)
        crash()
        
drawObject(fighter, x, y)



if rockPassed == 3:
    gameOver()


writePassed(rockPassed)



#게임 사운드 넣기1


padWidth = 480
padHeight = 640
rockImage = [
    'rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
    'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
    'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
    'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
    'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
    'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png'
]
explosionSound = ['explosion01.wav','explosion02.wav','explosion03.wav','explosion04.wav']



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
    missileX = x + fighterWidth/2
    missileY = y - fighterHeight
    missileXY.append([missileX, missileY])
    


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
    runGame()
    
    
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
    
    
                                               