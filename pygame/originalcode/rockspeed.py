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
        
        
        