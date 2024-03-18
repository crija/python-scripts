'''
Login de acesso: Verificar o gmail e senha para permitir ou negar o acesso do usuário.
Mudar senha:
 - Verificar se o usuário está logado;
 - Usuário insere senha atual para a troca de senha ser possível;
 - Se a senha inserida estiver correta o usuário pode inserir a senha nova
 - Salvar a senha nova no lugar da senha antiga.
'''

class Usuario:
    def __init__(self, name, age, gmail, senha, logged):
        self.name = name
        self.age = age
        self.gmail = gmail
        self.senha = senha
        self.logged = logged

    def login(self, gmail_tentativa, senha_tentativa):
        if self.gmail == gmail_tentativa and self.senha == senha_tentativa:
            person1.logged = True
            print(f'Usuário logado: {self.logged}')
        else:
            person1.logged = False
            print(f'Usuário logado: {self.logged}')


    def trocar_senha(self, escolher_mudar_senha, senha_atual, nova_senha):
        if self.logged == True:
            print('Quer mudar a senha?')
            if escolher_mudar_senha == 'sim':
                print('Digite sua senha atual')
                if senha_atual == self.senha:
                    print('Digite sua nova senha')
                    person1.senha = nova_senha
                    print(f'senha anterior: {senha_atual}')
                    print(f'nova senha: {nova_senha}')
                else:
                    print('senha incorreta')
            else:
                print('ok')

    def armazenar_dados(self):
        print(f'Usuário: {self.name, self.age, self.logged, self.gmail, self.senha}')

person1 = Usuario('Ana', 14, 'a', 'b', False)

person1.login('a', 'b')
person1.trocar_senha('sim', 'b', '4qa2')
person1.armazenar_dados()

