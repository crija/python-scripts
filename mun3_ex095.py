#Crie um programa que gerencie o aproveitamento de um jogador de futebol;

#O programa vai ler o nome do jogador e quantas partidas ele jogou;

#Depois vai ler a quantidade de gols feitos em cada partida;

#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#APRIMORAR DESAFIO:

#=>Para que funciona com vários jogadores;
#=>com um sistema de validação de detalhes do aproveitamento de cada jogador.

from time import sleep

res = ''
soma = 0 
tot = 0
lista = []
final = {}
nomes = {}
jogos = {}
gols = {}
lista2 = []

while True:
    nomes['Nome'] = str(input('Nome do jogador: '))
    jogos['Jogos'] = int(input(f"Quantas partidas {nomes['Nome']} jogou? "))
    for p in range(0, jogos['Jogos']):
        gols['Gols'] = int(input(f'Quantos gols na partida {p + 1}?'))
    
    res = str(input('deseja continuar? '))
    if res == 'n':
        break
        
lista2.append(nomes)
print(nomes)










