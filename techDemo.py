from pygame import *
from PyGameGame import PygameGame
import math
from Characters import Character, Enemy
# from Characters import Enemy
#PygameGame framework created by Lukas Peraza


class Background(sprite.Sprite):
    #creates the background for the field of play
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = image.load("landscape.jpg")
        self.image = transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        sprite.Sprite.__init__(self)

class Bullet(sprite.Sprite):
    #defines a bullet
    def __init__(self, x, y, angle, color):
        self.image = image.load(color)
        self.image = transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.angle = angle
        self.rect.x = x
        self.rect.y = y
        self.velocity = 11
        sprite.Sprite.__init__(self)
        
    def move(self):
        self.rect.x += math.cos(math.radians(self.angle))*self.velocity
        self.rect.y += math.sin(math.radians(self.angle))*self.velocity
    
    def check(self, width, height):
        #returns True if bullet off the screen
        if self.rect.x + 10 > width or self.rect.x - 10 < 0 or self.rect.y - 10 < 0 or self.rect.y > height:
            return True
        return False
            
            
class DirectionArrow(sprite.Sprite):
    #shows direction that character faces
    def __init__(self, distance, x, y):
        self.distance = distance
        self.image = image.load("arrow.jpg")
        self.image = transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0
        self.distance = 10
        sprite.Sprite.__init__(self)
    
    def move(self, keyCode):
        if keyCode == 113:
            self.angle -= self.distance
            self.rect.x += math.cos(math.radians(self.angle))*self.distance
            self.rect.y += math.sin(math.radians(self.angle))*self.distance
        if keyCode == 101:
            self.angle += self.distance
            self.rect.x += math.cos(math.radians(self.angle))*self.distance
            self.rect.y += math.sin(math.radians(self.angle))*self.distance
        #move char and rotate the direction it faces
        if keyCode == 100:
            self.angle = 0
        if keyCode == 97:
            self.angle = 180
        if keyCode == 119:
            self.angle = 270
        if keyCode == 115:
            self.angle = 90
        #quick select a direction
        self.rect.x += math.cos(math.radians(self.angle))*self.distance
        self.rect.y += math.sin(math.radians(self.angle))*self.distance
        

class Game(PygameGame):
    def init(self):
        
        self.width = 250
        self.height = 250
        self.gameMode = "Play"
        self.back = Background(self.width, self.height)
        self.backGroup = sprite.Group(self.back)
        #initialize background
        self.choice = 1
        #character selection
        self.characters = [("A&W.png", "orangeBolt.png", "hero.png", "axolotl.jpg"),("Pepsiman.png", "blueBolt.png","axolotl.jpg", "hero.png"), ("Spot.png", "redBolt.png", "hero.png")]
        self.char = Character(10, 1, 10, self.characters[self.choice][0])
        #init character and direction arrow
        self.arrow = DirectionArrow(10, self.char.rect.x, self.char.rect.y)
        #position of direction arrow
        self.canGroup1 = sprite.Group()
        self.canGroup2 = sprite.Group()
        #all the enemy cans
        self.charGroup = sprite.Group(self.char)
        self.bulletGroup = sprite.Group()
        self.arrowGroup = sprite.Group(self.arrow)
        #creates sprite groups
        self.timer = 0
        
    
    def keyPressed(self, keyCode, modifier):
        self.char.move(keyCode)
        self.arrow.move(keyCode)
        if keyCode == 32:
            self.bulletGroup.add(Bullet(self.char.rect.x+50,self.char.rect.y+50,self.arrow.angle, self.characters[self.choice][1]))
        
    def timerFired(self, dt):
        self.timer += 1
        if self.timer %5 == 0:
            for bullet in self.bulletGroup:
                bullet.move()
                if bullet.check(self.width, self.height):
                    self.bulletGroup.remove(bullet)
                    #deletes bullet if off the screen
        if self.timer % 100 == 0:
            print(self.characters[1][3])
            self.canGroup1.add(Enemy(2,1,self.characters[1][3], self.width, self.height))
            self.canGroup2.add(Enemy(2,1,self.characters[1][3], self.width, self.height))
            for can in self.canGroup1:
                if can.check(self.width, self.height):
                    self.canGroup1.remove(can)
            for can in self.canGroup2:
                if can.check(self.width, self.height):
                    self.canGroup2.remove(can)
                    #deletes can

    def redrawAll(self, screen):
        # if self.gameMode == "Start":
        #     
            
        if self.gameMode == "Play":
            self.backGroup.draw(screen)
            self.charGroup.draw(screen)
            self.arrowGroup.draw(screen)
            if len(self.bulletGroup) > 0:
                self.bulletGroup.draw(screen)
            if len(self.canGroup1) > 0 and len(self.canGroup2) > 0:
                self.canGroup1.draw(screen)
                self.canGroup2.draw(screen)
            #draws every bullet and can
        
Game(500,500).run()