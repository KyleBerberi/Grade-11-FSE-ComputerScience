import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import random


WIDTH = 800
HEIGHT = 600
player = Actor('mc.png', anchor=('left', 'top'))
player.vx = 5
# creating random starting location
#x = random.randint(0, WIDTH) + WIDTH
# random vertical location
# y = random.randint(0, HEIGHT) + HEIGHT
player.x = 50
print('x, y:', player.x, player.y)


def draw():
    screen.clear()
    screen.blit('jungle', (0,0))
    player.draw()


def update():
    player.x += player.vx
    if player.right >= WIDTH or player.left <= 0:
        player.vx *= -1               # bounces from side to side



pgzrun.go()
