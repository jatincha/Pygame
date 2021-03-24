import pygame
import time

from pygame import mixer

# inialize the pygame
pygame.init()
width,height=800,600

# create the screen
screen = pygame.display.set_mode((width, height))
bg_x = 0
FPS=10

isJump = False
jumpCount = 10
velocity=9

bg = pygame.image.load("background.png")

#background song
mixer.music.load('music.mp3')
mixer.music.play(1)

# title and icon
pygame.display.set_caption("Run Like Hell")
icon = pygame.image.load("pubg.png")
pygame.display.set_icon(icon)

# player
playerImg = [pygame.image.load('p1.png'),pygame.image.load('p2.png'),pygame.image.load('p3.png'),pygame.image.load('p5.png'),pygame.image.load('p6.png'),pygame.image.load('p7.png'),pygame.image.load('p9.png'),pygame.image.load('p10.png')]
playerX =370
playerY = 420
playerX_change = 5
player_Img_count=0
obstacle_count=0
obstacle_x=1200
obstacle_y=460
coin_x=800
coin_y=440
coin_count=0
score=0


gameoverimg=pygame.image.load('Game-Over.png')

obstacle1=[pygame.image.load('cactus.png'),pygame.image.load('cactus (1).png')]
coins=[pygame.image.load('c1.png'),pygame.image.load('c2.png'),pygame.image.load('c3 (1).png'),pygame.image.load('c4 (1).png')]
player_height=playerImg[playerX_change].get_height()
player_width=playerImg[playerX_change].get_width()
coin_height=coins[coin_count].get_height()
coin_width=coins[coin_count].get_width()
obstacle_height=obstacle1[obstacle_count].get_height()
obstacle_width=obstacle1[obstacle_count].get_width()
def coin_animation():
    global coin_x
    global coin_count
    screen.blit(coins[coin_count],(coin_x,coin_y))
    coin_count+=1
    if coin_count +1 > 3:
        coin_count=0
    coin_x-=10
    if coin_x < -100:
        coin_x=1000


def obstacles():
     global obstacle_x
     global obstacle_count
     screen.blit(obstacle1[obstacle_count],(obstacle_x,obstacle_y))
     obstacle_count+=1
     if obstacle_count+1 > 2:
         obstacle_count =0
     obstacle_x-=10
     if obstacle_x < -100:
         obstacle_x=1000

def scrolling_background():
        global bg_x
        relative_x = bg_x % bg.get_rect().width
        screen.blit(bg, (relative_x - bg.get_rect().width, 0))
        if relative_x < width:
            screen.blit(bg, (relative_x, 0))
        bg_x -= 10

def show_score():
    score_obj=pygame.font.SysFont('comicsans',50,True)
    score_txt=score_obj.render("score: "+str(score),1,(0,0,0))
    screen.blit(score_txt,(570,20))
#collision and showing score
def collision():
    global coin_x
    global score
    player_rect =pygame.Rect(playerX,playerY,player_width,player_height)
    coin_rect=pygame.Rect(coin_x,coin_y,coin_width,coin_height)
    blade_rect=pygame.Rect(obstacle_x+20,obstacle_y+20,obstacle_width-20,obstacle_height)
    if player_rect.colliderect(coin_rect):
        mixer.music.load('coin.mp3')
        mixer.music.play()
        coin_x=1000
        score+=1
    if player_rect.colliderect(blade_rect):
        mixer.music.load('game_over.mp3')
        mixer.music.play()
        screen.blit(gameoverimg,(170,250))
        score_obj=pygame.font.SysFont('comicsans',50,True)
        score_txt = score_obj.render("KHATAM TATA BYE BYE",2, (250, 0, 0))
        screen.blit(score_txt,(210,height/2))
        pygame.display.update()
        time.sleep(3)
        quit()


def scrolling_background():
    global bg_x
    relative_x = bg_x % bg.get_rect().width
    screen.blit(bg,(relative_x - bg.get_rect().width,0))
    if relative_x < width:
      screen.blit(bg,(relative_x,0))
    bg_x -=10
clock = pygame.time.Clock()


# game loop
running = True
while running:

    clock.tick(FPS)


    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    scrolling_background()
    obstacles()
    coin_animation()
    show_score()
    collision()
    pygame.display.update()
    screen.blit(playerImg[player_Img_count],(playerX, playerY))
    player_Img_count += 1
    if player_Img_count + 1 > 6:
       player_Img_count = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
                isJump = True
                mixer.music.load('jump.mp3')
                mixer.music.play()
    else:
            if velocity >= -9:
                gravity = 1
                if velocity < 0:
                    gravity = -1
                playerY -= (velocity ** 2) * 0.5 * gravity
                velocity -= 1
            else:
                velocity = 9
                isJump = False
    pygame.display.update()
