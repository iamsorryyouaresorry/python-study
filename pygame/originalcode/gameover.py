#전투기가 운석과 충돌하거나 운석을 놓치면 게임오버1
 
 
def writeMessage(text):
    global gamePad
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()
    
    
def crash():
    global gamePad
    writeMessage('전투기 파괴!')
    
    
def gameOver():
    global gamePad
    writeMessage('게임 오버!')
    
    