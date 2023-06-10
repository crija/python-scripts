#Faça um programa que tenha uma função chamada maior();
#que receba vários parâmetros com valores inteiros.
#Seu programa tem que mostrar o total de números digitados.

from time import sleep


def maior(*num):
    print(f'Os números são: {num}')
    print(f'Foram digitados:', end = " ")
    print(len(num), end = ' ')
    print('números \n')
    

    sleep(2)
    
#programa principal
maior(2, 4, 7, 1)
maior(3, 9)
maior(2)
maior(8, 0, 5)

