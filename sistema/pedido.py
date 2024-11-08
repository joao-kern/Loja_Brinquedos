from typing import List
from sistema.brinquedo import Brinquedo
from sistema.usuario import Usuario


class Pedido:
    def __init__(self, usuario: Usuario, carrinho: List[Brinquedo]):
        self._usuario: Usuario = usuario
        self._carrinho: List[Brinquedo] = carrinho
        self._total: float = 0
    
    def calcular_total(self) -> None:
        for brinquedo in self._carrinho:
            self._total += brinquedo.get_preco()

    def get_total(self) -> float:
        return self._total
    
    def print(self) -> None:
        print(f'Pedido realizado pelo usuário {self._usuario.get_nome()}')
        for brinquedo in self._carrinho:
            print(f'- {brinquedo.get_nome()}: R$ {brinquedo.get_preco():.2f}')
        print()