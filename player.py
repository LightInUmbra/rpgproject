import pygame

class Person(pygame.sprite.Sprite):
    def __init__(self, name, x, y, index=0):
        super(Person, self).__init__()
        self.name = name
        self.x = x
        self.y = y