import pygame
from StartGame import start

Brown = (93, 64, 55)
LightBeige = (255, 224, 178)

pygame.init()
selectWindow = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Select Algorithm and Difficulty Level')

def makeSelectGUI(selectWindow):
    selectWindow.fill(LightBeige)
    # Minimax Algorithm Button
    pygame.draw.rect(selectWindow, Brown, (120, 50, 250, 50))  # 50 100
    textFont = pygame.font.Font(None, 36)
    text = textFont.render("Minimax Algorithm", True, LightBeige)
    textX = 120 + int(250 - text.get_width())/2
    textY = 50 + int((50 - text.get_height())/2)
    selectWindow.blit(text, (textX, textY))

    # Alpha-Beta Pruning Algorithm Button
    pygame.draw.rect(selectWindow, Brown, (120, 120, 250, 50))  # 120 170
    textFont1 = pygame.font.Font(None, 36)
    text1 = textFont1.render("Alpha-Beta Pruning", True, LightBeige)
    textX1 = 120 + int(250 - text1.get_width())/2
    textY1 = 120 + int((50 - text1.get_height())/2)
    selectWindow.blit(text1, (textX1, textY1))

    # draw line
    start1 = (83, 35)
    end1 = (400, 35)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)
    start1 = (83, 185)
    end1 = (400, 185)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)
    start1 = (83, 35)
    end1 = (83, 185)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)
    start1 = (400, 35)
    end1 = (400, 185)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)

    # Easy Button
    pygame.draw.rect(selectWindow, Brown, (120, 230, 250, 50))  # 230 280
    textFont2 = pygame.font.Font(None, 36)
    text2 = textFont2.render("Easy", True, LightBeige)
    textX2 = 120 + int(250 - text2.get_width()) / 2
    textY2 = 230 + int((50 - text2.get_height()) / 2)
    selectWindow.blit(text2, (textX2, textY2))

    # Medium Button
    pygame.draw.rect(selectWindow, Brown, (120, 300, 250, 50))  # 300 350
    textFont3 = pygame.font.Font(None, 36)
    text3 = textFont3.render("Medium", True, LightBeige)
    textX3 = 120 + int(250 - text3.get_width()) / 2
    textY3 = 300 + int((50 - text3.get_height()) / 2)
    selectWindow.blit(text3, (textX3, textY3))

    # Hard Button
    pygame.draw.rect(selectWindow, Brown, (120, 370, 250, 50))  # 370 420
    textFont4 = pygame.font.Font(None, 36)
    text4 = textFont4.render("Hard", True, LightBeige)
    textX4 = 120 + int(250 - text4.get_width()) / 2
    textY4 = 370 + int((50 - text4.get_height()) / 2)
    selectWindow.blit(text4, (textX4, textY4))

    # draw line
    start1 = (83, 215)
    end1 = (400, 215)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)
    start1 = (83, 435)
    end1 = (400, 435)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)
    start1 = (83, 215)
    end1 = (83, 435)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)
    start1 = (400, 215)
    end1 = (400, 435)
    pygame.draw.line(selectWindow, Brown, start1, end1, 5)

    pygame.display.update()


def select():
    run = True
    algo = 0
    level = 0

    while run:
        makeSelectGUI(selectWindow)

        if algo != 0 and level != 0:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # (x,y)
            x, y = pos
            if 50 <= y <= 100:
                algo = 1
            elif 120 <= y <= 170:
                algo = 2
            elif 230 <= y <= 280:
                level = 1
            elif 300 <= y <= 350:
                level = 2
            elif 370 <= y <= 420:
                level = 3


    pygame.quit()
    return algo, level


algoNum, levelNum = select()
if algoNum !=0 and levelNum!=0:
    start(algoNum, levelNum)
