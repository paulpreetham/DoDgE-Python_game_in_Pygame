
import pygame
import time
import random

pygame.init()
width = 1000
height = 1000
black = (0, 0, 0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green =(0,255 ,0)
white = (255, 255, 255)
blue = (234, 233, 125)
obj_width = 96

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('CATCH The Pokemon')
clock = pygame.time.Clock()
carimage = pygame.image.load('picka.png')

def crash():
    message_display("Game Over")


def things(xt, yt, wt, ht, colour):
    pygame.draw.rect(gameDisplay, colour, [xt, yt, wt, ht])


def car(x, y):
    gameDisplay.blit(carimage, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width / 2), (height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)
    game_loop()


#def crash():
    #message_display('game ended')

def button(msg,x,y,w,h,ic,ac,verb = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    print(mouse)

    if x + w > mouse[0] > x and y + h > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and verb != None:
            if verb == "play":
                game_loop()
            elif verb == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    # if 750 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
    #   pygame.draw.rect(gameDisplay, bright_red,(750,450,100,50))
    # else:

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)
    #pygame.draw.rect(gameDisplay, red, (750, 450, 100, 50))





def game_intro():
     intro = True
     while intro:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
         gameDisplay.fill(blue)
         largeText = pygame.font.Font('freesansbold.ttf', 115)
         TextSurf, TextRect = text_objects("Dodge", largeText)
         TextRect.center = ((width / 2), (height / 2))
         gameDisplay.blit(TextSurf, TextRect)

         button("Start",150,450,100,50 , green, bright_green,"play")
         button("End", 750, 450, 100, 50, red, bright_red,"quit")

         #pygame.draw.rect(gameDisplay, red, (750, 450, 100, 50))
         pygame.display.update()
         clock.tick(10)



def game_loop():
    x = (1000 * 0.25)
    y = (1000 * 0.35)
    x_chg = 0
    y_chg = 0
    thing_startx = random.randrange(0,width)
    thing_starty = -600
    thing_speed = 10
    wt = 100
    ht = 100

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_chg = -5
                if event.key == pygame.K_RIGHT:
                    x_chg = +5
                if event.key == pygame.K_UP:
                    y_chg = -5
                if event.key == pygame.K_DOWN:
                    y_chg = +5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_chg = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_chg = 0

        x += x_chg
        y += y_chg
        gameDisplay.fill(red)

        #things(xt, yt, wt, ht, colour)
        things(thing_startx,thing_starty,wt,ht,black)
        thing_starty += thing_speed
        car(x, y)
        if x > 1000 - obj_width or x < 0:
            crash()
        if thing_starty > height:
           thing_starty = 0 - ht
           thing_startx = random.randrange(0, width)

        if y < thing_starty + ht:


            if x > thing_startx and x < thing_startx + wt or x + obj_width > thing_startx and x + obj_width < thing_startx + wt:

                crash()


        pygame.display.update()
        clock.tick(100)

game_intro()
game_loop()

pygame.quit()
quit()


