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