#Crie um programa que leia o nome e o preço de vários produtos. O programas deverá perguntar se o usuário vai continuar. No final, mostre:
#Qual é o total gasto na compra;
#Quantos produtos custam mais de R$ 1000;
#Qual é o nome do produto mais barato.
from time import sleep

menor = 0
produto = 0
c = 0
quantidade = 0
gasto = 0
maior1000 = 0
menornome = ''
maiornome = ''
listaprodutos = ''
valores = 0
lista = []

print('-='*10)
print('LOJA GASTE MENOS')
print('-='*10)

while c != 'N':

    nome = str(input('Digite o nome do produto: '))
    preço = int(input('Digite o preço do produto: '))
    c = str(input('Deseja continuar? [S/N]: ')).upper()

    lista.append(nome)

    quantidade += 1
    gasto += preço

    if quantidade == 1:
        maior = menor = preço

    else:
        if preço > maior:
            maior = preço
            maiornome = nome

        if  preço < menor:
            menor = preço
            menornome = nome

    if preço > 1000:
        maior1000 += 1

    if c == 'N':
        print('carregando...')



print('-------------- PRODUTOS ADICIONADOS A SUA SACOLA ---------------')
sleep(3)

print('Você adicionou {} produto na sua sacola com total de R${}.'.format(quantidade, gasto))
print('O produto de maior valor é {} com o valor de R${}.'.format(maiornome, maior))
print('O produto de menor valor é {} com o valor de R${}.'.format(menornome, menor))
print('Você adicionou {} produtos maiores de R$1000.'.format(maior1000))

print('CARRINHO:')

print('-'*15)

for lista in lista:
    print(lista)

print('-'*15)
