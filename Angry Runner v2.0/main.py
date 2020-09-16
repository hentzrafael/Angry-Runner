import pygame,random
from pygame.locals import *
from pygame import *
from personagem import Person
from obstaculo import Obstacle
pygame.init()

class App:
    def __init__(self):
        self.personagem = Person()
        self.obstaculo = Obstacle('img/pig.png',470)
        self.air_obstacle = Obstacle('img/yellow.png',400)
        self.set_icon()
        self.set_clock()
        self.set_speed()
        self.init_display()
        self.add_title('Angry Runner')
        self.create_rects()
        self.gravity()
        self.load_images()
        self.x1 = 0
        self.x2 = 1280
        self.WHITE = (255,255,255)
        self.start_game = False
        self.first_time = True
        self.colidiu = False
        self.perdeu = False
        self.colisionList = [self.person_rect]
        self.pontuacao = 0
        self.joga()

#----------------------BASES---------------------------
    #Cria o relogio
    def set_clock(self):
        self.clock = pygame.time.Clock()
    
    #Iniciar o display
    def init_display(self):
        WIDTH = 1280
        HEIGHT = 720
        self.display = pygame.display.set_mode((WIDTH,HEIGHT))

    #Adiciona título na janela
    def add_title(self, text:str):
        self.title = pygame.display.set_caption(text)
    
    #Colocar o ícone no display
    def set_icon(self):
        pygame.display.set_icon(pygame.image.load('img/angry_icon.png'))

    #Procura o evento de fechamento do display
    def quit_display(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
     
    #Atualiza a tela
    def update(self):
        pygame.display.update()

    #Gera e coloca texto na tela
    def gera_texto(self,texto,tamanho,x,y):
        pygame.font.init()
        base = pygame.font.SysFont('arial',tamanho)
        surface = base.render(texto,1,(255,255,255))
        self.display.blit(surface,[x,y])


#------------------------------RECTS------------------------------------
   
    #Criador de rects
    def rect_generator(self,objeto,width,height):
        return pygame.Rect(objeto.x,objeto.y,width,height)

    #Cria os rects para colisao
    def create_rects(self):
        self.obstacle_rect = self.rect_generator(self.obstaculo,60,80)
        self.person_rect = self.rect_generator(self.personagem,80,120)
        self.air_rect = self.rect_generator(self.air_obstacle,50,50)

#----------------------------SOUNDS-------------------------------------
   
    #Carrega o som
    def load_sound(self,sound_path):
        pygame.mixer.init()
        sound = pygame.mixer_music.load(sound_path)
        return sound
    
    #Executa o som que foi carregado
    def execute_sound(self):
        pygame.mixer_music.play()

    #Coloca o som da moeda
    def coin_sound(self):
        self.load_sound('sounds/smb_coin.wav')
        self.execute_sound()
    
    #Coloca o som de gameover
    def over_sound(self):
        self.load_sound('sounds/smb_gameover.wav')
        self.execute_sound()

    #Coloca o som principal
    def main_sound(self):
        self.load_sound('sounds/main_music.mp3')
        self.execute_sound()

#-------------------------------PHYSIS----------------------------------
    #Define a constante gravitacional
    def gravity(self):
        self.GRAVIDADE = 10

    #Define a velocidade
    def set_speed(self):
        self.speed = 15
        self.speed_increase = 0.2
        self.MAX_SPEED = 70
    
    #Define a gravidade
    def cai(self):
        if self.personagem.y < 455:
            self.personagem.y += self.GRAVIDADE

#-------------------------------OBSTACLES-------------------------------------
    
    #Gera número para escolha de obstaculo
    def random_n(self):
        self.selected_obstacle = random.randint(0,1)

    #Reseta a posição dos obstaculos
    def reset_pos(self,objeto):
        objeto.x = 1300
    
    #Atualiza a posição do obstáculo
    def update_rect(self):
        self.air_rect = pygame.Rect(self.air_obstacle.x,self.air_obstacle.y, 50,50)
        self.obstacle_rect = pygame.Rect(self.obstaculo.x,self.obstaculo.y, 60,75)
        self.person_rect = pygame.Rect(self.personagem.x,self.personagem.y, 80,120)
        self.display.blit(self.obstaculo.image,[self.obstaculo.x,self.obstaculo.y])
        self.display.blit(self.air_obstacle.image,[self.air_obstacle.x,self.air_obstacle.y])
    
    #Move o obstaculo
    def move_obstacle(self,objeto):
        objeto.rect.move_ip(objeto.speed,0)
        if objeto.speed < self.MAX_SPEED:
            self.obstaculo.speed += self.obstaculo.speed_increase
            self.air_obstacle.speed += self.air_obstacle.speed_increase            
        objeto.x -= objeto.speed
        if objeto.x < -80:
            self.pontuacao += 1
            self.coin_sound() 

#---------------------------------MEDIA---------------------------------------------
   
    #Carrega as imagens necessárias
    def load_images(self):
        self.background_image = pygame.image.load('img/background.jpg')
        self.start_background = pygame.image.load('img/angryRunnerCapa.jpg')

    #Coloca os backgrounds na tela  
    def update_back(self):
        self.display.blit(self.background_image,[self.x1,0])
        self.display.blit(self.background_image,[self.x2,0])

    #Move as imagens de fundo
    def move_back(self):
        if self.speed < self.MAX_SPEED:
            self.speed += self.speed_increase
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 < -1279:
            self.x1 = 1280
        if self.x2 < -1279:
            self.x2 = 1280

#---------------------------------EVENTS------------------------------------
   
    #Desabilita a tecla espaço
    def disable_keys(self):
        pygame.event.set_blocked(pygame.KEYDOWN)  
    
    #Verifica se houve colisão
    def colisao(self):
        if  self.obstacle_rect.collidelist(self.colisionList) >= 0 and self.personagem.y > 350:
            self.perdeu = True
            self.colidiu = True
        elif self.air_obstacle.x < self.personagem.x and  self.personagem.y < 420:
            self.perdeu = True
            self.colidiu = True


#----------------------------PERSONAGEM---------------------------------------
   
    #Coloca o personagem
    def update_person(self):
        self.display.blit(self.personagem.image,[self.personagem.x,self.personagem.y])

    #Pega o pulo do personagem
    def captura_pulo(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_UP]==1 or teclas[K_SPACE]==1:
            return True    
        return False
    
    #Executa o pulo
    def pula(self):
        if self.personagem.y < 455:
            self.disable_keys()
        elif self.captura_pulo() and self.personagem.y > 280:
            self.personagem.y -= 200

#-------------------------------SCREENS-----------------------------------
    
    #Configuração da tela inicial
    def start_screen(self):
        self.display.blit(self.start_background,[0,0])
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]==1 or teclas[K_UP]==1:
            self.start_game = True

    #Configuração da tela de restart
    def restart_screen(self):
        if self.first_time:
            self.over_sound()
            self.first_time = False
        self.display.fill((0,0,0))
        self.gera_texto('Game Over Boy',50,500,300)
        tela_over = pygame.image.load('img/game_over.jpg')
        self.display.blit(tela_over,[0,0])
        self.gera_texto('Press space or up to restart',30,500,500)
        self.gera_texto('Você fez '+ str(self.pontuacao)+' ponto(s)',30,520,600)
        self.update()
            
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]==1 or teclas[K_UP]==1:
            pygame.mixer_music.stop()
            self.reset()

