#랜덤한 운석 떨어지기2


missileXY = []


rock = pygame.image.load(random.choice(rockImage))
rockSize = rock.get_rect().size
rockWidth = rockSize[0]
rockHeight = rockSize[1]


rockX = random.randrange(0, padWidht - rockWidth)
rockY = 0
rockSpeed = 2