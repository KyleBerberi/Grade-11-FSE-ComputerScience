import pgzrun
from pgzero.actor import Actor
from random import randint
from pgzero.keyboard import keyboard
import random
from subprocess import call
import time


WIDTH = 800
HEIGHT = 554
player = Actor('mc.png')
player.pos = (400,470)
fireballs=[]
seconds = 0
timer = 0

timer += 1
# draw is called at the frame rate - 60x per sec or 30x per sec at schoo’
if timer == 60:
  seconds += 1
  timer = 0

def update():
  global seconds
  global timer
  timer += 1
  if timer == 60:
  seconds += 1
  timer = 0
  if keyboard.left:
    player.x -= 5
    # center of rot'n is the anchor point
  elif keyboard.right:
    player.x += 5
    player.angle = 0
  for i in reversed(range(len(fireballs))):
    fireballs[i].y += fireballs[i].vy
    if fireballs[i].y <= 0:
      del(fireballs[i])

def on_key_down(key):
  if key == keys.SPACE :
      launch()
def launch():
  fireball = Actor('fireballs')
  fireball.vy =-3
  fireball.pos =(player.x,player.y)
  fireballs.append(fireball)


def draw():
  screen.clear()
  screen.blit('jungle', (0, 0))
  player.draw()
  for x in fireballs:
    x.draw()

pgzrun.go()