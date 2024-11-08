from typing import List
from sistema.pedido import Pedido
from sistema.usuario import Usuario
from sistema.estoque import Estoque


class Loja:
    def __init__(self) -> None:
        self._estoque: Estoque = Estoque()
        self._usuarios: List[Usuario] = []
        self._pedidos: List[Pedido] = []
        self._receita: float = 0

    def registrar_usuario(self, nome: str, cpf: str, endereço: str, telefone: str, email: str, cartao_credito: int, senha: str) -> None:
        usuario = Usuario(nome, cpf, endereço, telefone, email, cartao_credito, senha)
        self._usuarios.append(usuario)
    
    def login_usuario(self, cpf: str, senha: str) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.get_cpf == cpf and usuario.get_senha == senha:
                return usuario
        return None
    
    def adicionar_pedido(self, pedido: Pedido) -> None:
        self._pedidos.append(pedido)

    def get_usuarios(self) -> List[Usuario]:
        return self._usuarios
    
    def get_estoque(self) -> Estoque:
        return self._estoque
    
    def get_pedidos(self) -> List[Pedido]:
        return self._pedidos
    
    def get_receita(self) -> float:
        return self._receita

    def atualizar_receita(self, valor) -> None:
        self._receita += valor