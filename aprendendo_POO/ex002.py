class Person:
    def __init__(self, name, age, logged):
        self.name = name
        self.age = age
        self.logged = logged

def armazenar_dados(self):
    print(f'Nome: {self.name}, Idade: {self.age}, Loggend: {self.logged}')

person1 = Person('Ana', 12, True)
armazenar_dados(person1)
