import re
from typing import List

class Usuario:
    def __init__(self, nome: str, cpf: str, cep: str, telefone: str, email: str, cartao_credito: int, senha: str):
        self._nome: str = nome
        self._cep: str = cep
        self._telefone: str = telefone
        self._email: str = email
        self._cpf: str = cpf
        self._cartão_credito: int = cartao_credito
        self._senha: str = senha
    
    @staticmethod
    def validar_cpf(cpf, usuarios: List) -> bool:
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            print('CPF fora do formato')
            return False
        for usuario in usuarios:
            if cpf == usuario.get_cpf():
                print('Já existe uma conta com esse CPF')
                return False
        return True
    
    @staticmethod
    def validar_senha(senha: str, cpf: str, nome: str, email: str) -> bool:
        if len(senha) < 8:
            print('* Senha menor do que 8 dígitos')
            return False
         
        elif not re.search(r'\d', senha):
            print('* Senha precisa conter pelo menos 1 número')
            return False
        
        elif not re.search(r'[A-Z]', senha):
            print('* Senha precisa conter pelo menos 1 letra maíuscula')
            return False
        
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            print('* Senha precisa conter pelo menos 1 caracter especial')
            return False
        
        elif cpf in senha or nome.lower() in senha or nome.title() in senha  or nome.upper() in senha or email in senha:
            print('* Informações pessoais como nome, email ou cpf compoem a senha')
            return False
        
        return True

    @staticmethod
    def validar_cep(cep: str) -> bool:
        if not re.match(r'^\d{5}-\d{3}$', cep):
            print('CEP fora do formato')
            return False
        return True

    @staticmethod
    def validar_telefone(telefone:str) -> bool:
        if not re.match(r'^\(\d{2}\)\s?\d{4,5}\-\d{4}$', telefone):
            print('Telefone fora do formato')
            return False
        return True
    
    @staticmethod
    def validar_email(email: str) -> bool:
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            print('Email inválido')
            return False
        return True

    def get_nome(self) -> str:
        return self._nome
    
    def get_cpf(self) -> str:
        return self._cpf
    
    def get_senha(self) -> str:
        return self._senha
    
    def get_telefone(self) -> str:
        return self._telefone

    def get_email(self) -> str:
        return self._email
    
    def print(self) -> None:
        print(f'Usuário: {self._nome}')
        print(f'- CPF: {self._cpf}')
        print(f'- Email: {self._email}')
        print(f'- CEP: {self._cep}')
        print(f'- Telefone: {self._telefone}')
        print()
        

        