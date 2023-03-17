#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0

print('-='*19)

print('\033[1;37m Digite um número inteiro qualquer*\033[m ')
n = int(input('- '))

for c in range(2, n):
    if n % c == 0:
        cont = cont + 1
        break

if cont == 0:
    print('\033[2;34m {} é um número primo \033[m'.format(n))

else:
    ('{} não é um número primo'.format(n))

print('-='*19)
