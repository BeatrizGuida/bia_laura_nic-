import pygame
from grid import Grid
import sys

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

#definir alguns valores na grid para teste
game_grid.grid[0][0]= 1
game_grid.grid[3][5]= 4
game_grid.grid[17][8]= 7


game_grid.print_grid()

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

    pygame.display.update()
    relogio.tick(60)