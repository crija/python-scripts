class Person:
    def __init__(self, name, age, logged):
        self.name = name
        self.age = age
        self.logged = logged

    def armazenar_dados(self):
        print(f'Nome: {self.name}, Idade: {self.age}, Loggend: {self.logged}')

    def permitir_acesso(self):
        if self.age < 18:
            print('Negar acesso!')
            self.logged = False
        else:
            print('Login feito com sucesso')
            self.logged = True


person1 = Person('Ana', 12, False)
person1.permitir_acesso()
person1.armazenar_dados()
