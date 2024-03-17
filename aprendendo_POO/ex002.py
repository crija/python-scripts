# Login de acesso: Verificar o gmail e senha para permitir ou negar o acesso do usuário.
# Mudar senha: Fazer verificação da senha atual para o usuário conseguir mudar a senha.

class Usuario:
    def __init__(self, name, age, gmail, senha, logged, mudar_senha, verificar_senha):
        self.name = name
        self.age = age
        self.gmail = gmail
        self.senha = senha
        self.logged = logged
        self.mudar_senha = mudar_senha
        self.verificar_senha = verificar_senha

    def login(self, gmail_tentativa, senha_tentativa):
        if self.gmail == gmail_tentativa and self.senha == senha_tentativa:
            print(f'Usuário logado: {self.logged == False}')
        else:
            print(f'Usuário logado: {self.logged == True}')

   def armazenar_dados(self):
        return (f'Usuário: {self.name, self.age, self.logged}')

'''  def verificar_escolha(self, escolher_mudar_senha):
        if escolher_mudar_senha == 'sim':
            print(f'Mudar senha: {self.mudar_senha == True}')
        else:
            print(f'Mudar senha: {self.mudar_senha == False}')

    def verificar_senha_atual(self, verificar):
        if verificar == self.senha:
            print(f'Senha correta: {self.verificar_senha == True}')
        else:
            print('Senha incorreta')
'''

person1 = Usuario('Ana', 14, 'aninha@gmail.com', '90gE1', False, 'sim', '90gE1')

person1.login('aninha@gmail.com', '90gE1')
person1.armazenar_dados()

'''
person1.verificar_escolha('sim')
person1.verificar_senha_atual('90gE1')
'''
