#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectores preços, na sequência. No final, mostre uma lista de preços, organizando os dados em forma tabular;
resposta = ''
lista = []

while resposta != 'N':
    produto = str(input('Digite o nome do produto desejado: '))
    valor = float(input('valor que deseja pagar: '))
    resposta = str(input('Deseja continuar [S/N]? ')).upper()
    item = (produto, valor)
    lista.append(item)

for item in lista:
    produto = item[0]
    valor = item[1]
    print(f'{produto}.............{valor}')
