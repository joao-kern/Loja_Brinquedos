from typing import Callable, List

from sistema.loja import Loja


class Sistema_Adm:
    def __init__(self, loja: Loja) -> None:
        self._loja: Loja = loja
        self._execucao: bool = False
        self._operacoes: List[Callable] = [
            self.adicionar_brinquedo,
            self.mudar_estoque,
            self.mudar_preco,
            self.estoque,
            self.receita_total,
            self.usuarios,
            self.pedidos,
            self.sair_conta
            
        ]
    
    def run(self) -> None:
        self._execucao = True
        while self._execucao: 
            print('Menu de Ações')
            print('1 - Adicionar Brinquedo')
            print('2 - Mudar Estoque')
            print('3 - Mudar Preço')
            print('4 - Ver Estoque')
            print('5 - Ver Receita Total')
            print('6 - Ver Usuários')
            print('7 - Ver pedidos realizados')
            print('8 - Sair da conta')
            op = self.input_int("Escolha a ação que deseja realizar: ")
            self._operacoes[op - 1]()
            print()
    
    def adicionar_brinquedo(self) -> None:
        print('Adicionar Brinquedo')
        print()
        nome = self.input_str('Nome: ')
        preco = self.input_float('Preço: R$ ')
        faixa_etaria = self.input_str('Faixa etária (X anos até X anos): ')
        estoque = self.input_int('Estoque: ')
        self._loja.get_estoque().adicionar_brinquedo(nome, preco, faixa_etaria, estoque)
        print()
        print('Brinquedo adicionado com sucesso')
        print()

    def mudar_estoque(self) -> None:
        print('Mudar Estoque')
        print()
        nome_brinquedo = self.input_str('Nome brinquedo: ')
        brinquedo = self._loja.get_estoque().buscar_brinquedo(nome_brinquedo)
        if brinquedo is None:
            print('Esse brinquedo não existe no estoque')
        else:
            estoque = self.input_int('Digite o novo estoque: ')
            brinquedo.set_estoque(estoque)
            print()
            print('Novo estoque definido com sucesso')
        print()

    def mudar_preco(self) -> None:
        print('Mudar Preço')
        print()
        nome_brinquedo = self.input_str('Nome brinquedo: ')
        brinquedo = self._loja.get_estoque().buscar_brinquedo(nome_brinquedo)
        if brinquedo is None:
            print('Esse brinquedo não existe no estoque')
        else:
            preco = self.input_int('Digite o novo preço: R$ ')
            brinquedo.set_preco(preco)
            print()
            print('Novo preço definido com sucesso')
        print()  

    def estoque(self) -> None:
        print('Estoque')
        print()
        self._loja.get_estoque().print_brinquedos()
        print()

    def receita_total(self) -> None:
        print('Receita Total')
        print()
        print(f'R$ {self._loja.get_receita():.2f}')
        print()

    def usuarios(self) -> None:
        print('Usuários')
        for usuario in self._loja.get_usuarios():
            usuario.print()
        print()

    def pedidos(self) -> None:
        print('Pedidos')
        for pedido in self._loja.get_pedidos():
            pedido.print()
        print()

    def sair_conta(self) -> None:
        self._execucao = False
        print()
        print('Sessão finalizada com sucesso!')
        print()

    def input_int(self, text: str) -> int:
        while True:
            try:
                return int(input(text))
            except:
                print("*Valor não válido*")

    def input_str(self, text: str) -> str:
        while True:
            try:
                return input(text)
            except:
                print("*Valor não válido*")
    
    def input_float(self, text: str) -> float:
        while True:
            try:
                return float(input(text))
            except:
                print("*Valor não válido*")
    
