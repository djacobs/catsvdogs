from GameEngine import *
import sys, tty
import colorama
from colorama import Fore, Back, Style
from blessings import Terminal
import random
import time

#my level will tell you how to play,what cats you have,how to beat enemies and more.

Lev = Player()

#cats cat,big cat,mecha cat,malicious cat,doom cat,king catticus ruler of da cats.
#enemys dog,big dog,knight dog,blood raven(black),black knight mutt(black),king doggodoom duke of da dogs(relic)

cat = Cat("mew")
big_cat = Bigcat("meooow")
mecha_cat = Mechacat("M-E-E-O-O-W")
malice_cat = Malicecat("meowmeowmeow")
doom_cat = Doomcat("mEeeeeEeEeeEoooOoOooW")
king_catticus = Kingcatticus("meow peasant and tremble in fear")

dog = Dog("ruff")
big_dog = Bigdog("rooff")
knight_dog = Knightdog("ruffruffruff")
blood_raven = Bloodraven("caw caw caw")
black_mutt = Blackmutt("rwarrrrrrrrrrr")
duke_doggodoom = Doggodoom("ruff loudly and send a shiver down our foes spines")


blood_raven = Animal("Blood Raven")
blood_raven.hp(20,40)
blood_raven.strength(20,35)
blood_raven.speed(20,45)

 blood_raven.battle(king_catticus)














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