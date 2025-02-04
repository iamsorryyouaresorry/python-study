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
                
                
        