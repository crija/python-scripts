#Crie um programa que leia vários números inteiros
#O programa só vai parar quando o usuário digitar o valor 2
#No final, mostre quantos números foram digitados e a soma entre eles;

n = 0
cont = 0
soma = 0

while True:

    n = int(input('Digite um número: '))

    if n == 2:

        break

    cont += n
    soma += 1

print(f'Foram digitados {soma} números e a soma é {cont}.')
