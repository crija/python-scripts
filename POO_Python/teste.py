class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


pessoa1 = Pessoa('Eduardo', 27, 'M')
print(f'1 nome: {pessoa1.nome}, idade: {pessoa1.idade}, sexo: {pessoa1.sexo}')

pessoa1.nome = 'Claudio'
pessoa1.idade = 34

print(f'2 nome: {pessoa1.nome}, idade: {pessoa1.idade}, sexo: {pessoa1.sexo}')

pessoa2 = Pessoa('Bia', 12, 'F')
print(f'3 nome: {pessoa2.nome}, idade: {pessoa2.nome}, sexo: {pessoa2.sexo}')

print(Pessoa)