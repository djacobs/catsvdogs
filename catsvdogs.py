from GameEngine import *
import sys, tty
import colorama
from colorama import Fore, Back, Style
from blessings import Terminal

import random
import time

#import emoji

# First pseudo code, 
# the "stub" code, 
# the real code

# 4 8 15 16 23 42


#bloogle choogle moogle floogle fat cats are cool
# 1. First Pseudo code cats slap dog faces

# For my game (each of you can add and negotiate your own rules), I will have cats and dogs leaving their base and approach their
# opponent's bases

# cats are fast, but have only small claws

# dogs are slow, but have a loud bark

# when cats and dogs collide they battle 
  # we don't want it to be the same each time, so we should add some random-ness. 



# def is how we make a new command
def dice(n):
  return random.randint(1,n)


print(dice(6))


# now make the cat
meow = Cat("😺 Meow")#yeet so fat cats are cool so fat cats are cool this eli saying fat cats are cool
woof = Dog("🐶 Woof")

# see the default stats
#meow.sheet()
# baby_yoda.speed = dice(2)
#baby_yoda.strength = dice(10) + 10
# now let's make them random
meow.speed = dice(3) + 1
meow.strength = dice(3) + 1
meow.hp = dice(9) + 1     


# now let's make the dog

woof.speed = dice(1) + 1
woof.strength = dice(4) + 1
woof.hp = dice(10) + 1  

#no unfair advantages eli
meow.sheet()
woof.sheet()


# print(Back.BLUE + "Hello there")
# print(Style.RESET_ALL)
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

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

        
battle(meow, woof)



# unicode text color:
# https://www.instructables.com/id/Printing-Colored-Text-in-Python-Without-Any-Module/

# colorama
# https://pypi.org/project/colorama/

# blessings
# https://pypi.org/project/blessings/