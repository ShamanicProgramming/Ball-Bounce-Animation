import math
import pygame.image

class Ball():
    def __init__(self):

        self.image = pygame.image.load("Resources/Images/ball.gif")
        self.rect = self.image.get_rect()

        self.rect.center = 250,250
        self.bearing = math.pi*2/5
        self.speed = 5


    def hit(self, source):
        if source == "top" or source == "bottom":
            self.bearing = - self.bearing
        elif source == "left" or source == "right":
            self.bearing = math.pi - self.bearing
        self.rect.move(math.copysign(self.rect.width,self.bearing),0)


    def move(self):
        x, y = self.speed*math.cos(self.bearing), self.speed*math.sin(self.bearing)
        self.rect = self.rect.move(x, y)


    def check_collision(self,size, boxes):
        midtop = self.rect.midtop
        midleft = self.rect.midleft
        midbottom = self.rect.midbottom
        midright = self.rect.midright
        if midright[0] >= size[0]:
            self.hit("right")
        elif midleft[0] <= 0:
            self.hit("left")
        elif midbottom[1] >= size[1]:
            self.hit("bottom")
        elif midtop[1] <= 0:
            self.hit("top")
        else:
            i = 0
            for each in boxes:
                if each.rect.collidepoint(midright):
                    self.hit("right")
                    return i
                elif each.rect.collidepoint(midleft):
                    self.hit("left")
                    return i
                elif each.rect.collidepoint(midtop):
                    self.hit("top")
                    return i
                elif each.rect.collidepoint(midbottom):
                    self.hit("bottom")
                    return i
                i = i + 1
            return None