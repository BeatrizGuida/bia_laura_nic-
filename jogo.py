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
    dica = fonte_info.render("Clique em START", True, Colors.branco)
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
    dica = fonte_info.render("Clique em RESTART", True, Colors.branco)
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



# loop principal
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # cliques do mouse para START / REINICIAR
        if eventos.type == pygame.MOUSEBUTTONDOWN and eventos.button == 1:
            mouse_pos = eventos.pos
            if estado == "menu":
                if botao_start.collidepoint(mouse_pos):
                    estado = "playing"
                    game.reset()
            elif estado == "game_over":
                if botao_restart.collidepoint(mouse_pos):
                    estado = "playing"
                    game.reset()

        # teclado
        if eventos.type == pygame.KEYDOWN:
            if estado == "menu":
                # Enter inicia o jogo
                if eventos.key == pygame.K_RETURN or eventos.key == pygame.K_KP_ENTER:
                    estado = "playing"
                    game.reset()

            elif estado == "playing":
                # se o jogo acabou e o jogador apertar Enter - reinicia (comportamento opcional)
                if eventos.key == pygame.K_RETURN and game.game_over:
                    game.game_over = False
                    game.reset()

                # controles do jogo (somente se não for game over)
                if not game.game_over:
                    if eventos.key == pygame.K_LEFT:
                        game.move_esquerda()
                    if eventos.key == pygame.K_RIGHT:
                        game.move_direita()
                    if eventos.key == pygame.K_DOWN:
                        game.move_baixo()
                    if eventos.key == pygame.K_UP:
                        game.rotaciona()

            elif estado == "game_over":
                # Enter reinicia e volta ao estado de playing
                if eventos.key == pygame.K_RETURN or eventos.key == pygame.K_KP_ENTER:
                    estado = "playing"
                    game.reset()

        # queda automática do bloco
        if eventos.type == GAME_TEMP and estado == "playing" and not game.game_over:
            game.move_baixo()

    # desenho com base no estado atual
    if estado == "menu":
        tela_inicial(tela)
    elif estado == "playing":
        tela_game_over(tela)
        # se o jogo ficar com game_over True durante a execução, trocamos o estado
        if game.game_over:
            estado = "game_over"
    elif estado == "game_over":
        tela_jogo(tela, getattr(game, "score", 0))

    pygame.display.update()
    relogio.tick(60)


# #loop principal do jogo
# while True:
#     #verifica os eventos
#     for eventos in pygame.event.get():
#         if eventos.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()


#         if eventos.type == pygame.KEYDOWN:
#             if game.game_over == True:
#                 game.game_over = False
#                 game.reset()
#             if eventos.key == pygame.K_LEFT and game.game_over == False:
#                 game.move_esquerda()
#             if eventos.key == pygame.K_RIGHT and game.game_over == False:
#                 game.move_direita()
#             if eventos.key == pygame.K_DOWN and game.game_over == False:
#                 game.move_baixo()
#             if eventos.key == pygame.K_UP and game.game_over == False:
#                 game.rotaciona()
#         if eventos.type == GAME_TEMP and game.game_over == False: #se o jogo não acabou, move o bloco para baixo
#             game.move_baixo()


#     #pega todas as alterações feitas e desenha uma imagem nova
#     tela.fill(Colors.roxo_neon)
#     tela.blit(pontuacao, (332, 20, 50, 50))
#     pygame.draw.rect(tela, Colors.azul_claro, pontuacao_rect, 0, 10, )
#     game.draw(tela)



#     pygame.display.update()
#     relogio.tick(60)




import pygame, sys
from game import Game
from colors import Colors

# inicializa o pygame
pygame.init()

# fontes e UI
fonte_titulo = pygame.font.Font(None, 40)
texto_pontuacao = fonte_titulo.render("Pontuação", True, Colors.branco)

retangulo_pontuacao = pygame.Rect(315, 55, 170, 60)

# tamanho da tela
tela = pygame.display.set_mode((500, 620))
pygame.display.set_caption('Trix!')

# relógio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

# instância do jogo
jogo = Game()

# evento de queda automática
EVENTO_QUEDA = pygame.USEREVENT
pygame.time.set_timer(EVENTO_QUEDA, 200)

# Estados possíveis
estado = "menu"  # menu, jogando, game_over

# botões
botao_iniciar = pygame.Rect(0, 0, 180, 54)
botao_reiniciar = pygame.Rect(0, 0, 180, 54)

# fontes auxiliares
fonte_subtitulo = pygame.font.Font(None, 28)
fonte_botao = pygame.font.Font(None, 30)
fonte_info = pygame.font.Font(None, 20)

# área do próximo bloco
retangulo_proximo = pygame.Rect(315, 140, 170, 120)


# Função para desenhar o próximo bloco (miniatura)
def desenhar_proximo_bloco(superficie, bloco, rect):
    if bloco is None:
        return

    cores = Colors.cores_celulas()
    tamanho_celula = 18  # tamanho menor para preview

    pecas = bloco.cells.get(bloco.rotation_state, list(bloco.cells.values())[0])

    colunas = [p.coluna for p in pecas]
    linhas = [p.linha for p in pecas]
    min_c, max_c = min(colunas), max(colunas)
    min_l, max_l = min(linhas), max(linhas)

    largura_px = (max_c - min_c + 1) * tamanho_celula
    altura_px = (max_l - min_l + 1) * tamanho_celula

    inicio_x = rect.x + (rect.width - largura_px) // 2
    inicio_y = rect.y + (rect.height - altura_px) // 2

    for p in pecas:
        rx = inicio_x + (p.coluna - min_c) * tamanho_celula
        ry = inicio_y + (p.linha - min_l) * tamanho_celula
        r = pygame.Rect(rx + 1, ry + 1, tamanho_celula - 2, tamanho_celula - 2)
        cor = cores[bloco.id] if 0 <= bloco.id < len(cores) else Colors.cinza_escuro
        pygame.draw.rect(superficie, cor, r)


