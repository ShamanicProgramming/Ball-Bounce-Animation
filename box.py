import pygame.image

class Box():
    def __init__(self,column,row):

        self.image = pygame.image.load("Resources/Images/box.gif")
        self.rect = self.image.get_rect()

        self.rect.center = (column*38,row*23)