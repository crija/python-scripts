#Faça um programa em python que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

('''n = int(input('Informe um número: '))
print('Analisando o número {}...'.format(n))

#Extraindo a unidade
unidade = n % 10

#Eliminando a unidade de nosso número
n = (n - unidade) / 10

#Extraindo a dezena
dezena = n % 10

#Eliminando a dezena do número originaol, fica a centena
n = (n - dezena) / 10
centena = n

#Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))''')

n = int(input('Informe um número: '))
print('Analisando o número {}...'.format(n))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unidade: {}, dezena: {}, centena: {}, milhar: {}.'.format(u, d, c, m))
