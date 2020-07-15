import pygame
from pygame import *
from pygame.rect import *

class Person():
        def __init__(self):
                pygame.sprite.Sprite.__init__(pygame.sprite.Sprite)
                self.x = 40
                self.image = pygame.image.load('img/personagem.png')
                self.rect = self.image.get_rect()
                self.y = 455

    