#Crie um programa que tenha uma função chamada voto()que vai receber como parâmetro o ano de nascimento de uma pessoa
#retornandoum valor literal indicando se uma pessoa tem voto NEGATIVO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano=0):
    if 2023 - ano < 18:
        return 'Não é obrigatório'

    elif 2023 - ano < 64 :
        return 'É obrigatório'
    
    elif 2023 - ano >= 65:
        return 'Opcional'

#programa principal
ano = int(input('Ano de nascimento: '))
if voto(ano)=='Não é obrigatório':
    print('Não é obrigatório')

elif voto(ano)=='É obrigatório':
    print('Voto Obrigatório')


elif voto(ano)=='Opcional':
    print('Voto Opcional')



