#Faça um programa que tenha uma função chamada ficha()
#que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(n, g=0):
    g = 0
    if nome == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato'
    elif gols == '':
        return f'O jogador {n} fez {g} gol(s) no campeonato'
    else:
        return f'O jogador {n} fez {gols} gol(s) no campeonato'

#programa principal:
nome = str(input('Nome do jogador: '))
gols = str(input('Números de gols: '))
print(ficha(nome, gols))

