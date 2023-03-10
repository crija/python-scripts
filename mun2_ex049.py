#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#O programa também devera mostrar o tempo que falta ou que passou do prazo.

print('ALISTAMENTO MILITAR')

print('Para o alistamento obrigatório é nescessário ter 18 a 24 anos.')

print('Qual é a sua idade?')
idade = int(input('- '))

if idade == 18:
    print('Você pode ser alistar.')
    print('Compareça a uma junta militar mais perto de você para mais informações.')

elif idade < 18:
    calculo = 18 - idade
    print('Você não pode se alistar!')
    print('Ainda faltam {} anos para você completar 18 anos.'.format(calculo))

elif idade > 18 and idade <= 24:
    calculo2 = idade - 18
    print('Você pode se alistar!')
    print('Você está {} anos atrasado para o alistamento.Procure a junta militar o mais rapido possível!'.format(calculo2))

elif idade > 24:
    calculo3 = idade - 18
    print('Você não pode mais se alistar!')
    print('Você excedeu o período de alistamento!')
