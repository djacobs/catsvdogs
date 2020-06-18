from GameEngine import *
import sys, tty
import colorama
from colorama import Fore, Back, Style
from blessings import Terminal
import random
import time


def dice(n):
  return random.randint(1,n)


mandorlian = Dog("hot or cold")
god = Cat("run, run")

mandorlian.speed = dice(4)+1
mandorlian.strength = dice(10)+3
mandorlian.hp = dice(6)+1

god.speed = dice(2)+1
god.strength = dice(7)+3
god.hp = dice(10)

space = ''


def battle(p1,p2):
  print("let the bloodshed begin...")
  field_size=30
  p1.pos = p1.pos + field_size
  while (p2.hp > 0 and p1.hp > 0):
    print(p2.pos*space, p2.name, (p1.pos-p2.pos)*space, p1.name)
    time.sleep(2)
    p2.pos = p2.pos + p2.speed
    p1.pos = p1.pos - p1.speed
    if (p2.pos > p1.pos):
      while p2.hp > 0 and p1.hp > 0:
        print("there's a bloodfest!")
        p1.hp = p1.hp - p2.strength
        p2.hp = p2.hp - p1.strength
        p1.health()
        p2.health()

print("mandorlian: time to die.")
time.sleep(2)
print("god: you beat god? no no.")
time.sleep(2)

battle(god, mandorlian)

# when god dies he comes back with some hp
if god.hp == 0 or god.hp <0:
  print("you realise i am god. I will rise again.")
  god.hp = 20
  print("time to go away from chucky cheese.")
  mandorlian.strength += 10      
  mandorlian.speed = 10
  battle(god, mandorlian)