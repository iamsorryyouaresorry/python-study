#전투기가 운석과 충돌하거나 운석을 놓치면 게임오버2


x += fighterX
if x < 0:
    x = 0
elif x > padWidth - fighterWidth:
    x = padWidth - fighterWidth
    
    
if y < rockY + rockHeight:
    if(rockX > x and rockX < x + fighterWidth) or \
        (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth)
        crash()
        
drawObject(fighter, x, y)



if rockPassed == 3:
    gameOver()


writePassed(rockPassed)

