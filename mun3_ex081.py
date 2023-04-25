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
print('LISTAGEM DE PREÇOS')
print('_'*30)
print('carregando...')
sleep(3)

for item in lista:

    produto = item[0]
    valor = item[1]

    print(f'{produto}.............{valor}')
print(f'Total {soma}')
print(f'Você adicionou {cont} produtos na sacola')

print('_'*30)
