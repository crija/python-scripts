class Person:
    def __init__(self, name, age, logged):
        self.name = name
        self.age = age
        self.logged = logged

    def acesso(self):
        if dados_sensiveis != dados_sensiveis:
            print('Negar acesso!')
            self.logged = False
        else:
            print('Login feito com sucesso')
            self.logged = True

    def armazenar_dados(self, dados_sensiveis):
        return (f'Dados de acesso: {self.name, self.age, self.logged}\nDados sensíveis: {dados_sensiveis}')

person1 = Person('Ana', 14, False)
dados_sensiveis = {'gmail': 'aninha@gmail.com', 'senha': 2976}
person1.acesso()
person1.armazenar_dados(dados_sensiveis)
