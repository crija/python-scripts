#Crie um programa que leia dois números e mostre a soma entre eles.
#Pass.1 [Digite um número:]
#Pass.2 [Digite outro número]
#Pass.3 [Some os dois números]
#Pass.4 [Escreva uma string que mostre o resultado]

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2

print('A soma entre {} e {} vale {}'.format(n1, n2, s))
