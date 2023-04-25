#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectores preços, na sequência. No final, mostre uma lista de preços, organizando os dados em forma tabular;
resposta = ''
lista = []
print('=-'*15)
print('LOJA DE MATERIAIS ESCOLAR')
print('=-'*15)
while resposta != 'N':
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    resposta = str(input('Deseja adicionar mais itens na sacola [S/N]? ')).upper()
    item = (produto, valor)
    lista.append(item)
print('')
print('LISTAGEM DE PREÇOS')
print('_'*30)
for item in lista:
    produto = item[0]
    valor = item[1]
    print(f'{produto}.............{valor}')
print('_'*30)
