import pygame
from pygame import *

class Obstacle():
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite().__init__()
        self.x = 1300
        self.y = 470
        self.image = pygame.image.load('img/stone.png')
        self.speed = 2
        self.rect = self.image.get_rect()
        self.speed_increase = 0.05