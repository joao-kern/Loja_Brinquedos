from typing import List
from sistema.brinquedo import Brinquedo

class Estoque:
    def __init__(self) -> None:
        self._brinquedos_estoque: List[Brinquedo] = []

    def adicionar_brinquedo(self, nome: str, preco: float, faixa_etaria: str, estoque: int) -> None:
        brinquedo = Brinquedo(nome, preco, faixa_etaria, estoque)
        self._brinquedos_estoque.append(brinquedo)
    
    def remover_brinquedo(self, brinquedo: Brinquedo) -> None:
        self._brinquedos_estoque.remove(brinquedo)
    
    def buscar_brinquedo(self, nome_brinquedo: str) -> Brinquedo | None:
        for brinquedo in self._brinquedos_estoque:
            if nome_brinquedo == brinquedo.get_nome():
                return brinquedo
        return None

    def get_brinquedos_estoque(self) -> List[Brinquedo]:
        return self._brinquedos_estoque   

    def print_brinquedos(self) -> None:
        for brinquedo in self._brinquedos_estoque:
            brinquedo.print()
            print()
              