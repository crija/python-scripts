#Crie um programa que tenha uma função chamada voto()que vai receber como parâmetro o ano de nascimento de uma pessoa
#retornandoum valor literal indicando se uma pessoa tem voto NEGATIVO, OPCIONAL ou OBRIGATÓRIO nas eleições.

import datetime

def voto(ano=0):
    
    if s < 18:
        return 'Não é obrigatório'

    elif s - ano < 64 :
        return 'É obrigatório'
    
    elif s - ano >= 65:
        return 'Opcional'

#programa principal
ano = int(input('Ano de nascimento: '))

s = 2023 - ano

if voto(ano)=='Não é obrigatório':
    print(f'Com {s} anos o voto não é obrigatório')

elif voto(ano)=='É obrigatório':
    print(f'Com {s} anos o voto é obrigatório')

elif voto(ano)=='Opcional':
    print(f'Com {s} anos o voto é opcional')



