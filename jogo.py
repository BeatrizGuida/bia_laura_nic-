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
pygame.time.set_timer(EVENTO_QUEDA, 200)  # a cada 200 ms

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
def desenhar_proximo_bloco(surface, bloco, rect):
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
        pygame.draw.rect(surface, cor, r)


# Tela inicial
def tela_inicial(surface):
    surface.fill(Colors.roxo_neon)

    titulo = fonte_titulo.render("TRIX", True, Colors.branco)
    surface.blit(titulo, titulo.get_rect(center=(500 // 2, 160)))

    instrucoes = fonte_info.render("Use ← → ↓ para mover, ↑ para girar a peça", True, Colors.branco)
    surface.blit(instrucoes, instrucoes.get_rect(center=(500 // 2, 205)))

    botao_iniciar.center = (500 // 2, 300)
    pygame.draw.rect(surface, Colors.verde_neon, botao_iniciar, border_radius=10)
    texto_botao = fonte_botao.render("INICIAR", True, Colors.preto)
    surface.blit(texto_botao, texto_botao.get_rect(center=botao_iniciar.center))

    dica = fonte_info.render("Clique em INICIAR", True, Colors.branco)
    surface.blit(dica, dica.get_rect(center=(500 // 2, 360)))


# Tela de Game Over
def tela_game_over(surface, pontuacao=None):
    surface.fill(Colors.roxo_neon)

    titulo = fonte_titulo.render("FIM DE JOGO", True, Colors.vermelho_neon)
    surface.blit(titulo, titulo.get_rect(center=(500 // 2, 160)))

    if pontuacao is not None:
        pontuacao_texto = fonte_subtitulo.render(f"Pontuação: {pontuacao}", True, Colors.branco)
        surface.blit(pontuacao_texto, pontuacao_texto.get_rect(center=(500 // 2, 210)))

    botao_reiniciar.center = (500 // 2, 300)
    pygame.draw.rect(surface, Colors.verde_neon, botao_reiniciar, border_radius=10)
    texto_botao = fonte_botao.render("REINICIAR", True, Colors.preto)
    surface.blit(texto_botao, texto_botao.get_rect(center=botao_reiniciar.center))

    dica = fonte_info.render("Clique em REINICIAR", True, Colors.branco)
    surface.blit(dica, dica.get_rect(center=(500 // 2, 360)))


# Tela principal do jogo
def tela_jogo(surface):
    surface.fill(Colors.roxo_neon)

    surface.blit(texto_pontuacao, (332, 20))
    pygame.draw.rect(surface, Colors.azul_claro, retangulo_pontuacao, border_radius=10)

    texto_score = fonte_titulo.render(str(getattr(jogo, "score", 0)), True, Colors.branco)
    surface.blit(texto_score, texto_score.get_rect(center=retangulo_pontuacao.center))

    # desenha o tabuleiro e a peça atual
    jogo.draw(surface)

    # próximo bloco
    pygame.draw.rect(surface, Colors.azul_claro, retangulo_proximo, border_radius=10)
    texto_proximo = fonte_info.render("PRÓXIMO BLOCO", True, Colors.branco)
    surface.blit(texto_proximo, (retangulo_proximo.x + 8, retangulo_proximo.y - 20))
    desenhar_proximo_bloco(surface, jogo.next_block, retangulo_proximo)


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
