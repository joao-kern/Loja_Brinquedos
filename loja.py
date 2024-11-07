from usuario import Usuario
from estoque import Estoque


class Loja:
    def __init__(self):
        self._estoque = Estoque()
        self._usuarios = []
        self._pedidos = []
        self._receita = 0

    def registrar_usuario(self, nome, cpf, endereço, telefone, email, cartao_credito, senha):
        usuario = Usuario(nome, cpf, endereço, telefone, email, cartao_credito, senha)
        self._usuarios.append(usuario)
    
    def login_usuario(self, cpf, senha):
        for usuario in self._usarios:
            if usuario.get_cpf == cpf and usuario.get_senha == senha:
                return usuario
        return None
    
    def adicionar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def get_usuarios(self):
        return self._usuarios
    
    def get_estoque(self):
        return self._estoque
    
    def get_pedidos(self):
        return self._pedidos
    
    def get_receita(self):
        return self._receita

    def atualizar_receita(self, valor):
        self._receita += valor