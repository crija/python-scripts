#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas células de cada valor serão entregues
#Considere que o caixa possui celulas de 50, 20, 10 e 1

sacar = int(input('Qual valor você deseja sacar? R$'))

if sacar > 10:
    cem = int(sacar / 100)
    cinquenta = sacar / 50

    cinquenta = int(sacar/ 50)
    sacar = sacar % 50

    vinte = int(sacar / 20)
    sacar = sacar % 20

    dez = int(sacar / 10)
    sacar = sacar % 10

    um = int(sacar / 1)

    print('Você vai receber {} notas de R$100,00'.format(cem))
    print('Você vai receber {} notas de R$50,00'.format(cinquenta))
    print('Você vai receber {} notas de R$20,00'.format(vinte))
    print('Você vai receber {} nota(s) de R$1,00'.format(um))

elif sacar < 10:
    print('Seu saldo não é suficiente.')
