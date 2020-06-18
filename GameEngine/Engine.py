#!/usr/bin/python3


# constants

# classes
class Player:
  def __init__(self):
    # Print this message when the class starts
    print("A player appears")
    self.level = 0

  

class Animal:
  def __init__(self):
    print("an animal is born...")

  def health(self):
    print(self.name, "has", self.hp, "hp left.")
  
  def sheet(self):
    print ("speed is ", self.speed)
    print ("strength is", self.strength)
    print ("hp is", self.hp)
    
class Cat(Animal):
  def __init__(self, name):
    # Print this message when the class starts
    print("A cat appears, meow")
    self.name = name
    self.speed = 2
    self.strength = 1
    self.hp = 8
    self.pos = 0


class Dog(Animal):
  def __init__(self, name):
    # Print this message when the class starts
    print("A dog appears, woof")
    self.name = name
    self.speed = 1
    self.strength = 2
    self.hp = 10
    self.pos = 0

    
    
    
    
    
    
    
    
class Boss:
  def __init__(self):
    # Print this message when the class starts
    print("A boss appears")
    
    

class Base:
  def __init__(self):
    # Print this message when the class starts
    print("A base appears")

    
class Attack:
  def __init__(self, name, damage, animation, rechargetime, duration, range, power):
    # Print this message when the class starts
    print("A creature appears")
    self.name = name
    self.damage = damage
    self.animation = animation
    self.rechargetime = rechargetime
    self.duration = duration
    self.range = range
    self.power = power

    
    
class Attacker:
  def __init__(self, name, unit, type, hp, speed, hitbox, minxp):
    self.name = name
    
    # name this later
    self.unit = unit
    
    # type can be cat or dog
    self.type = type
    
    # only a player with this xp can use this attacker
    self.xp = 0
    self.hp = hp
    self.speed = speed 
    self.minxp = minxp    
    self.hitbox = hitbox

    # Define rules
    # we want to make sure we can return an error if the stats are too high.



    
  def upgrade(self, name, ability, upgrade):
    self.name = name
    self.ability = ability
    self.upgrade = upgrade
    
  def addAttacks(self, attack):
    self.attack = attack
    
    
class Card:
  def __init__(self, xp, picture, effect, description, food):
    name.xp = xp
    name.picture = picture
    name.effect = effect
    name.description = description
    name.food = food
    # Print this message when the class starts
    print("A card appears")
    
    
class Mission:
  def __init__(self, name, description, reward, unit):
    self.name = name
    self.description = description
    self.reward = reward
    self.unit = unit
    # Print this message when the class starts
    print("A mission appears")
    
    
class Hitbox:
  def __init__(self, shape):
    self.shape. shape
  
class Effect: 
  def __init__(self):
    print("An effect?")