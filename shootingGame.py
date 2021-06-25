import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pg
import random
import copy
from pygame.constants import DROPTEXT
from pygame.math import Vector2
import time
import sys






pg.init()

class Player(pg.sprite.Sprite):

    def __init__(self, pos, color, left, right, up, down, fire,
                all_sprites, bullets, enemy_bullets, enemy_score, name):
        super().__init__()
        self.name = name
        self.image = pg.Surface((30, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        font = pg.font.SysFont('Arial', 20)
        font_color = pg.Color('black')
        textsurface = font.render(name, True, font_color)
        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        self.image.blit(textsurface, textrect)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(self.rect.topleft)
        self.dt = 0.03
        self.key_left = left
        self.key_right = right
        self.key_up = up
        self.key_down = down
        self.key_fire = fire
        # Store the groups as attributes, so that you can add bullets
        # and use them for the collision detection in the update method.
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.enemy_bullets = enemy_bullets
        self.fire_direction = Vector2(350, 0)
        self.enemy_score = enemy_score

    def update(self, dt):
        self.dt = dt
        temp = Player(
            (self.rect.x, self.rect.y), pg.Color('dodgerblue2'),
            pg.K_a, pg.K_d, pg.K_w, pg.K_s, pg.K_SPACE,
            self.all_sprites, None, None, None, "P2")  # Pass the groups.
        temp.rect.topleft = self.pos + self.vel
        collisions = pg.sprite.spritecollide(temp, self.all_sprites, False)
        if len(collisions) > 1 or temp.rect.x > 800 - 30 or temp.rect.y > 600 - 50 or temp.rect.x < 0 or temp.rect.y < 0:
            self.vel.x = 0
            self.vel.y = 0
        else:
            self.pos += self.vel
            self.rect.topleft = self.pos



        # Check if enemy bullets collide with the player, reduce
        # health and kill self if health is <= 0.
        collided_bullets = pg.sprite.spritecollide(self, self.enemy_bullets, True)
        for bullet in collided_bullets:
            self.enemy_score[0] += 1
            if self.enemy_score[0] >= 10:
                self.kill()

        changed_places = False
        while len(collided_bullets) > 0 and changed_places == False:

            x = random.randint(0,770)
            y = random.randint(0,550)
            if (x >= 450 and y <= 57) or (x == self.rect.x and y == self.rect.y):
                continue
            playertemp = Player(
            (x, y), pg.Color('dodgerblue2'),
            pg.K_a, pg.K_d, pg.K_w, pg.K_s, pg.K_SPACE,
            self.all_sprites, None, None, None, "P2")  # Pass the groups.
                
            bumbum = pg.sprite.spritecollide(playertemp, self.all_sprites, False)
            if len(bumbum) == 0:
                changed_places = True
                self.rect.x = x
                self.rect.y = y
                self.pos = Vector2((x,y))


    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.key_left:
                self.vel.x = -90 * self.dt
                self.fire_direction = Vector2(-350, 0)
            elif event.key == self.key_right:
                self.vel.x = 90 * self.dt
                self.fire_direction = Vector2(350, 0)
            elif event.key == self.key_up:
                self.vel.y = -90 * self.dt
                self.fire_direction = Vector2(0, -350)
            elif event.key == self.key_down:
                self.vel.y = 90 * self.dt
                self.fire_direction = Vector2(0, 350)
            elif event.key == self.key_fire:  # Add a bullet to the groups.
                bullet = Bullet(self.rect.center, self.fire_direction)
                self.bullets.add(bullet)
                self.all_sprites.add(bullet)





        elif event.type == pg.KEYUP:
            if event.key == self.key_left and self.vel.x < 0:
                self.vel.x = 0
            elif event.key == self.key_right and self.vel.x > 0:
                self.vel.x = 0
            elif event.key == self.key_up and self.vel.y < 0:
                self.vel.y = 0
            elif event.key == self.key_down and self.vel.y > 0:
                self.vel.y = 0


class Bullet(pg.sprite.Sprite):

    def __init__(self, pos, velocity):
        super().__init__()
        self.image = pg.Surface((5, 5))
        self.image.fill(pg.Color('aquamarine1'))
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.speed = velocity

    def update(self, dt):
        self.pos += self.speed * dt
        self.rect.center = self.pos
        
    def setSpeed(self, speed):
        self.speed = speed


class Game:

    def __init__(self):
        self.fps = 30
        self.done = False
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((800, 600))
        self.font = pg.font.Font("freesansbold.ttf", 32)
        self.text = self.font.render("Hello", True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect = (450, 25)
        self.bg_color = pg.Color('gray30')

        # Sprite groups that contain the players and bullets.
        self.all_sprites = pg.sprite.Group()
        self.bullets1 = pg.sprite.Group()  # Will contain bullets of player1.
        self.bullets2 = pg.sprite.Group()  # Will contain bullets of player2.
        self.p1Score = [0]
        self.p2Score = [0]
        player2 = Player(
            (300, 400), pg.Color('dodgerblue2'),
            pg.K_a, pg.K_d, pg.K_w, pg.K_s, pg.K_SPACE,
            self.all_sprites, self.bullets1, self.bullets2, self.p1Score, "P2")  # Pass the groups.
        player1 = Player(
            (100, 300),  pg.Color('sienna2'),
            pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN, pg.K_RETURN,
            self.all_sprites, self.bullets2, self.bullets1, self.p2Score, "P1")  # Pass the groups.          
        self.all_sprites.add(player1, player2)
        self.players = pg.sprite.Group(player1, player2)
        i = 0
        while i < 5:
            x = random.randint(0,760)
            y = random.randint(0,570)
            if x >= 450 and y <= 57:
                continue

            barrel = Barrel(
                (x,y), pg.Color("green"), self.bullets1, self.bullets2
            )
            bumbum = pg.sprite.pygame.sprite.spritecollide(barrel, self.all_sprites, False)
            if len(bumbum) == 0:
                i = i + 1
                self.all_sprites.add(barrel)
        i = 0
        while i < 7:
            x = random.randint(0,780)
            y = random.randint(0,570)
            if x >= 450 and y <= 57:
                continue

            sandbag = Sandbag(
                (x,y), pg.Color("yellow"), self.bullets1, self.bullets2
            )
            bumbum = pg.sprite.pygame.sprite.spritecollide(sandbag, self.all_sprites, False)
            if len(bumbum) == 0:
                i = i + 1
                self.all_sprites.add(sandbag)
                



    def run(self):
        while not self.done:
            self.dt = self.clock.tick(self.fps) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()
            if self.p1Score[0] >= 10 or self.p2Score[0] >=10:
                self.done = True
        player_sprites = []
        for player in self.players:
            player_sprites.append(player)
        return player_sprites[0].name
            
            
        

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            for player in self.players:
                player.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.screen.fill(self.bg_color)
        self.text = self.font.render("Player1: " + str(self.p1Score[0]) + " Player2: " + str(self.p2Score[0]), True, (255, 255, 255))
        self.screen.blit(self.text, self.textRect)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

        

class Barrel(pg.sprite.Sprite):
    def __init__(self, pos, color, bulletsp1, bulletsp2):
        super().__init__()
        self.image = pg.Surface((40,30))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = Vector2(self.rect.topleft)
        self.bullletsp1 = bulletsp1
        self.bulletsp2 = bulletsp2
        self.dt = 0.03
    def update(self, dt):
        self.dt = dt
        collided_bulletsp1 = pg.sprite.spritecollide(self, self.bullletsp1, True)
        collided_bulletsp2 = pg.sprite.spritecollide(self, self.bulletsp2, True)
        if len(collided_bulletsp1) > 0 or len(collided_bulletsp2) > 0:
            self.kill()


class Sandbag(pg.sprite.Sprite):
    def __init__(self, pos, color, bulletsp1, bulletsp2):
        super().__init__()
        self.image = pg.Surface((20,30))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = Vector2(self.rect.topleft)
        self.bullletsp1 = bulletsp1
        self.bulletsp2 = bulletsp2
        self.dt = 0.03
    def update(self, dt):
        self.dt = dt
        collided_bulletsp1 = pg.sprite.spritecollide(self, self.bullletsp1, True)
        collided_bulletsp2 = pg.sprite.spritecollide(self, self.bulletsp2, True)



if __name__ == '__main__':
    pg.init()
    game = Game()
    winner = game.run()
    

    smallfont = pg.font.SysFont('Corbel',35)
    
    # rendering a text written in
    # this font
    color = (0,255,191)
    color_light = (170,170,170)
    color_dark = (100,100,100)
    text = smallfont.render('RESTART' , True , color)

    black = (0,0,0)
    white = (255,255,255)
    blue = (0,0,225)
    red = (255,0,0)

    width = game.screen.get_width()
    height = game.screen.get_height()
    
        
    font = pg.font.SysFont(None, 35)
    gameDisplay = pg.display.set_mode((width,height))
    def message_to_screen(msg,color):
        screen_text = font.render(msg, True, color)
        gameDisplay.blit(screen_text, [200, 220])

            

    while True:
        pg.init()

        for ev in pg.event.get():
                
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
                    
                    
            #checks if a mouse is clicked
            if ev.type == pg.MOUSEBUTTONDOWN:
                    
                #if the mouse is clicked on the
                # button the game will restart
                if width/2 <= mouse[0] <= width/2+190 and height/2 <= mouse[1] <= height/2+40:
                    pg.init()
                    game = Game()
                    winner = game.run()
                
        # fills the screen with a color
        game.screen.fill((60,25,60))
            
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pg.mouse.get_pos()
            
        # if mouse is hovered on a button it
        # changes to lighter shade 
        if width/2 <= mouse[0] <= width/2+190 and height/2 <= mouse[1] <= height/2+40:
            pg.draw.rect(game.screen,color_light,[width/2,height/2,190,40])
                
        else:
            pg.draw.rect(game.screen,color_dark,[width/2,height/2,190,40])
            
        # superimposing the text onto our button
        game.screen.blit(text , (width/2+30,height/2))
            
        # updates the frames of the game
        statement = "Player " + winner[-1] + " wins, do u wanna play again?"
        message_to_screen(statement, white)
        pg.display.update()
        
