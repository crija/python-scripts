sabor = ['4 queijos', 'portuguesa', 'margarita', 'frango', 'brócolis', 'atum', 'escarola', 'toscana', 'vegetariana', 'coração', 'chocolate preto', 'prestigio', 'brigadeiro', 'nutella', 'sorvete']
adicional = {'cheddar': 4.25, 'maionese verde': 2.50, 'morango': 5.15, 'chocolate preto': 8.90}
borda = {'catupiry': 10.99, 'bombom': 15.90}
valor_pizza = {'P': 34.99, 'M': 42.99, 'G': 55.99}

print('Tamanho')
for i in valor_pizza.items():
    print(i)

escolher_tamanho = input('Escolha o tamanho: ')
if escolher_tamanho == 'P':
    print('Você pode escolher 3 sabores')
    for s in range(0, 3):
        escolher_sabor = input('Escolha o sabor: ')