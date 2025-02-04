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


