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

#criar um evento sempre que a posição do bloco atual mudar
GAME_TEMP = pygame.USEREVENT 
pygame.time.set_timer(GAME_TEMP, 200)

#loop principal do jogo
while True:
    #verifica os eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_LEFT and game.game_over == False:
                game.move_esquerda()
            if eventos.key == pygame.K_RIGHT and game.game_over == False:
                game.move_direita()
            if eventos.key == pygame.K_DOWN and game.game_over == False:
                game.move_baixo()
            if eventos.key == pygame.K_UP and game.game_over == False:
                game.rotaciona()
        if eventos.type == GAME_TEMP and game.game_over == False: #se o jogo não acabou, move o bloco para baixo
            game.move_baixo()


    #pega todas as alterações feitas e desenha uma imagem nova
    tela.fill(preto)
    game.draw(tela)


    pygame.display.update()
    relogio.tick(60)