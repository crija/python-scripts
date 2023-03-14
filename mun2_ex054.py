#Crie um programa que faça o computador jogar Jokenpô com você:
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PÔ')
sleep(2)

print('¨' * 30)

print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')

print('¨' * 30)

if computador == 0:

    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE!')

    elif jogador == 2:
        print('COMPUTADOR VENCEU')

    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCEU!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')

    elif jogador == 1:
        print('COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA!')
