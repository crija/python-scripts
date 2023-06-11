#Faça um programa que tenha uma função chamada maior();
#que receba vários parâmetros com valores inteiros.
#Seu programa tem que mostrar o total de números digitados.

from time import sleep

lista = []

def maior(*num):
    print()
    print('RESULTADO...\n')
    sleep(2)
    for n in num:
        print(f'Os números são: {lista}')
        print(f'Foram digitados:', end = " ")
        print(len(lista), end = ' ')
        print('números \n')
    
#programa principal
while True:
    v = int(input('Digite um número: '))
    res = int(input('Digite 999 para parar: '))
    lista.append(v)
    if res == 999:
        break

maior(lista)

