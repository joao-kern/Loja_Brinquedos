class Pedido:
    def __init__(self, usuario, carrinho):
        self._usuario = usuario
        self._carrinho = carrinho
        self._total = 0
    
    def calcular_total(self):
        for brinquedo in self._carrinho:
            self._total += brinquedo.get_preco()

    def get_total(self):
        return self._total
    
    def print(self):
        print(f'Pedido realizado pelo usuário {self._usuario.get_nome()}')
        for brinquedo in self._carrinho:
            print(f'- {brinquedo.get_nome()}: R$ {brinquedo.get_preco():.2f}')
        print()