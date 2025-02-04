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
                
                