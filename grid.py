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
        # if linha >= 0 and linha < self.num_linhas and coluna >= 0 and coluna < self.num_colunas:
        #     return True
        # return False
        return 0 <= linha < self.num_linhas and 0 <= coluna < self.num_colunas

    
    #verifica se a celula está vazia
    def vazia (self, linha, coluna):
        if self.grid[linha][coluna] == 0:
            return True
        return False
    

    def linhas_completas (self,linha):
        for coluna in range (self.num_colunas):
            if self.grid[linha][coluna] == 0:
                return False
        return True
    
    def limpa_linha (self, linha):
        for coluna in range (self.num_colunas):
            self.grid[linha][coluna] = 0

    def desce_linhas (self,linha, num_linhas):
        # for coluna in range (self.num_colunas):
        #     #Move a linha para baixo
        #     self.grid[linha + num_linhas][coluna] = self.grid[linha][coluna]
        #     #Limpa a linha que foi movida
        #     self.grid[linha][coluna] = 0
        destino = linha + num_linhas
        # segurança: não tentar escrever fora do grid
        if destino < 0 or destino >= self.num_linhas:
            return
        # copia a linha inteira
        self.grid[destino] = self.grid[linha][:]
        # limpa a linha original
        self.grid[linha] = [0 for _ in range(self.num_colunas)]


    def limpa_linhas_completas (self):
        linhas_completas= 0
        for linha in range (self.num_linhas -1, -1, -1):
            #verifica se a linha está completa
            if self.linhas_completas(linha):
                self.limpa_linha(linha)
                linhas_completas += 1   
            elif linhas_completas > 0:
                self.desce_linhas(linha, linhas_completas)
        return linhas_completas
    
    def reset(self):
        #redefinir valor das celulas para 0
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                self.grid[linha][coluna] = 0
                #grade reiniciada

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
   

