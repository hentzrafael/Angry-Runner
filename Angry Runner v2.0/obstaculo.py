import pygame
from pygame import *

class Obstacle():
    def __init__(self,image_path,y):
        super().__init__()
        pygame.sprite.Sprite().__init__()
        self.x = 1300
        self.y = y
        self.image = pygame.image.load(image_path)
        self.speed = 15
        self.rect = self.image.get_rect()
        self.speed_increase = 0.2