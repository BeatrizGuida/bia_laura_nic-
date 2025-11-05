from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid= Grid()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block= self
        self.next_block= self

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block= random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_esquerda(self):
        self.current_block.move(0, -1)

    def move_direita(self):
        self.current_block.move(0, 1)

    def move_baixo(self):
        self.current_block.move(1, 0)
    
    def draw(self, tela):
        self.grid.draw(tela)
        self.current_block.draw(tela)

        
