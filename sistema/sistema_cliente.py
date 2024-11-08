from typing import Callable, List
from sistema.brinquedo import Brinquedo
from sistema.loja import Loja
from sistema.pedido import Pedido
from sistema.usuario import Usuario

class Sistema_Cliente:
    def __init__(self, loja: Loja, usuario: Usuario | None):
        self._loja: Loja = loja
        self._usuario: Usuario | None = usuario
        self._carrinho: List[Brinquedo] = []
        self._execucao: bool = False
        self._operacoes: List[Callable] = [
            self.adicionar_brinquedo,
            self.itens_carrinho,
            self.finalizar_compra,
            self.sair_conta
        ]

    def run(self):
        self._execucao = True
        while self._execucao: 
            print('Menu de Ações')
            print('1 - Adicionar brinquedo no carrinho')
            print('2 - Ver itens no carrinho')
            print('3 - Finalizar compra')
            print('4 - Sair da Conta')

            op = self.input_int("Escolha a ação que deseja realizar: ")
            self._operacoes[op - 1]()
            print()
    
    def adicionar_brinquedo(self):
        print('Adicionar brinquedo no carrinho')
        print()
        self._loja.get_estoque().print_brinquedos()
        nome_brinquedo = self.input_str('Digite o brinquedo que desejas adicionar ao carrinho: ')
        brinquedo = self._loja.get_estoque().buscar_brinquedo(nome_brinquedo)
        if brinquedo == None:
            print('Esse brinquedo não existe no estoque')
        else:
            self._carrinho.append(brinquedo)
            print('Brinquedo adicionado ao carrinho com sucesso!')
        print()     

    def itens_carrinho(self):
        print('Itens carrinho:')
        print()
        for brinquedo in self._carrinho:
            print(f'- {brinquedo.get_nome()}: R$ {brinquedo.get_preco():.2f}')
            print()
    
    def finalizar_compra(self):
        pedido = Pedido(self._usuario, self._carrinho)
        pedido.calcular_total()
        self._loja.adicionar_pedido(pedido)
        print('Itens carrinho:')
        print()
        for brinquedo in self._carrinho:
            print(f'_ {brinquedo.get_nome()}: R$ {brinquedo.get_preco():.2f}')
            print()
        print(f'Total carrinho: R$ {pedido.get_total():.2f}')
        self._loja.atualizar_receita(pedido.get_total())
        for brinquedo in self._carrinho:
            brinquedo.diminuir_estoque()
        self._carrinho = []
        print()
        print('Compra finalizada')
        print()

    def sair_conta(self):
        self._execucao = False
        print('Sessão finalizada')
        
    def input_int(self, text):
        while True:
            try:
                return int(input(text))
            except:
                print("*Valor não válido*")

    def input_str(self, text):
        while True:
            try:
                return input(text).strip().title()
            except:
                print("*Valor não válido*")
                        