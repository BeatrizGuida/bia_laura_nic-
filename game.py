from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid= Grid()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block= self.get_random_block()
        self.next_block= self.get_random_block()
        self.game_over = False   # <-- importante inicializar aqui
        # (opcional) score/level
        self.score = 0
        self.level = 1
        # musica:
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
		self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

		pygame.mixer.music.load("Sounds/music.ogg")
		pygame.mixer.music.play(-1)

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block= random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_esquerda(self):
        self.current_block.movimento(0, -1)
        if self.bloqueia_movimento() == False or self.verifica_bloco() == False:
            self.current_block.movimento(0, 1)


    def move_direita(self):
        self.current_block.movimento(0, 1)
        if self.bloqueia_movimento() == False or self.verifica_bloco() == False:
            self.current_block.movimento(0, -1)

    def move_baixo(self):
        self.current_block.movimento(1, 0)
        if self.bloqueia_movimento() == False or self.verifica_bloco() == False:
            self.current_block.movimento(-1, 0)
            self.lock_block()

    def lock_block(self):
        #atualizar a grid com a posição do bloco travado
        pecas = self.current_block.movimento_celulas()
        # Antes de escrever, verificar se todas as peças estão dentro do grid.
        # Se alguma peça estiver fora (por exemplo, linha < 0 ou coluna fora),
        # é sinal que o bloco não coube -> game over.
        for peca in pecas:
            if not self.grid.dentro(peca.linha, peca.coluna):
                # Se a peça estiver fora para cima (linha < 0) ou fora das colunas,
                # considerei como fim de jogo ao travar
                self.game_over = True
                return
        #escrever as peças na grid

        for peca in pecas:
            self.grid.grid[peca.linha][peca.coluna] = self.current_block.id
        self.current_block= self.next_block
        #pega um novo bloco aleatório
        self.next_block= self.get_random_block()

        # Limpa linhas completas
        linhas_removidas = self.grid.limpa_linhas_completas()
        if linhas_removidas > 0:
            # (opcional) atualizar score
            self.score += 100 * linhas_removidas

        # Se o novo bloco já está colidindo com algo (spawn bloqueado), game over
        if not self.verifica_bloco():
            self.game_over = True


    def reset(self):
        self.grid.reset()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block= self.get_random_block()
        self.next_block= self.get_random_block()

    def verifica_bloco(self):
        pecas= self.current_block.movimento_celulas()
        for peca in pecas:
            #if self.grid.vazia(peca.linha, peca.coluna) == False:
            # se fora do grid ou célula ocupada -> bloco inválido
            if not self.grid.vazia(peca.linha, peca.coluna):
                return False
        return True

    def rotaciona(self):
        self.current_block.rotaciona()
        if self.bloqueia_movimento() == False or self.verifica_bloco() == False:
            self.current_block.desfaz_rotacao()


    def bloqueia_movimento (self):
        tiles= self.current_block.movimento_celulas()
        for tile in tiles:
            if self.grid.dentro(tile.linha, tile.coluna) == False:
                return False
        return True
    
    def draw(self, tela):
        self.grid.draw(tela)
        self.current_block.draw(tela)

        
