from colors import Colors
import pygame
from posicoes import Position

#cria blocos
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        #atualizar a posição de cada bloco
        self.linha = 0
        self.coluna = 0
        self.rotation_state = 0
        self.colors= Colors.cores_celulas()

    def movimento(self,linhas, colunas):
        self.linha += linhas
        self.coluna += colunas
    
    def movimento_celulas(self):
        tiles= self.cells[self.rotation_state]
        moved_posi= []
        for posicoes in tiles:
            #posição nova da celula (atualizadas)
            posicoes = Position (posicoes.linha + self.linha, posicoes.coluna + self.coluna)
            moved_posi.append(posicoes)
        return moved_posi
    

    def rotaciona (self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def canccela_rotacao (self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) -1
    

    def draw(self, tela):
        tiles= self.movimento_celulas()
        for tile in tiles:
            tile_rect= pygame.Rect(tile.coluna * self.cell_size +1, tile.linha * self.cell_size +1, 
            self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(tela, self.colors[self.id], tile_rect)


            