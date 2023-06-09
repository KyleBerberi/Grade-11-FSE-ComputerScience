import pgzrun
from pgzero.actor import Actor
from random import randint
from pgzero.keyboard import keyboard
import random
from subprocess import call
import time

global music
WIDTH = 800
HEIGHT = 554
player = Actor('mc.png')
bg = Actor('bg.png')
heart1 = Actor('heart.png')
heart2 = Actor('heart.png')
heart3 = Actor('heart.png')
endscreen1 = Actor('endscreen1.png')
endscreen2 = Actor('endscreen2.png')
endscreen3 = Actor('endscreen3.png')

heart1.pos =(10,10)
heart2.pos =(10,10)
heart3.pos =(10,10)
player.pos = (400, 470)
bullets = []
enemy_bullets = []
health = 100
lives = 3
gamestate = 0
kong = Actor("enemy")
kong.pos = (WIDTH // 2, 50)
kong.velocity = 2

tracks = ['menu', 'menu2', 'menu3']
track = randint(0, 2)
music.set_volume(0.3)
music.play(tracks[track])

start = Rect((270, 170), (250, 100))
setting = Rect((270, 400), (250, 100))
exit = Rect((270, 280), (250, 100))

end_screen_timer = 0
SHOW_END_SCREEN_DURATION = 5  # in seconds
SHOW_END_SCREEN2_DURATION = 3  # in seconds

def draw():
    global gamestate
    global screen
    global Rect
    screen.clear()
    if gamestate == 0:
        bg.draw()
    elif gamestate == 1:
        screen.blit('jungle', (0, 0))
        player.draw()
    if lives = 3:
        heart1.draw()
        heart2.draw()
        heart3.draw()
    if lives = 2:
        kong.draw()
        for bullet in bullets:
            bullet.draw()
        for enemy_bullet in enemy_bullets:
            enemy_bullet.draw()
        health_bar_width = health * 2
        screen.draw.filled_rect(Rect((50, 50), (health_bar_width, 20)), "red")
    elif gamestate == 10:
        endscreen1.draw()
    elif gamestate == 2:
        endscreen2.draw()

def on_mouse_down(pos):
    global gamestate
    if start.collidepoint(pos):
        print('Start')
        gamestate = 1
    elif setting.collidepoint(pos):
        print('Exit')
    elif exit.collidepoint(pos):
        print('Menu')

def update():
    global gamestate, end_screen_timer
    if gamestate == 1:
        global health, lives

        if keyboard.left:
            player.x -= 5
            player.flip_x = True
        elif keyboard.right:
            player.x += 5
            player.angle = 0

        if player.x < 18:
            player.x = 18
        if player.x > 782:
            player.x = 782

        for bullet in reversed(range(len(bullets))):
            bullets[bullet].y -= bullets[bullet].vy

            if bullets[bullet].y <= 0:
                del bullets[bullet]
            else:
                for enemy_bullet in reversed(range(len(enemy_bullets))):
                    if bullets[bullet].colliderect(enemy_bullets[enemy_bullet]):
                        del bullets[bullet]
                        del enemy_bullets[enemy_bullet]
                        break
                else:
                    if bullets[bullet].colliderect(kong):
                        bullets.remove(bullets[bullet])
                        health -= 10

        for enemy_bullet in reversed(range(len(enemy_bullets))):
            enemy_bullets[enemy_bullet].y += enemy_bullets[enemy_bullet].vy
            if enemy_bullets[enemy_bullet].y >= HEIGHT:
                del enemy_bullets[enemy_bullet]
            else:
                if enemy_bullets[enemy_bullet].colliderect(player):
                    enemy_bullets.remove(enemy_bullets[enemy_bullet])
                    health -= 10
                    lives -= 1
                    if lives == 0:
                        gamestate = 10
                        end_screen_timer = time.time()

        kong.x += kong.velocity

        if kong.left < 0 or kong.right > WIDTH:
            kong.velocity *= -1
        if random.random() < 0.01:  # Adjust the firing rate of the enemy
            fire_enemy_bullet()

        if health <= 0:
            gamestate = 2
            end_screen_timer = time.time()

    elif gamestate == 10:
        if time.time() - end_screen_timer >= SHOW_END_SCREEN_DURATION:
            gamestate = 0

    elif gamestate == 2:
        if time.time() - end_screen_timer >= SHOW_END_SCREEN2_DURATION:
            gamestate = 0

def on_key_down(key):
    global keys
    if key == keys.SPACE:
        fire_bullet()

def fire_bullet():
    bullet = Actor('bullets')
    bullet.vy = 3
    bullet.pos = (player.x + 25, player.y - 38)
    bullets.append(bullet)

def fire_enemy_bullet():
    enemy_bullet = Actor('banana')
    enemy_bullet.vy = 3
    enemy_bullet.pos = (kong.x + 20, kong.y + 30)
    enemy_bullets.append(enemy_bullet)

pgzrun.go()
