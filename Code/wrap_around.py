import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import random


WIDTH = 800
HEIGHT = 600
martian = Actor('martian.png', anchor=('left', 'top'))
martian.vx = 5
x = random.randint(0, WIDTH) + WIDTH
martian.x = x
print('x, y:', martian.x, martian.y)


def draw():
    screen.clear()

    screen.fill((70, 70, 30))
    martian.draw()


def update():
    martian.x -= martian.vx
    if martian.right <= 0:
        martian.x = WIDTH  # wraps around


pgzrun.go()
