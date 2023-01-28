#Faça um programa que some dois números quaisquer, subtraia o resultado, mostre seu tipo primitivo e pergunte se o resultado está certo:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 =int(input('Digite mais um número: '))

x = n1 + n2 - n3

print('O resultado é', x)

print(type(x))

f = input('O resultado {} está correto? '.format(x))

if f == 'sim':
    print('Tudo certo! ')

else:
    print('Tente novamente mais tarde! ')
