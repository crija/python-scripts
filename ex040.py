#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

print('Digite um número inteiro.')
n = int(input(''))

resto =  n % 2

if resto == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')
