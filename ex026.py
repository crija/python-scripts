#Crie um programa que leia um número e mostre o seu dobro, triplo e a raiz quadrada:

import math

n = float(input('Digite um número: '))

d = n * 2
t = n * 3
r = math.sqrt(n)

print('Double of {} is {} triple is {} and the root is {:.2f}.'.format(n, d, t, r ))
