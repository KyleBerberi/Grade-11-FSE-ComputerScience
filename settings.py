import pgzrun
from pgzero.actor import Actor
from random import randint
from pgzero.keyboard import keyboard
import random
from subprocess import call

WIDTH = 800
HEIGHT = 554
player=Actor('mc.png')
player.pos = (WIDTH/2,HEIGHT-50)

fireballs=[]

def update():
  if Keyboard.left:
    player.x -=5
    player.angle = 180
  elif keyboard.right:
    player.x =5
    player.angle = 0
for i in reversed(range(len(fireballs))):
  fireballs[i].y += fireballs[i].vy
  if fireballs[i].y <= 0:
    del(fireballs[i])

def on_key_down(key):
  if key==key.space:
    launch()
def launch():
  fireballs = Actor('fireballs')
  fireballs.vy =-3
  fireballs.pos =(player.x,player.y)
  fireballs.append(fireballs)

def draw():
  screen.clear()
  player.draw()
  for x in fireballs:
    x.draw()