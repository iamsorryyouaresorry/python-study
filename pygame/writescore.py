# 파괴한 운석 수와 놓친 운석 수 표시


def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:' + str(countr), True, (255,255,255))
    gamePad.blit(text,(10,0))
    
    
    
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('놓친 운석 :' + str(count), True, (255,0,0))
    gamePad.blit(text, (360,0))
    
    
    