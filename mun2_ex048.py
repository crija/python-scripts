#Escreva um programa que leia dois múmeros inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print('Digite um número.')
n1 = int(input('- '))

print('Digite mais um número.')
n2 = int(input('- '))

if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))

elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))

elif n1 == n2:
    print('{} é igual a {}'.format(n1, n2))
