import pygame as pg
import sys, random

def ball_anim():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_heigth:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = pg.time.get_ticks()
    
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pg.time.get_ticks()

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

def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pg.time.get_ticks()
    ball.center = (screen_width/2, screen_heigth/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3",False, light_grey)
        screen.blit(number_three,(screen_width/2 - 10, screen_heigth/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",False, light_grey)
        screen.blit(number_two,(screen_width/2 - 10, screen_heigth/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False, light_grey)
        screen.blit(number_one,(screen_width/2 - 10, screen_heigth/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None
    

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

# Colors
bg_color = pg.Color("grey12")
light_grey = (200,200,200)

# Game variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

# Text variables
player_score = 0
opponent_score = 0
game_font = pg.font.Font("freesansbold.ttf",32)

# Score timer
score_time = True

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

    # Game Logic
    ball_anim()
    player_anim()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pg.draw.rect(screen,light_grey, player)
    pg.draw.rect(screen,light_grey, opponent)
    pg.draw.ellipse(screen, light_grey, ball)
    pg.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_heigth))

    if score_time:
        ball_start()

    player_text = game_font.render(f"{player_score}",False,light_grey)
    screen.blit(player_text,(660,470))

    opponent_text = game_font.render(f"{opponent_score}",False,light_grey)
    screen.blit(opponent_text,(600,470))

    # Updating the screen
    pg.display.flip()
    clock.tick(60)