#----------------------------RESET-----------------------------------------
    
    #Reseta as configurações necessárias
    def reset(self):
            self.first_time = True
            self.colidiu = False
            self.obstaculo.x = 1300
            self.air_obstacle.x = 1300
            self.air_obstacle.speed_increase = 0.2
            self.obstaculo.speed_increase = 0.2
            self.perdeu = False          
            self.pontuacao = 0  
            self.speed_increase = 0.2
            self.speed = 15
            self.x1 = 0
            self.x2 = 1280
            self.obstaculo.speed = 15
            self.air_obstacle.speed = 15


#----------------------------GAME-----------------------------------
    
    #Método com o loop do jogo
    def joga(self):
        first = True
        while True:
            if first:
                self.random_n()
            if self.start_game == False and self.perdeu == False:
                self.start_screen()
            elif self.start_game == True and self.perdeu== True:
                self.restart_screen()
            elif self.start_game:
                self.update_back()
                self.update_person()
                self.update_rect()
                if self.selected_obstacle==1 and (self.obstaculo.x == 1300 ):
                    self.move_obstacle(self.air_obstacle)
                elif self.selected_obstacle==0 and (self.air_obstacle.x == 1300):
                    self.move_obstacle(self.obstaculo)
                self.move_back()
                self.pula()
                self.cai()
                self.gera_texto(str(self.pontuacao),50,630,40)
                self.colisao()
            self.quit_display()
            self.update()
            first = False
            if self.selected_obstacle==1 and self.air_obstacle.x < -80:
                self.reset_pos(self.air_obstacle)
                first = True
            elif self.selected_obstacle==0 and self.obstaculo.x < -80:
                self.reset_pos(self.obstaculo)
                first = True
            self.tick = self.clock.tick(30)

App()