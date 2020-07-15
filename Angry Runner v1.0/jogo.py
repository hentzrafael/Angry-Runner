import pygame
from pygame import *
class Jogo:
    def __init__(self):
        self.tela_inicial = True
        self.iniciado = False
        self.WHITE = (255,255,255)
    
    def limpa_tela(self,display):
        display.fill(self.WHITE)