from pizza import *

sabores = ['4 queijos', 'portuguesa', 'margarita', 'frango', 'brócolis', 'atum', 'escarola', 'toscana', 'vegetariana', 'coração', 'chocolate preto', 'prestigio', 'brigadeiro', 'nutella', 'sorvete']
adicionais = {'cheddar': 4.25, 'maionese verde': 2.50, 'morango': 5.15, 'chocolate preto': 8.90}
bordas = {'catupiry': 10.99, 'bombom': 15.90}
tamanhos = {'P': 34.99, 'M': 42.99, 'G': 55.99}

pizza = Pizza('', [], '')

print('Tamanho')
for i in tamanhos.items():
    print(i)

escolher_tamanho = input('Escolha o tamanho: ')
pizza.escolher_tamanho(escolher_tamanho)
print(pizza.tamanho)

print(sabores)
if pizza.tamanho == 'p':
    print('Você pode escolher 2 sabores')
    for s in range(0, 2):
        escolher_sabor = input('Escolha o sabor: ')
        pizza.escolher_sabor(escolher_sabor)

elif pizza.tamanho == 'm':
    print('Você pode escolher 3 sabores')
    for s in range(0, 3):
        escolher_sabor = input('Escolha o sabor: ')
        pizza.escolher_sabor(escolher_sabor)

else:
    print('Você pode escolher 4 sabores')
    for s in range(0, 4):
        escolher_sabor = input('Escolha o sabor: ')
        pizza.escolher_sabor(escolher_sabor)

print(pizza.sabores)

print('Borda')

print(bordas)
escolher_borda = input('Escolha a borda: ')
pizza.escolher_borda(escolher_borda)
print(pizza.borda)

pizza.valor_total()

