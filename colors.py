#copiar as cores da grid.py para cá
class Colors:
    cinza_escuro = (26, 31, 40)       
    verde_neon   = (77, 255, 0)     
    vermelho_neon = (255, 30, 30)     
    laranja_neon = (255, 140, 0)      
    amarelo_neon = (255, 255, 0)       
    roxo_neon    = (191, 0, 255)       
    ciano_neon   = (0, 255, 255)      
    azul_neon    = (0, 100, 255)  
    branco= (255, 255, 255)
    preto= (0, 0, 0)
    azul_claro= (59, 85, 162)

    @classmethod
    def cores_celulas(cls):
        return [cls.cinza_escuro, cls.verde_neon, cls.vermelho_neon, cls.laranja_neon,
                cls.amarelo_neon, cls.roxo_neon, cls.ciano_neon, cls.azul_neon]