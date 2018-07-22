import pygame

pygame.init()
from time import *



win = pygame.display.set_mode((1024,642))

pygame.display.set_caption('Великие моменты истории')

walkLeft = [pygame.image.load('7u_L_bok1.png'), pygame.image.load('9u_L_bok2.png')]
walkRight = [pygame.image.load('10u_R_bok1.png'), pygame.image.load('12u_R_bok2.png')]
walkDown = [pygame.image.load('2u_wper1.png'), pygame.image.load('3u_wper2.png')]
walkUp = [pygame.image.load('6u_zad2.png'), pygame.image.load('4u_zad1.png')]
uznikAss = pygame.image.load('5u_stand_zad.png')
uznikDick = pygame.image.load('1u_stand_wper.png')
uznikSpeech = [pygame.image.load('suki.png'),pygame.image.load('love.png')]

bg = pygame.image.load('prison_look.jpg')

clock = pygame.time.Clock()
x = 293
y = 300


width = 34
height = 86
speed = 5

isSpeaking = False
sp_klack = 0

left = False
right = False
up = False
down = False


animCount = 0
diaCount = 0




def drawWindow():
    global animCount
    win.blit(bg, (0,0))
    if animCount + 1 >= 10:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount//5],(x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount//5],(x,y))
        animCount += 1
    elif down:
        win.blit(walkDown[animCount//5],(x,y))
        animCount += 1
    elif up:
        win.blit(walkUp[animCount//5],(x,y))
    elif isSpeaking:
        global sp_klack
        if sp_klack <15:
            win.blit(uznikDick, (x,y))
            win.blit(uznikSpeech[0],(250,150))
        else:
            win.blit(uznikDick, (x,y))
            win.blit(uznikSpeech[1],(250,150))

    else:
        win.blit(uznikDick, (x,y))


    pygame.display.update()


run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>180:
        x -= speed

        isSpeaking = False
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_RIGHT] and x < 341:
        x += speed

        isSpeaking = False
        right = True
        left = False
        up = False
        down = False
    elif keys[pygame.K_UP] and y >260 - height:
        y -= speed

        isSpeaking = False
        up = True
        down = False
        left = False
        right = False
    elif keys[pygame.K_DOWN] and y <476 - height:
        y += speed

        isSpeaking = False
        down = True
        up = False
        left = False
        right = False

    elif keys[pygame.K_f]:
        sp_klack += 1
        isSpeaking = True
        down = False
        up = False
        left = False
        right = False



    else:
        win.blit(uznikDick, (x,y))
        isSpeaking = False

        left = False
        right = False
        up = False
        down = False
        animCount = 0


    drawWindow()





pygame.quit()
