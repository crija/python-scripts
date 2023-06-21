#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 

#A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteandos pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores aleatórios: ', end='')
    for n in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando todos os valores pares dos números: {lista}, o resultado é {soma}')
            
num = list()
sorteia(num)
somaPar(num)

