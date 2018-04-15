from pygame import *
import math
import random
class Character(sprite.Sprite):
    #the character that you choose
    def __init__(self, health, attack, speed, character, width, height):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.character = character
        #char attack and health and character
        self.image = image.load(self.character)
        self.image = transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = width/2
        self.rect.y = height/2
        self.x = self.rect.x - 50
        self.y = self.rect.y - 50
        #position and creation of char
        self.currLvl = 1
        #level of character
        sprite.Sprite.__init__(self)
    
    def move(self, keyCode):
        step = 10
        if keyCode == 275:
            self.rect.x += (self.speed)
        if keyCode == 276:
            self.rect.x -= (self.speed)
        if keyCode == 273:
            self.rect.y -= (self.speed)
        if keyCode == 274:
            self.rect.y += (self.speed)
        #move char

class Enemy(sprite.Sprite):
    def __init__(self,health,attack,can, x, y):
        self.health = health
        self.attack = attack
        self.can = can
        self.image = image.load(can)
        self.image = transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(x/2,x)
        self.rect.y = random.randint(0,y)
        sprite.Sprite.__init__(self)