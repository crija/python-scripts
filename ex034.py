#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A:

'''frase = str(input('Digite uma frase: '))

ndv = 0

for letter in frase :
    if letter == 'a' or letter == 'A' :
        ndv = ndv + 1

print('A letra A repete {}:'.format(ndv))'''

frase = str(input('Digite uma frase: ')).upper()

print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
