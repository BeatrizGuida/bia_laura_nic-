import pygame, sys
from game import Game
from colors import Colors

#inicializa o pygame
pygame.init()

fonte_titulo= pygame.font.Font(None, 40)
pontuacao= fonte_titulo.render("Pontuação", True, Colors.branco)

pontuacao_rect= pygame.Rect(315, 55, 170, 60) 

#tamanho da tela
tela= pygame.display.set_mode((500, 620))
#nome do jogo
pygame.display.set_caption('Trix!')
# relogio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

game= Game()

#criar um evento sempre que a posição do bloco atual mudar
GAME_TEMP = pygame.USEREVENT
pygame.time.set_timer(GAME_TEMP, 200)

# Estados: "menu", "playing", "game_over"
estado = "menu"

# botões (serão reposicionados centralmente)
botao_start = pygame.Rect(0, 0, 180, 54)
botao_restart = pygame.Rect(0, 0, 180, 54)

# Fontes auxiliares (mantive um pouco da sua configuração visual)
fonte_sub = pygame.font.Font(None, 28)
fonte_botao = pygame.font.Font(None, 30)
fonte_info = pygame.font.Font(None, 20)


# Função para desenhar a tela inicial
def tela_inicial(surface):
    """Tela inicial centralizada"""
    surface.fill(Colors.roxo_neon)

    # título centralizado (um pouco no topo)
    title_surf = fonte_titulo.render("TRIX", True, Colors.branco)
    surface.blit(title_surf, title_surf.get_rect(center=(500 // 2, 160)))

    # instruções centralizadas
    instr = fonte_info.render("Use ← → ↓ para mover, ↑ para rotacionar", True, Colors.branco)
    surface.blit(instr, instr.get_rect(center=(500 // 2, 205)))

    # botão START centralizado
    botao_start.center = (500 // 2, 300)
    pygame.draw.rect(surface, Colors.verde_neon, botao_start, border_radius=10)
    start_surf = fonte_botao.render("START", True, Colors.preto)
    surface.blit(start_surf, start_surf.get_rect(center=botao_start.center))

    # dica de teclado centralizada
    dica = fonte_info.render("Pressione Enter ou clique em START", True, Colors.branco)
    surface.blit(dica, dica.get_rect(center=(500 // 2, 360)))


# Função para desenhar a tela de game over
def tela_game_over(surface):
    """Tela de game over centralizada"""
    surface.fill(Colors.roxo_neon)

    # título GAME OVER centralizado
    over_surf = fonte_titulo.render("GAME OVER", True, Colors.vermelho_neon)
    surface.blit(over_surf, over_surf.get_rect(center=(500 // 2, 160)))

    # botão RESTART centralizado
    botao_restart.center = (500 // 2, 300)
    pygame.draw.rect(surface, Colors.verde_neon, botao_restart, border_radius=10)
    restart_surf = fonte_botao.render("RESTART", True, Colors.preto)
    surface.blit(restart_surf, restart_surf.get_rect(center=botao_restart.center))

    # dica de teclado centralizada
    dica = fonte_info.render("Pressione Enter ou clique em RESTART", True, Colors.branco)
    surface.blit(dica, dica.get_rect(center=(500 // 2, 360)))




# tela jogo
def tela_jogo(surface):
    surface.fill(Colors.roxo_neon)
    
    surface.blit(pontuacao, (332, 20, 50, 50))
    pygame.draw.rect(surface, Colors.azul_claro, pontuacao_rect, 0, 10, )
    # desenha o jogo (sua função Game.draw já desenha a grid e o bloco)
    game.draw(surface)
    score_text = fonte_titulo.render(str(getattr(game, "score", 0)), True, Colors.branco)
    surface.blit(score_text, score_text.get_rect(center=pontuacao_rect.center))



#loop principal do jogo
while True:
    #verifica os eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if eventos.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
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
    tela.fill(Colors.roxo_neon)
    tela.blit(pontuacao, (332, 20, 50, 50))
    pygame.draw.rect(tela, Colors.azul_claro, pontuacao_rect, 0, 10, )
    game.draw(tela)



    pygame.display.update()
    relogio.tick(60)




