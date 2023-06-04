#Crie um programa que gerencie o aproveitamento de um jogador de futebol;

#O programa vai ler o nome do jogador e quantas partidas ele jogou;

#Depois vai ler a quantidade de gols feitos em cada partida;

#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from time import sleep

aproveitamento = {}
soma = 0 
tot = 0
lista = []
final = {}

aproveitamento['Nome'] = str(input('Nome do jogador: '))
aproveitamento['Jogos'] = int(input(f"Quantas partidas {aproveitamento['Nome']} jogou? "))

for c in range(0, aproveitamento['Jogos']):
    quantidade_gols = int(input(f'Quantidade de gols na partida {c+1}: '))
    soma = soma + quantidade_gols
    aproveitamento['Total_gols'] = soma

    lista.append(quantidade_gols)
aproveitamento['Gols'] = lista

print('Aguarde...')
print('')
sleep(3)
print('RESULTADO:')
print('*'*25)
for k, i in aproveitamento.items():
    print(f'{k}: {i}')
print('*'*25)

print(f"{aproveitamento['Nome']} jogou {aproveitamento['Jogos']} partidas.")

for i, v in enumerate(lista):
    print(f'Na partida {i+1} {aproveitamento["Nome"]} fez {v} gols.')


    
