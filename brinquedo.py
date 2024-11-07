class Brinquedo:
    def __init__(self, nome, preco, faixa_etaria, estoque):
        self._nome = nome
        self._preco = preco
        self._faixa_etaria = faixa_etaria
        self._estoque = estoque

    def set_estoque(self, estoque):
        self._estoque = estoque

    def set_preco(self, preco):
        self._preco = preco

    def diminuir_estoque(self):
        self._estoque -= 1
    
    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco
    
    def get_faixa_etaria(self):
        return self._faixa_etaria
    
    def get_estoque(self):
        return self._estoque
    
    def print(self):
        print(f'{self._nome}:')
        print(f'- Preço: R$ {self._preco:.2f}')
        print(f'- Faixa Etária: {self._faixa_etaria}')
        print(f'- Estoque: {self._estoque}')
    
