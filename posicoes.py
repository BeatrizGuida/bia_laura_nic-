class Position:
    def __init__(self, linha, coluna):
        self.linha= linha
        self.coluna= coluna
    def mostrar_posicao(self):
        return f"Linha: {self.linha}, Coluna: {self.coluna}"
    