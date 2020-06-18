from GameEngine import *
import sys, tty
import colorama
from colorama import Fore, Back, Style
from blessings import Terminal

import random
import time
#one baby yoda kills multiple enemeys
def dice(n):
  return random.randint(1,n)

baby_yoda = Cat(" Baby yoda")#yeet so fat cats are cool so fat cats are cool this eli saying fat cats are cool
woof = Dog("🐶 Woof")
a_god = Dog("🥋 a usless peice of trash")

baby_yoda.speed = dice(1)  
baby_yoda.strength = dice(10) + 20
baby_yoda.hp = dice(20) + 10

a_god.speed = dice(1)
a_god.strength = dice(1)
a_god.strength = dice(1)

woof.speed = dice(1) + 1
woof.strength = dice(4) + 1
woof.hp = dice(10) + 1  


baby_yoda.sheet()
a_god.sheet()

space=' '

def battle(p1,p2):
  print("let's begin...")
  field_size=30
  p1.pos = p1.pos + field_size
  while (p2.hp > 0 and p1.hp > 0):
    print(p2.pos*space, p2.name, (p1.pos-p2.pos)*space, p1.name)
    time.sleep(2)
    p2.pos = p2.pos + p2.speed
    p1.pos = p1.pos - p1.speed
    if (p2.pos > p1.pos):
      while p2.hp > 0 and p1.hp > 0:
        print("there's a battle!")
        p1.hp = p1.hp - p2.strength
        p2.hp = p2.hp - p1.strength
        p1.health()
        p2.health()
battle(baby_yoda, a_god)

    