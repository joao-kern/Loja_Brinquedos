class Brinquedo:
    def __init__(self, nome: str, preco: float, faixa_etaria: str, estoque: int) -> None:
        self._nome: str = nome
        self._preco: float = preco
        self._faixa_etaria: str = faixa_etaria
        self._estoque: int = estoque

    def set_estoque(self, estoque: int) -> None:
        self._estoque = estoque

    def set_preco(self, preco: float) -> None:
        self._preco = preco

    def diminuir_estoque(self) -> None:
        self._estoque -= 1
    
    def get_nome(self) -> str:
        return self._nome

    def get_preco(self) -> float:
        return self._preco
    
    def get_faixa_etaria(self) -> str:
        return self._faixa_etaria
    
    def get_estoque(self) -> int:
        return self._estoque
    
    def print(self) -> None:
        print(f'{self._nome}:')
        print(f'- Preço: R$ {self._preco:.2f}')
        print(f'- Faixa Etária: {self._faixa_etaria}')
        print(f'- Estoque: {self._estoque}')
    
