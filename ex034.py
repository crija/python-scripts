#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A:

frase = str(input('Digite uma frase: '))

nv = 0

for letter in frase :
    if letter == 'a' or letter == 'A' :
        nv = nv + 1

print('A letra A repete {}:'.format(nv))
