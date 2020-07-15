import pygame
from pygame.locals import *
from pygame import *
from personagem import Person
from obstaculo import Obstacle
pygame.init()

class App:
    def __init__(self):
        self._WIDTH = 1280
        self._HEIGHT = 720
        self.background_image = pygame.image.load('img/background.jpg')
        self.display = pygame.display.set_mode((self._WIDTH,self._HEIGHT),flags=pygame.RESIZABLE)
        self.x1 = 0
        self.x2 = 1280
        self.speed = 2
        self.WHITE = (255,255,255)
        self.speed_increase = 0.05
        self.personagem = Person()
        self.obstaculo = Obstacle()
        self.start_game = False
        self.clock = pygame.time.Clock()
        self.colidiu = False
        self.perdeu = False
        self.obstacle_rect = pygame.Rect(self.obstaculo.x,self.obstaculo.y, 60,80)
        self.person_rect = pygame.Rect(self.personagem.x,self.personagem.y, 80,120)
        self.colisionList = [self.person_rect]
        self.title = pygame.display.set_caption('Angry Runner v1.0')
        self.start_background = pygame.image.load('img/angry_start.jpg')
        self.gravidade = 15
        self.pontuacao = 0
        self.set_icon()
        self.joga()

    def set_icon(self):
        pygame.display.set_icon(pygame.image.load('img/angry_icon.png'))

    def quit_display(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
    
    def update(self):
        pygame.display.flip()

    def update_back(self):
        self.display.blit(self.background_image,[self.x1,0])
        self.display.blit(self.background_image,[self.x2,0])

    def move_back(self):
        self.speed += self.speed_increase
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 < -1279:
            self.x1 = 1280
        if self.x2 < -1279:
            self.x2 = 1280

    def joga(self):
        while True:
            self.tick = self.clock.tick(30)
            if self.start_game == False and self.perdeu == False:
                self.start_screen()
            elif self.start_game == True and self.perdeu== True:
                self.restart_screen()
            elif self.start_game:
                self.update_back()
                self.update_person()
                self.update_obstacle()
                self.move_obstacle()
                self.move_back()
                self.pula()
                self.cai()
                self.pontuacao_aumenta()
                self.gera_texto(str(self.pontuacao),50,630,40)
                self.colisao()
            self.quit_display()
            self.update()

    def update_person(self):
        self.display.blit(self.personagem.image,[self.personagem.x,self.personagem.y])

    def captura_pulo(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_UP]==1 or teclas[K_SPACE]==1:
            return True    
        return False

    def start_screen(self):
        self.display.blit(self.start_background,[0,0])
        self.gera_texto('Angry Runner', 80,420,90)
        self.gera_texto('Pressione espaço para iniciar!',40,400,540)
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]==1:
            self.start_game = True

    def gera_texto(self,texto,tamanho,x,y):
        pygame.font.init()
        base = pygame.font.SysFont('arial',tamanho)
        surface = base.render(texto,1,(255,255,255))
        self.display.blit(surface,[x,y])

    def cai(self):
        if self.personagem.y < 455:
            self.personagem.y += self.gravidade

    def pula(self):
        if self.captura_pulo() and self.personagem.y > 200:
            self.personagem.y -= 40

    def update_obstacle(self):
        self.obstacle_rect = pygame.Rect(self.obstaculo.x,self.obstaculo.y, 60,80)
        self.person_rect = pygame.Rect(self.personagem.x,self.personagem.y, 80,120)
        self.display.blit(self.obstaculo.image,[self.obstaculo.x,self.obstaculo.y])

    def move_obstacle(self):
        self.obstaculo.rect.move_ip(self.obstaculo.speed,0)
        self.obstaculo.speed += self.obstaculo.speed_increase
        self.obstaculo.x -= self.obstaculo.speed
        if self.obstaculo.x < -40:
            self.obstaculo.x = 1300

    def colisao(self):
        if  self.obstacle_rect.collidelist(self.colisionList) >= 0 and self.personagem.y > 350:
            self.perdeu = True
            self.colidiu = True

    def restart_screen(self):
        if self.colidiu:
            self.display.fill((0,0,0))
            self.gera_texto('Game Over Boy',50,500,300)
            self.gera_texto('Press space to restart',30,500,450)
            self.gera_texto('Você fez '+ str(self.pontuacao)+' pontos',30,500,600)
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]==1:
            self.colidiu = False
            self.obstaculo.x = 1300
            self.obstaculo.speed_increase = 0.05
            self.perdeu = False          
            self.pontuacao = 0  
            self.speed_increase = 0.05
            self.speed = 2
            self.obstaculo.speed = 2

    def pontuacao_aumenta(self):
        if self.colidiu ==False and self.obstaculo.x < self.personagem.x:
            self.pontuacao += 1

App()