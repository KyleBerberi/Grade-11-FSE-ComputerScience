import random
import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import sys

WIDTH = 800
HEIGHT = 554

player = Actor('mc.png')
player.pos = (400, 470)

bullets = []
enemy_bullets = []

health = 100
lives = 3

kong = Actor("enemy")
kong.pos = (WIDTH // 2, 50)
kong.velocity = 2

def update():
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
                    call(["python", "mainscreen.py"])

    kong.x += kong.velocity

    if kong.left < 0 or kong.right > WIDTH:
        kong.velocity *= -1
    if random.random() < 0.01:  # Adjust the firing rate of the enemy
        fire_enemy_bullet()

    if health <= 0:
        print("Enemy defeated!")

def draw():
    screen.clear()
    screen.blit('jungle', (0, 0))
    player.draw()
    kong.draw()

    for bullet in bullets:
        bullet.draw()

    for enemy_bullet in enemy_bullets:
        enemy_bullet.draw()

    health_bar_width = health * 2
    screen.draw.filled_rect(Rect((50, 50), (health_bar_width, 20)), "red")

def on_key_down(key):
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

def open_menu():
    call(["python", "mainscreen.py"])

pgzrun.go()
