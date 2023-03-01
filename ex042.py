#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano =  int(input('Em qual ano você está? '))

a = ano / 400
res1 = a % b

c = ano / 4
res2 = ano % 4

d = ano / 100
res3 = ano % 100

if res1 == 0 or res2 == 0 and res3 != 0:

    print('{} é um ano bisseto.'.format(ano))

else:
    
    print('{} não é um ano bissexto.'.format(ano))
