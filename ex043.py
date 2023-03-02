#Faça um programa que leia dois números e mostre qual é o maior e qual é o menor

n1 = input('Digite um número: ')

n2 = input('Digite mais um número: ')

if n1 < n2:
    print('{} é menor que {}.'.format(n1, n2))

elif n1 > n2:
    print('{} é maior que {}.'.format(n1, n2))

elif n1 == n2:
    print('{} e {} tem o mesmo valor.'.format(n1, n2))
