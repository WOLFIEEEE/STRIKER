import pygame
import random
import math

# import the sound class

from pygame import mixer
# intialize the pygame

pygame.init()

# create a screen
screen = pygame.display.set_mode((800,600))

# changing icon and title of game
pygame.display.set_caption("Kicker")
icon=pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# player
Player = pygame.image.load('player.png')
PlayerX = 370
PlayerY = 480
PlayerX_change=0
PlayerY_change=0

# goal
Goal = pygame.image.load('goal.png')
GoalX = random.randint(0,800)
GoalY = 0
GoalX_change=1.5
GoalY_change=0

#background sound
mixer.music.load('Bgmusic.wav')
mixer.music.play(-1)

# ball
# ready = is when the ball is invisible and not seen
# FIre= when the shot is fired

Ball= pygame.image.load('ball.png')
BallX=0
BallY=480
BallX_change=0
BallY_change=3
Ball_state='ready'
# BACKGROUND
BG= pygame.image.load('BG.png')


#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10

# game over

over_font=pygame.font.Font('freesansbold.ttf',74)
#show score


def show_score(x,y):
    score= font.render("GOAL:- " + str(score_value) , True , (0,0,0))
    screen.blit(score,(x,y))

# show game over

def show_over():
    Over= over_font.render('GAME OVER',True,(0,0,0))
    screen.blit(Over,(200,250))

# drwaing player on  screen


def player(x,y):
    screen.blit(Player,(x,y))

# drawing goal on screen


def goal(x,y):
    screen.blit(Goal,(x,y))

# drwaing ball on screen

k=0
def ball(x,y):
    global Ball_state
    global BallY
    global k
    Ball_state='fire'
    BallY = y
    screen.blit(Ball , (x , y))




# checking collision


def is_collide( BallX , BallY , GoalX , GoalY ):

    distance = math.sqrt(math.pow((BallX-GoalX),2)+math.pow((BallY-GoalY),2))
    if distance<27:
        return True
    else:
        return False


running = True
# game loop
while running:
    # R G B
    screen.fill((0, 0, 0))

    # background image
    screen.blit(BG,(0,0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # playing with keys for player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('LEFT KEY IS PRESSED')
                PlayerX_change=-2
            if event.key == pygame.K_RIGHT:
                print('RIGHT KEY IS PRESSED')
                PlayerX_change=2
            if event.key == pygame.K_UP:
                print('up key is pressed')
                PlayerY_change=-2
            if event.key == pygame.K_DOWN:
                print('down key is pressed')
                PlayerY_change=2
            # ball function calling
            if event.key ==pygame.K_SPACE:
                print('space key is pressed')
                if Ball_state is 'ready':
                    Ball_sound=mixer.Sound('kick.wav')
                    Ball_sound.play()
                    k+=1
                    BallX=PlayerX
                    ball(BallX,BallY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print('key has been release')
                PlayerX_change=0
                PlayerY_change=0

# MOVING THE GOAL
    GoalX+=GoalX_change
    if GoalX>=736:
        GoalX_change=-1.5
    elif GoalX<=0:
        GoalX_change=1.5




# Moving the Ball

    if BallY<=0:
        BallY=PlayerY
        Ball_state = 'ready'


    if Ball_state is 'fire':
        ball(BallX,BallY)
        BallY-=BallY_change


# MAKING A BOUNDARY FOR PLAYER
    PlayerX+=PlayerX_change
    PlayerY+=PlayerY_change
    if PlayerX<=0:
        PlayerX=0
    elif PlayerX>=736:
        PlayerX=736
    if PlayerY <= 450:
        PlayerY = 450
    elif PlayerY >= 536:
        PlayerY = 536


    #collision
    if k<10:

        collision=is_collide(BallX,BallY,GoalX,GoalY)
        if collision is True:
            Co_sound=mixer.Sound('yeehaw.wav')
            Co_sound.play()
            BallY=PlayerY
            Ball_state='ready'
            score_value=score_value+1
    else:
        show_over()




    show_score(textX,textY)
    player (PlayerX,PlayerY)
    goal(GoalX,GoalY)
    pygame.display.update()