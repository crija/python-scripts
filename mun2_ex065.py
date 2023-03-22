

#Escrever um programa que leia a opção desejada do cliente,

import time

print('Remédios ainda em estoque:')
print('¨'* 15)
print('''
Tilenol
Patanol
''')
print('¨'* 15)

remedio = str(input('Qual das opções você deseja? ')).lower()

if remedio == (''):

    print('preencha o campo a cima:')

elif remedio == 'tilenol' or remedio == 'patanol':

    nome = str(input('Qual seu nome? '))

    if nome == (''):

        print('Nome é obrigatório:')

    else:

        idade = int(input('Quantos anos você tem? '))

        if idade == (''):

            print('Idade é obrigatório:')

        elif idade < 18:

# especifique se o remedio escolhido é recomendado para a idade do cliente ou nao,

            print('{} NÃO é recomendado para menor de idade.'.format(remedio))

            print('A venda de {} não é autorizada para menores de 18 anos'.format(remedio))

            print('Compareça a loja mais próxima com um adulto responsável para a compra.')

        else:

            if idade >= 18:

                print('CARREGANDO INFORMAÇÕES...')

                time.sleep(2)

                print('''
Nome: {}
Idade: {}
Produto: {}'''.format(nome, idade, remedio))

else:
    print('erro')
