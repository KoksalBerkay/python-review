import pygame as pg
import sys, random

def ball_anim():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_heigth:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_anim():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_heigth:
        player.bottom = screen_heigth

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_heigth:
        opponent.bottom = screen_heigth

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_heigth/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# General setup
pg.init()
clock = pg.time.Clock()

# Setting up the main window
screen_width = 1280
screen_heigth = 960
screen = pg.display.set_mode((screen_width, screen_heigth))
pg.display.set_caption("Pong")

# Rectangless
ball = pg.Rect(screen_width/2 - 15,screen_heigth/2 -15,30,30)
player = pg.Rect(screen_width - 20,screen_heigth/2 -70,10,140)
opponent = pg.Rect(10, screen_heigth/2 - 70, 10, 140)

bg_color = pg.Color("grey12")
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                player_speed += 7
            if event.key == pg.K_UP:
                player_speed -= 7
        if event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                player_speed -= 7
            if event.key == pg.K_UP:
                player_speed += 7
                
    ball_anim()
    player_anim()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pg.draw.rect(screen,light_grey, player)
    pg.draw.rect(screen,light_grey, opponent)
    pg.draw.ellipse(screen, light_grey, ball)
    pg.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_heigth))

    # Updating the screen
    pg.display.flip()
    clock.tick(60)