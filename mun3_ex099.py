#Faça um programa que tenha uma função chamada contador()
#Que receba três parametros:início, fim e passo e realize a contagem
#Seu programa tem que realizar três contagens através da função criada
# A)De 1 até 10, de 1 em 1;
# B)De 10 até 0, de 2 em 2;
# Uma contagem personalizada pelo usuário.

from time import sleep

def contador(a, b, c):
    print('-' * 20)
    print(f'Inicio:{a}, Fim:{b}, Passo:{c}')
    for n in range(a, b, c):
        print(n)
        sleep(1)
    print('-' * 20)

contador(1, 11, 1)
contador(10, -1, -2)


