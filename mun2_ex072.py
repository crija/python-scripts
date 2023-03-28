#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
#No final, mostre quantos números foram digitados e qual foi a soma entre eles.

import random
c = 0
s = 0
n = 1
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        c = c + n
        s = s + 1
print('Você digitou {} números e a soma é {}'.format(s, c))
