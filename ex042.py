#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano =  int(input('Em qual ano você está? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    
    print('{} é um ano bisseto.'.format(ano))

else:

    print('{} não é um ano bissexto.'.format(ano))
