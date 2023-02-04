#Crie um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor:

n = int(input('Digite qualquer número inteiro: '))

n1 = n - 1
n2 = n + 1

print('O antecessor de {} é {} e o seu sucessor é {}.'.format(n, n1, n2))
