#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso:
from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

e = 1
while e != 5:

    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')

    print('Digite 1, 2, 3, 4, ou 5!')
    e = int(input('-'))
    sleep(2)

    if e == 1:
        s = n1 + n2
        print('{} + {} = {}.'.format(n1, n2, s))
    elif e == 2:

        m = n1 * n2
        print('{} x {} = {}.'.format(n1, n2, m))

    elif e == 3:
        if n1 < n2:
            print('O número {} é menor que número {}.'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que número {}.'.format(n2, n1))
        elif n1 == n2:
            print('{} e {} tem valores iguais.'.format(n1, n2))

    elif e == 4:
        print('>>>Digite os novos números:')
        novnum1 = int(input('Digite outro número: '))
        novnum2 = int(input('Digite mais um número: '))

    elif e == 5:
        print('Você saiu do programa!')

    else:
        print('Essa opção não existe!')
