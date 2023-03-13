#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimenro de um atleta e mostre sua categoria , de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 30 anos: SÊNIOR
#Acima: MASTER

print('Para saber a qual categoria você pertence digite o ano do seu nascimento:')

nascimento = int(input('- '))

if nascimento >= 2014:
     print('Você pertence a categoria MIRIM.')

elif nascimento >= 2009:
    print('Você pertence a catertence a categoria INFANTIL.')

elif nascimento >=2003:
    print('Você pertence a categoria JUNIOR.')

elif nascimento >= 1993:
    print('Você pertence a categoria SÊNIOR.')

elif nascimento < 1993:
    print('Você pertence a categoria MASTER.')
