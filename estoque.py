from brinquedo import Brinquedo

class Estoque:
    def __init__(self):
        self._brinquedos_estoque = []

    def adicionar_brinquedo(self, nome, preco, faixa_etaria, estoque):
        brinquedo = Brinquedo(nome, preco, faixa_etaria, estoque)
        self._brinquedos_estoque.append(brinquedo)
    
    def remover_brinquedo(self, brinquedo):
        self._brinquedos_estoque.remove(brinquedo)
    
    def buscar_brinquedo(self, nome_brinquedo):
        for brinquedo in self._brinquedos_estoque:
            if nome_brinquedo == brinquedo.get_nome():
                return brinquedo
        return None

    def get_brinquedos_estoque(self):
        return self._brinquedos_estoque   

    def print_brinquedos(self):
        for brinquedo in self._brinquedos_estoque:
            brinquedo.print()
            print()
              