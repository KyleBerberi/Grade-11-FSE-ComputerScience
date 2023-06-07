import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


WIDTH = 800
HEIGHT = 554
player = Actor('mc.png')
player.pos = (400,470)
def update():
    if keyboard.left:
        player.x -= 5
        # center of rot'n is the anchor point
        player.flip_x = True
    elif keyboard.right:
        player.x += 5
        player.angle = 0
def draw():
    screen.clear()
    screen.blit('jungle', (0,0))
    player.draw()

pgzrun.go()