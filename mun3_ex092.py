#Crie um programa onde 4 jogadores joguem um dado e tenham resualtados aleatórios.
#Guarde esses resultados em um dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random 
from time import sleep

organizar = []

jogadores = {'Jogador1', 'Jogador2', 'Jogador3', 'Jogador4'}


for c in jogadores:
    print(f'{c}: {random.randint(1, 7)}')
    sleep(2)