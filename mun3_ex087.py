#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
#em seguida, mostre:
#Quantas pessoas foram cadastradas
#Uma listagem com as pessoas mais pesadas
#Uma listagem com as pessoas meis leves

lista = []
dados = []
res = ''
maior = menor = 0
p = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Quantos quilos você pesa? ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()

    res = str(input('Quer continuar?[s/n] ')).lower()
    if res == 'n':
        break
print(f'Os dados foram: {lista}')
print(f'{len(lista)} se cadastraram')
print(f'Pesos maiores: {maior}kg.')
for p in lista:
    if p[1] == maior:
        print(f'Nome: {p[0]}.')
print()
print(f'Peso menore: {menor}kg.')
for p in lista:
    if p[1] == menor:
        print(f'Nome: {p[0]}.')
print()
