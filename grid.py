import pygame

from colors import Colors

class Grid:
    def __init__(self):
        self.num_linhas= 20
        self.num_colunas= 10
        self.tamanho_celula= 30
        #inicia no zero a grid
        self.grid= [[0 for j in range(self.num_colunas)] for i in range(self.num_linhas)]
        self.colors= Colors.cores_celulas()


    def print_grid(self):
        for linha in range (self.num_linhas):
            for coluna in range (self.num_colunas):
                print(self.grid[linha][coluna], end= " ")
            #imprime valor linha por linha
            print()
    
    def dentro (self, linha, coluna):
        if linha >= 0 and linha < self.num_linhas and coluna >= 0 and coluna < self.num_colunas:
            return True
        return False
    
    #verifica se a celula está vazia
    def vazia (self, linha, coluna):
        if self.grid[linha][coluna] == 0:
            return True
        return False

    #função para desenhar o grid 
    def draw(self, tela):
        #itera cada celula no grid
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                valor_celula= self.grid[linha][coluna] 
                #soma um pixel para que a linha seja visivel no grid e subtrai (para que fique 29 pixels)
                celula_rect= pygame.Rect(coluna*self.tamanho_celula +1, linha*self.tamanho_celula +1,
                self.tamanho_celula -1, self.tamanho_celula -1)
                pygame.draw.rect(tela, self.colors[valor_celula], celula_rect)
   

