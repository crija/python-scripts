

#Escrever um programa que leia a opção desejada do cliente,

import time

print('Remédios ainda em estoque:')
print('¨'* 15)
print('''
Tilenol
Patanol
''')
print('¨'* 15)

remedio = str(input('Qual das opções você deseja? '))

nome = str(input('Qual seu nome? '))

idade = int(input('Quantos anos você tem? '))

# especifique se o remedio escolhido é recomendado para a idade dele ou nao,

if remedio == 'Tilenol' or remedio == 'Patanol':

    if idade < 18:

        print('{} NÃO é recomendado para menor de idade.'.format(remedio))

# se o usuario for menor de idade nao autorize  a compra

        print('A venda de {} não é autorizada para menores de 18 anos'.format(remedio))
        print('Compareça a loja mais próxima com um adulto responsável para a compra.')

    elif idade >= 18:

        print('CARREGANDO INFORMAÇÕES...')

        time.sleep(2)

        print('''
Nome: {}
Idade: {}
Produto: {}'''.format(nome, idade, remedio))
