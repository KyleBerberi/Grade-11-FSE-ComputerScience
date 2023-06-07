import pgzrun
from pgzero.actor import Actor
from random import randint
from pgzero.keyboard import keyboard
import random
from subprocess import call


bg = Actor('bg.png', anchor=(0,0))
WIDTH = 800
HEIGHT = 554

tracks = ['menu', 'menu2', 'menu3']
track = randint(0,2)
music.set_volume(0.3)
music.play(tracks[track])


start = Rect((270, 170), (250, 100))
setting = Rect((270, 400), (250, 100))
exit = Rect((270, 280), (250, 100))


def draw():
    bg.draw()
    """RED = 200, 0, 0
    BLUE = 0, 0, 200
    GREEN = 0, 200, 0
    screen.draw.rect(setting, RED)
    screen.draw.rect(start, BLUE)
    screen.draw.rect(exit, GREEN)"""

def on_mouse_down(pos):
    if start.collidepoint(pos):
        call(["python", "mainscreen.py"])
    elif setting.collidepoint(pos):
        call(["python", "shooting.py"])
    elif exit.collidepoint(pos):
        menu.py.close()

pgzrun.go()