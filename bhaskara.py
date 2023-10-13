print('Bhaskara')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b**2)-4*a*c
print(f'Valor de Delta: {delta}')

raiz = (delta ** (1/2))

x_mais = ((-b) + (raiz)) / (2*a)
print(f'Valor de X1: {x_mais}')

x_menos = ((-b) - (raiz)) / (2*a)
print(f'Valor de X2: {x_menos}')
