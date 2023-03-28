#Faça um programa que leia um número qualquer e mostre o seu fatorial:
#ex: 5! = 5x4x3x2x1 = 120;

from math import factorial

'''n = 2

while n != 1:

    n = int(input('Digite um número para ver seu fatorial: '))

    f = factorial(n)

    print('O fatorial de {} é {}.'.format(n, f))'''

for n in range(1, 3):

    n = int(input('Digite um número para calcular seu fatorial: '))

    f = factorial(n)

    print('O fatorial de {} é {}.'.format(n, f))