# Tela inicial
def tela_inicial(superficie):
    superficie.fill(Colors.roxo_neon)

    titulo = fonte_titulo.render("TRIX", True, Colors.branco)
    superficie.blit(titulo, titulo.get_rect(center=(500 // 2, 160)))

    instrucoes = fonte_info.render("Use ← → ↓ para mover, ↑ para girar a peça", True, Colors.branco)
    superficie.blit(instrucoes, instrucoes.get_rect(center=(500 // 2, 205)))

    botao_iniciar.center = (500 // 2, 300)
    pygame.draw.rect(superficie, Colors.verde_neon, botao_iniciar, border_radius=10)
    texto_botao = fonte_botao.render("INICIAR", True, Colors.preto)
    superficie.blit(texto_botao, texto_botao.get_rect(center=botao_iniciar.center))

    dica = fonte_info.render("Pressione Enter ou clique em INICIAR", True, Colors.branco)
    superficie.blit(dica, dica.get_rect(center=(500 // 2, 360)))


# Tela de Game Over
def tela_game_over(superficie, pontuacao=None):
    superficie.fill(Colors.roxo_neon)

    titulo = fonte_titulo.render("FIM DE JOGO", True, Colors.vermelho_neon)
    superficie.blit(titulo, titulo.get_rect(center=(500 // 2, 160)))

    if pontuacao is not None:
        pontuacao_texto = fonte_subtitulo.render(f"Pontuação: {pontuacao}", True, Colors.branco)
        superficie.blit(pontuacao_texto, pontuacao_texto.get_rect(center=(500 // 2, 210)))

    botao_reiniciar.center = (500 // 2, 300)
    pygame.draw.rect(superficie, Colors.verde_neon, botao_reiniciar, border_radius=10)
    texto_botao = fonte_botao.render("REINICIAR", True, Colors.preto)
    superficie.blit(texto_botao, texto_botao.get_rect(center=botao_reiniciar.center))

    dica = fonte_info.render("Pressione Enter ou clique em REINICIAR", True, Colors.branco)
    superficie.blit(dica, dica.get_rect(center=(500 // 2, 360)))


# Tela principal do jogo
def tela_jogo(superficie):
    superficie.fill(Colors.roxo_neon)

    superficie.blit(texto_pontuacao, (332, 20))
    pygame.draw.rect(superficie, Colors.azul_claro, retangulo_pontuacao, border_radius=10)

    texto_score = fonte_titulo.render(str(getattr(jogo, "score", 0)), True, Colors.branco)
    superficie.blit(texto_score, texto_score.get_rect(center=retangulo_pontuacao.center))

    # desenha o tabuleiro e a peça atual
    jogo.draw(superficie)

    # próximo bloco
    pygame.draw.rect(superficie, Colors.azul_claro, retangulo_proximo, border_radius=10)
    texto_proximo = fonte_info.render("PRÓXIMO BLOCO", True, Colors.branco)
    superficie.blit(texto_proximo, (retangulo_proximo.x + 8, retangulo_proximo.y - 20))
    desenhar_proximo_bloco(superficie, jogo.next_block, retangulo_proximo)


# loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # cliques do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos = evento.pos
            if estado == "menu":
                if botao_iniciar.collidepoint(pos):
                    jogo.reset()
                    jogo.game_over = False
                    jogo.score = 0
                    estado = "jogando"
            elif estado == "game_over":
                if botao_reiniciar.collidepoint(pos):
                    jogo.reset()
                    jogo.game_over = False
                    jogo.score = 0
                    estado = "jogando"

        # teclado
        if evento.type == pygame.KEYDOWN:
            if estado == "menu":
                if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    jogo.reset()
                    jogo.game_over = False
                    jogo.score = 0
                    estado = "jogando"

            elif estado == "jogando":
                if evento.key == pygame.K_RETURN and jogo.game_over:
                    jogo.reset()
                    jogo.game_over = False
                    jogo.score = 0
                    estado = "jogando"

                if not jogo.game_over:
                    if evento.key == pygame.K_LEFT:
                        jogo.move_esquerda()
                    if evento.key == pygame.K_RIGHT:
                        jogo.move_direita()
                    if evento.key == pygame.K_DOWN:
                        jogo.move_baixo()
                    if evento.key == pygame.K_UP:
                        jogo.rotaciona()

            elif estado == "game_over":
                if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    jogo.reset()
                    jogo.game_over = False
                    jogo.score = 0
                    estado = "jogando"

        # evento de queda automática
        if evento.type == EVENTO_QUEDA and estado == "jogando" and not jogo.game_over:
            jogo.move_baixo()

    # desenho de acordo com o estado
    if estado == "menu":
        tela_inicial(tela)
    elif estado == "jogando":
        tela_jogo(tela)
        if jogo.game_over:
            estado = "game_over"
    elif estado == "game_over":
        tela_game_over(tela, getattr(jogo, "score", 0))

    pygame.display.update()
    relogio.tick(60)
