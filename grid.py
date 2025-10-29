class Grid:
    def __init__(self):
        self.num_linhas= 20
        self.num_colunas= 10
        self.tamanho_celula= 30
        #inicia no zero a grid
        self.grid= [[0 for j in range(self.num_colunas)] for i in range(self.num_linhas)]
        self.colors= self.get_cell_colors()


    def print_grid(self):
        for linha in range (self.num_linhas):
            for coluna in range (self.num_colunas):
                print(self.grid[linha][coluna], end=" ")
            #imprime valor linha por linha
            print()
    

    def get_cell_colors(self):
        cinza_escuro = (26, 31, 40)
        verde = (47, 230, 23)
        vermelho = (232, 18, 18)
        laranja= (226, 116, 17)
        amarelo = (237, 234, 4)
        roxo = (166, 0, 247)
        ciano = (21, 204, 209)
        azul = (13, 64, 216)

        return [cinza_escuro, verde, vermelho, laranja, amarelo, roxo, ciano, azul]