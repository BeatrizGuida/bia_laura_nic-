import pygame, sys
from grid import Grid
from blocks import *

#inicializa o pygame
pygame.init()
preto= (0, 0, 0)

#tamanho da tela
tela= pygame.display.set_mode((300, 600))
#nome do jogo
pygame.display.set_caption('Trix!')
# relogio para controlar a velocidade do jogo
relogio = pygame.time.Clock()


game_grid= Grid()

block= TBlock() 
block.movimento(5,3)


#loop principal do jogo
while True:
    #verifica os eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #pega todas as alterações feitas e desenha uma imagem nova
    tela.fill(preto)
    game_grid.draw(tela)
    block.draw(tela)

    pygame.display.update()
    relogio.tick(60)