# Login de acesso: Verificar o gmail e senha para permitir ou negar o acesso do usuário.

class Usuario:
    def __init__(self, name, age, gmail, senha, logged):
        self.name = name
        self.age = age
        self.gmail = gmail
        self.senha = senha
        self.logged = logged

    def login(self, gmail_tentativa, senha_tentativa):
        if self.gmail == gmail_tentativa and self.senha == senha_tentativa:
            print(f'{self.logged == False}')
        else:
            print(f'{self.logged == True}')

    def armazenar_dados(self):
        return (f'Usuário: {self.name, self.age, self.logged}')

person1 = Usuario('Ana', 14, 'aninha@gmail.com', '90gE1', False)

person1.login('aninha@gmail.com', '90gw1')
person1.armazenar_dados()
