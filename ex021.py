import random

nome1 = input('Digite seu nome: ')
nome2 = input('Digite seu nome: ')
nome3 = input('Digite seu nome: ')
nome4 = input('Digite seu nome: ')

lista = [nome1, nome2, nome3, nome4]

sorteio = random.choice(lista)

print('O aluno sorteado foi:',sorteio)
