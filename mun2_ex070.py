#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso:

e = 1
while e != 5:

    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite um valor: '))

    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')

    print('Digite 1, 2, 3, 4, ou 5!')
    e = int(input('-'))

    if e == 1:
        s = n1 + n2
        print('A soma dos números é {}.'.format(s))
    elif e == 2:

        m = n1 * n2
        print('O resultado é {}.'.format(m))

    elif e == 3:
        if n1 < n2:
            print('O número {} é menor que número {}.'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que número {}.'.format(n2, n1))
        elif n1 == n2:
            print('{} e {} tem valores iguais.'.format(n1, n2))

    elif e == 4:
        novnum1 = int(input('Digite outro número: '))
        novnum2 = int(input('Digite mais um número: '))

    elif e == 5:
        print('Você saiu do programa!')

    else:
        print('Essa opção não existe!')
