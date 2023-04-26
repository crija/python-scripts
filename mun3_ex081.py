#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectores preços, na sequência. No final, mostre uma lista de preços, organizando os dados em forma tabular;

from time import sleep

resposta = ''
lista = []
cont = 0
soma = 0

print('=-'*15)
print('LOJA DE MATERIAL ESCOLAR')
print('=-'*15)

while resposta != 'N':

    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    resposta = str(input('Deseja adicionar mais itens na sacola [S/N]? ')).upper()

    item = (produto, valor)
    lista.append(item)

    soma += valor
    cont += 1

print('')
titulo = 'LISTAGEM DE PREÇOS'
print(titulo.center(30, ))
print('_'*30)
print('carregando...')
sleep(3)
print(f'Você adicionou {cont} produto(s) na sacola')


for item in lista:

    produto = item[0]
    valor = item[1]

    print(f'{produto:.<30} R$ {valor}')
print(f'Total R${soma}')

print('_'*30)
