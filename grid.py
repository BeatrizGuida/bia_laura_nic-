import pygame

class Grid:
    def __init__(self):
        self.num_linhas= 20
        self.num_colunas= 10
        self.tamanho_celula= 30
        #inicia no zero a grid
        self.grid= [[0 for j in range(self.num_colunas)] for i in range(self.num_linhas)]
        self.colors= self.cor_dos_blocos()


    def print_grid(self):
        for linha in range (self.num_linhas):
            for coluna in range (self.num_colunas):
                print(self.grid[linha][coluna], end=" ")
            #imprime valor linha por linha
            print()
    

    def cor_dos_blocos(self):
        #sete blocos de cores diferentes para as peças
        cinza_escuro = (26, 31, 40)       
        verde_neon   = (77, 255, 0)     
        vermelho_neon = (255, 30, 30)     
        laranja_neon = (255, 140, 0)      
        amarelo_neon = (255, 255, 0)       
        roxo_neon    = (191, 0, 255)       
        ciano_neon   = (0, 255, 255)      
        azul_neon    = (0, 100, 255)  
             
        return [cinza_escuro, verde_neon, vermelho_neon, laranja_neon, amarelo_neon, roxo_neon, ciano_neon, azul_neon]
    

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
   
