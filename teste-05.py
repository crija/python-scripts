#Faça um sintema que some dois números aleatórios e mostre se é < ou > que 50:

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
soma = a + b
if soma < 50:
    print('A soma de {} + {} é menor que 50!'.format(a, b))
else:
    print('A soma de {} + {} é maior que 50!'.format(a, b))
