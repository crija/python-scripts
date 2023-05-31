#update previous file.  

from random import randint
from time import sleep
from operator import itemgetter


players = {
            'player1': randint(1, 6),
            'player2': randint(1, 6),
            'player3': randint(1, 6),
            'player4': randint(1, 6)
}

ranking = []

for k, v in players.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
#organizar a tabela de vencedores(formato decrescente do dicionario)

print('')
print('=-'*6)

print('**RANKING**')
for k, v in ranking:
    print(f' {k}: {v}')

print('=-'*6)
