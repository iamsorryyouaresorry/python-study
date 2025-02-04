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


