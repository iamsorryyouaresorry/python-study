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
