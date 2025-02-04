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
        