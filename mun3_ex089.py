#Faça um programa que ajude o jogador da mega sena a criar palpites
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e e 60 para cada jogo,
#Cadastrando tudo em uma lista completa

from random import randint
from time import sleep

lista = []
n = []
sorte = '\033[1;33mBOA SORTE\033[m'

print('*'*30)
print('\033[1;34mGERAR NÚMEROS PARA A MEGA SENA\033[m')
print('*'*30)

quant = int(input('Quantos jogos você deseja gerar? '))
tot = 1
while tot <=  quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    n.append(lista[:])
    lista.clear()
    tot += 1

print(f'\033[2;32m-------Gerando {quant} jogos-------\033[m')

for i, l in enumerate(n):
    print(f'Jogo {i+1}): {l}')
    sleep(1)

print(sorte.center(40, '<'))
