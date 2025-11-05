from colors import Colors
import pygame

#cria blocos
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors= Colors.cores_celulas()

    def draw(self, tela):
        tiles= self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect= pygame.Rect(tile.coluna * self.cell_size +1, tile.row * self.cell_size +1, 
            self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(tela, self.colors[self.id], tile_rect)


            