from loja import Loja
from usuario import Usuario
from sistema_adm import Sistema_Adm
from sistema_cliente import Sistema_Cliente

class Sistema:
    def __init__(self):
        self._loja = Loja()
        self._adm_usuario = "adm"
        self._adm_senha = "Administrador@2761"
        self._execucao = False
        self._operacoes = [
            self.criar_conta,
            self.login_conta,
            self.login_adm,
            self.finalizar_programa
        ]

    def run(self):
        self._execucao = True
        while self._execucao: 
            print('Menu de Ações')
            print('1 - Criar Conta')
            print('2 - Entrar na sua Conta - Cliente')
            print('3 - Entrar na sua Conta - Administrador')
            print('4 - Finalizar Programa')

            op = self.input_int("Escolha a ação que deseja realizar: ")
            self._operacoes[op - 1]()
            print()

    def criar_conta(self):
        print('Criar Conta')
        print()
        validacao_cpf = False
        validacao_senha = False
        validacao_telefone = False
        validacao_email = False
        validacao_cep = False
        nome = self.input_str('Nome: ').title().strip()
        while not validacao_cpf:
            cpf = self.input_str('CPF (XXX.XXX.XXX-XX): ').strip()
            validacao_cpf = Usuario.validar_cpf(cpf, self._loja.get_usuarios())
        while not validacao_cep:
            cep = self.input_str('CEP (XXXXX-XXX): ').title().strip()
            validacao_cep = Usuario.validar_cep(cep)
        while not validacao_telefone:
            telefone = self.input_str('Telefone ((XX) XXXXX-XXXX) : ')
            validacao_telefone = Usuario.validar_telefone(telefone)
        while not validacao_email:
            email = self.input_str('Email: ').lower().strip()
            validacao_email = Usuario.validar_email(email)
        cartao_credito = self.input_int('Cartão de crédito (Sem espaços): ')
        while not validacao_senha:
            senha = self.input_str('Senha: ').strip()
            validacao_senha = Usuario.validar_senha(senha, cpf, nome, email)
        self._loja.registrar_usuario(nome, cpf, cep, telefone, email, cartao_credito, senha)
        print()
        print('Conta criada com sucesso')
        print()
            
    def login_conta(self):
        print('Login Conta - Cliente')
        print()
        cpf = self.input_str('CPF (XXX.XXX.XXX-XX): ')
        login_cpf = self.verifica_login_usuario_cpf(cpf)
        senha = self.input_str('Senha: ')
        login_senha, usuario = self.verifica_login_usuario_senha(senha)
        if not login_cpf:
            print("CPF Incorreto")
        if not login_senha:
            print("Senha incorreta")
        else:
            print()
            print('Login realizado com sucesso')
            print()
            sistema_cliente = Sistema_Cliente(self._loja, usuario)
            sistema_cliente.run()
            
    def login_adm(self):
        print('Login Conta - Administrador')
        print()
        usuario = self.input_str('Usuário: ')
        senha = self.input_str('Senha: ')
        login= self.verifica_login_adm(usuario, senha)
        if login:
            print()
            print("Login realizado com sucesso")
            print()
            sistema_adm = Sistema_Adm(self._loja)
            sistema_adm.run()
            
    def verifica_op_login(self, op):
        while op > 4 or op < 1:
            print('*OPERAÇÃO  INEXISTENTE*')
            return False
        return True

    def verifica_login_usuario_cpf(self, cpf):
        for usuario in self._loja.get_usuarios():
            if usuario.get_cpf() == cpf:
                return True
        return False

    def verifica_login_usuario_senha(self, senha):
        for usuario in self._loja.get_usuarios():
            if usuario.get_senha() == senha:
                return True, usuario
        return False, None

    def verifica_login_adm(self, usuario, senha):
        if self._adm_usuario == usuario and self._adm_senha == senha:
            return True
    
        return False

    def finalizar_programa(self):
            print("Programa Finalizado")
            self._execucao = False
    
    def input_str(self, text):
        while True:
            try:
                return input(text)
            except:
                print("*Valor não válido*")

    def input_int(self, text):
        while True:
            try:
                return int(input(text))
            except:
                print("*Valor não válido*")
    
    def get_sistema_adm(self):
        return self._sistema_adm

    def get_loja(self):
        return self._loja
    
    