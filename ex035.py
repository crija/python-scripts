#Faça um programa que leia uma frase pelo teclado e mostre:
#Em que posição a letra A aparece pela primeira vez:

frase = str(input('Digite uma frase: ')).upper()

print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
