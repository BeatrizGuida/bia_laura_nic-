class Grid:
    def __init__(self):
        self.num_linhas= 20
        self.num_colunas= 10
        self.tamanho_celula= 30
        self.grid= [[0 for j in range(self.num_colunas)] for i in range(self.num_linhas)]

        
    def print_grid(self):
        for linha in range (self.num_linhas):
            for coluna in range (self.num_colunas):
                print(self.grid[linha][coluna], end=" ")
            print()
    