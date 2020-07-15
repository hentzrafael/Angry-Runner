import pygame,random
from pygame import *
from personagem import Personagem
from background import Background 
from jogo import Jogo
from obstaculo import Obstaculo 
"""Correções
O programa está dependendo do clique na barra de espaço para gerar e mostrar novos obstaculos e não está detectando corretamente a colisao
com o personagem
Na tela final deve aguardar pressionar a tecla de espaço e reiniciar o jogo, resetando todas as posições e variáveis
"""
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
DISPLAY_HEIGHT = 720
DISPLAY_WIDTH = 1280
GRAVIDADE_PERSONAGEM = 4

pygame.init()
tela_jogo = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('Angry Runner')

personagem_pula = False
personagem_principal = Personagem(80,100,200,450,'img/personagem.png')

mensagem_tela_inicial = 'Bem vindo ao Angry Runner'
mensagem_pressiona_barra_espaco = 'Aperte a barra de espaço para continuar'
pygame.font.init()
fonte_base_titulos = pygame.font.SysFont('arial',50)
mensagem_tela_inicial_surface = fonte_base_titulos.render(mensagem_tela_inicial,1,(0,0,0))
fonte_base_subtitulos = pygame.font.SysFont('arial',30)
mensagem_pressiona_barra_espaco_surface = fonte_base_subtitulos.render(mensagem_pressiona_barra_espaco,1,(0,0,0))

jogo = Jogo()
jogo.limpa_tela(tela_jogo)


background_image = pygame.image.load('img/background.jpg').convert()

background_primario = Background(background_image,0,0)
background_secundario = Background(background_image,1280,0)

pontuacao = 0

obstaculo = Obstaculo()
obstaculo_selecionado = obstaculo.obstaculo_aleatorio('img/flecha_obstaculo.png','img/stone.png')

tela_final = False

while True:
    #saída
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()


    if jogo.tela_inicial==False:
        pontuacao_surface = fonte_base_titulos.render(str(pontuacao),1,(0,0,0))
        if personagem_principal.colisao(obstaculo,obstaculo.aceleracao)==False:
            if obstaculo.obstaculo_x <= 0:
                pontuacao += 1
                obstaculo.obstaculo_x = 1400
                obstaculo_selecionado = obstaculo.obstaculo_aleatorio('img/flecha_obstaculo.png','img/stone.png') #Se não houve colisao
        else:
            tela_final = True

        tela_jogo.blit(background_image,[background_primario.x,background_primario.y])
        tela_jogo.blit(background_image,[background_secundario.x,background_secundario.y])
        tela_jogo.blit(pontuacao_surface,[500,100])
        tela_jogo.blit(obstaculo_selecionado,[obstaculo.obstaculo_x,obstaculo.obstaculo_y])
        obstaculo.move_obstaculo(0.0005)
        background_primario.move_left(1)
        background_secundario.move_left(1)
        personagem_principal.mostra_na_tela(tela_jogo,personagem_principal.x_personagem,personagem_principal.y_personagem)
    

        if background_primario.x + 1280 <= 0:
            background_primario.x = 1280
        elif background_secundario.x + 1280 <= 0:
            background_secundario.x = 1280
        
        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[K_SPACE]==1 or teclas_pressionadas[K_UP]==1:
            personagem_pula = True

        personagem_principal.pula_personagem(personagem_pula,10,300)

        if personagem_principal.y_personagem < 450:
            personagem_principal.y_personagem += GRAVIDADE_PERSONAGEM
        
        personagem_pula = False

    
    elif tela_final ==True:
        jogo.limpa_tela(tela_jogo)
        pontuacao_final_surface = fonte_base_titulos.render('Sua pontuacao foi de {}'.format(str(pontuacao)),1,(0,0,0))
        tela_jogo.blit(pontuacao_final_surface,[400,100])
    
    elif jogo.tela_inicial:
        tela_jogo.blit(mensagem_tela_inicial_surface,[350,100])
        tela_jogo.blit(mensagem_pressiona_barra_espaco_surface,[420,400])

        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[K_SPACE]==1:
            jogo.tela_inicial = False
    
    pygame.display.flip()

    