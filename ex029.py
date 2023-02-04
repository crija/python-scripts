import random

n1 = str(input('Primeiro nome do aluno: '))
n2 = str(input('Segundo nome do aluno: '))
n3 = str(input('Terceiro nome do aluno: '))
n4 = str(input('Quarto nome do aluno: '))

lista = [n1, n2, n3, n4]

sorteio = random.choice(lista)

print('A ordem da apresentação será')
