#전투기 넣기 2


    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
        drawObject(background, 0, 0)
        
        drawObject(fighter, x, y)
        
        
        