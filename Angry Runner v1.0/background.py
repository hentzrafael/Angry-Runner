class Background:
    def __init__(self,imagem,x,y):
        self.__image = imagem
        self.x = x
        self.y = y
        self.__HEIGHT = 720 
        self.__WIDTH = 1280

    def move_left(self,velocidade):
        self.x -= velocidade
