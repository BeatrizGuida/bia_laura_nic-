import pygame, sys
from game import Game

#inicializa o pygame
pygame.init()
preto= (0, 0, 0)

#tamanho da tela
tela= pygame.display.set_mode((300, 600))
#nome do jogo
pygame.display.set_caption('Trix!')
# relogio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

game= Game()

#loop principal do jogo
while True:
    #verifica os eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_LEFT:
                game.move_esquerda()
            if eventos.key == pygame.K_RIGHT:
                game.move_direita()
            if eventos.key == pygame.K_DOWN:
                game.move_baixo()


    #pega todas as alterações feitas e desenha uma imagem nova
    tela.fill(preto)
    game.draw(tela)

    pygame.display.update()
    relogio.tick(60)