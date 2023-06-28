#Crie um programa que tenha uma função chamada voto()que vai receber como parâmetro o ano de nascimento de uma pessoa
#retornandoum valor literal indicando se uma pessoa tem voto NEGATIVO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano=0):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'Com {idade} o voto não é negado'

    elif idade - ano < 64 :
        return f'Com {idade} o voto é obrigatório'
    
    elif idade - ano >= 65:
        return f'Com {idade} o voto é opcional'

#programa principal
usuario = int(input('Qual ano você nasceu? '))
print(voto(usuario))