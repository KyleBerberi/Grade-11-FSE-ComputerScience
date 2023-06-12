
import pgzrun
from pgzero.actor import Actor
from random import randint
from pgzero.keyboard import keyboard
import random
import time

global music
WIDTH = 800
HEIGHT = 554
player = Actor('mc.png')
bg = Actor('bg.png')
heart1 = Actor('heart1.png')
heart2 = Actor('heart2.png')
heart3 = Actor('heart3.png')
end_screen1 = Actor('end_screen1.png')
end_screen2 = Actor('end_screen2.png')
end_screen3 = Actor('end_screen3.png')

heart1.pos = (20, 30)
heart2.pos = (40, 30)
heart3.pos = (60, 30)
player.pos = (400, 470)
bullets = []
enemy_bullets = []
health = 100
lives = 3
game_state = 0
kong = Actor("enemy")
kong.pos = (WIDTH // 2, 50)
kong.velocity = 2

if game_state == 0:
    menu_tracks = ['menu', 'menu2', 'menu3']
    track = randint(0, 2)
    music.set_volume(0.3)
    music.play(menu_tracks[track])

start = Rect((270, 170), (250, 100))
setting = Rect((270, 400), (250, 100))
exit_button = Rect((270, 280), (250, 100))

timer = 0
timer1 = 2  # in seconds
timer2 = 2  # in seconds


def draw():
    global game_state
    global screen
    screen.clear()
    if game_state == 0:
        bg.draw()
    elif game_state == 1:
        screen.blit('jungle', (0, 0))
        player.draw()
        heart1.draw()
        heart2.draw()
        heart3.draw()
        kong.draw()
        for bullet in bullets:
            bullet.draw()
        for enemy_bullet in enemy_bullets:
            enemy_bullet.draw()
        health_bar_width = health * 2
        screen.draw.filled_rect(Rect((50, 50), (health_bar_width, 20)), "red")
    elif game_state == 10:
        end_screen1.draw()
    elif game_state == 2:
        end_screen2.draw()


def on_mouse_down(pos):
    global game_state
    if start.collidepoint(pos):
        print('Start')
        game_state = 1
    elif setting.collidepoint(pos):
        print('Exit')
    elif exit_button.collidepoint(pos):
        print('Menu')


def update():
    global game_state, timer, music
    if game_state == 1:
        global health, lives
        main_track = 'song1'
        music.set_volume(0.3)
        music.play(main_track)
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
                        game_state = 10
                        timer = time.time()

        kong.x += kong.velocity

        if kong.left < 0 or kong.right > WIDTH:
            kong.velocity *= -1
        if random.random() < 0.01:  # Adjust the firing rate of the enemy
            fire_enemy_bullet()

        if health <= 0:
            game_state = 2
            timer = time.time()

    elif game_state == 10:
        if time.time() - timer >= timer1:
            game_state = 0

    elif game_state == 2:
        if time.time() - timer >= timer2:
            


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
