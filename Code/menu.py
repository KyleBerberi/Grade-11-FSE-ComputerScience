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
menu = Actor('menu.png')
exit = Actor('exit.png')
heart1 = Actor('heart1.png')
heart2 = Actor('heart2.png')
heart3 = Actor('heart3.png')
end_screen1 = Actor('end_screen1.png')
end_screen2 = Actor('end_screen2.png')
end_screen3 = Actor('end_screen3.png')

monkey_x = 0
monkey_y = 0
monkey_shoot = 0
player_y = 0
player_x = 0
player_shoot = 0

heart1.pos = (60, 30)
heart2.pos = (100, 30)
heart3.pos = (140, 30)
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
    global game_state, screen, level
    screen.clear()
    if game_state == 0:
        bg.draw()
    elif game_state == 5:
        end_screen2.draw()
    elif game_state == 1 or game_state == 3:
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
    elif game_state == 20:
        menu.draw()
    elif game_state == 30:
        exit.draw()


def on_mouse_down(pos):
    global game_state, music
    if start.collidepoint(pos):
        print('Start')
        game_state = 1
        main_track = 'song1'
        music.set_volume(0.3)
        music.play(main_track)
    elif setting.collidepoint(pos):
        game_state = 20
    elif exit_button.collidepoint(pos):
        game_state = 30


def update():
    global game_state, timer, music, fire_rate, health, lives
    if time.time() - timer >= 8:
        sounds.monkey.play()
        timer = time.time()
    if keyboard.left:
        player.x -= 5
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
            for i in reversed(range(len(enemy_bullets))):
                if bullets[bullet].colliderect(enemy_bullets[i]):
                    sounds.splat.play()
                    del bullets[bullet]
                    del enemy_bullets[i]
                    break
            else:
                if bullets[bullet].colliderect(kong):
                    sounds.metal.play()
                    bullets.remove(bullets[bullet])
                    health -= 10

    for i in reversed(range(len(enemy_bullets))):
        enemy_bullets[i].y += enemy_bullets[i].vy
        if enemy_bullets[i].y >= HEIGHT:
            del enemy_bullets[i]
        else:
            if enemy_bullets[i].colliderect(player):
                del enemy_bullets[i]
                lives -= 1
                if lives == 0:
                    game_state = 10
                    timer = time.time()
                    sounds.lose.play()
                    reset_game()  # Reset the game when lives reach 0
                elif lives == 2:
                    heart3.image = 'empty_heart.png'
                    sounds.hit.play()  # Play 'hit' sound when a live is lost
                elif lives == 1:
                    heart2.image = 'empty_heart.png'
                    sounds.hit.play()  # Play 'hit' sound when a live is lost
                    break

    kong.x += kong.velocity

    if kong.left < 0 or kong.right > WIDTH:
        kong.velocity *= -1
    if random.random() < fire_rate:  # Adjust the firing rate of the enemy
        fire_enemy_bullet()
        sounds.throw.play()

    if health <= 0:
        timer = time.time()
        game_state = 5
        sounds.win.play()

elif game_state == 10:
if time.time() - timer >= timer1:
    game_state = 0

elif game_state == 5:
if time.time() - timer >= timer2:
    if time.time() - timer >= timer1:
        game_state = 3
        print('gamestate = 3')

if game_state == 3:
    health = 150
    lives = 3
    heart2.image = 'heart2.png'
    heart3.image = 'heart3.png'
    fire_rate += 3.9
    print('level2')


def reset_game():
    global health, lives, bullets, enemy_bullets
    health = 100
    lives = 3
    bullets = []
    enemy_bullets = []
    heart2.image = 'heart2.png'
    heart3.image = 'heart3.png'
    music.stop()  # Stop the current music
    menu_tracks = ['menu', 'menu2', 'menu3']
    track = randint(0, 2)
    music.set_volume(0.3)
    music.play(menu_tracks[track])


def level2():
    global health, lives, bullets, enemy_bullets, game_state, timer, music, fire_rate
    health = 150
    lives = 3
    bullets = []
    enemy_bullets = []
    heart2.image = 'heart2.png'
    heart3.image = 'heart3.png'
    fire_rate += 3.9
    print('level2')


def on_key_down(key):
    global keys, game_state
    if game_state == 20 and key == keys.ESCAPE:
        game_state = 0
    if key == keys.SPACE:
        fire_bullet()
        sounds.gun.play()
    if game_state == 30 and key == keys.ESCAPE:
        game_state = 0


def fire_bullet():
    bullet = Actor('bullets.png')  # Update the image filename to 'bullet.png'
    bullet.vy = 3
    bullet.pos = (player.x + 25, player.y - 38)
    bullets.append(bullet)


def fire_enemy_bullet():
    enemy_bullet = Actor('banana')
    enemy_bullet.vy = 3
    enemy_bullet.pos = (kong.x + 20, kong.y + 30)
    enemy_bullets.append(enemy_bullet)


pgzrun.go()
