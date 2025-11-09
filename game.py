from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid= Grid()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block= self.get_random_block()
        self.next_block= self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block= random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_esquerda(self):
        self.current_block.movimento(0, -1)
        if self.bloqueia_movimento() == False:
            self.current_block.movimento(0, 1)


    def move_direita(self):
        self.current_block.movimento(0, 1)
        if self.bloqueia_movimento() == False:
            self.current_block.movimento(0, -1)

    def move_baixo(self):
        self.current_block.movimento(1, 0)
        if self.bloqueia_movimento() == False or self.verifica_bloco() == False:
            self.current_block.movimento(-1, 0)
            self.lock_block()

    def lock_block(self):
        #atualizar a grid com a posição do bloco travado
        pecas = self.current_block.movimento_celulas()
        for peca in pecas:
            self.grid.grid[peca.linha][peca.coluna] = self.current_block.id
        self.current_block= self.next_block
        #pega um novo bloco aleatório
        self.next_block= self.get_random_block()

    def verifica_bloco(self):
        pecas= self.current_block.movimento_celulas()
        for peca in pecas:
            if self.grid.vazia(peca.linha, peca.coluna) == False:
                return False
        return True

    def rotaciona(self):
        self.current_block.rotaciona()
        if self.bloqueia_movimento() == False:
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

        
