import csv
from pizza import *

flavors = ['4 queijos', 'portuguesa', 'margarita', 'frango', 'brócolis', 'atum', 'escarola', 'toscana', 'vegetariana', 'coração', 'chocolate preto', 'prestigio', 'brigadeiro', 'nutella', 'sorvete']

print('Tamanhos')
for t, f in PIZZA_VALUE.items():
    print(t, f)

size = str(input('Digite o tamanho escolhido: ')).upper()
match size:
    case 'P':
        print(f'valor: {PIZZA_VALUE[size]}')
        for i in flavors:
            print(i)
        print('Escolha 3 igredientes')
        for i in range(0, 3):
            p = str(input('Adicione um igrediente: '))

    case 'M':
        print(f'valor: {PIZZA_VALUE[size]}')
        for i in flavors:
            print(i)
        print('Escolha 4 igredientes')
        for i in range(0, 4):
            m = str(input('Adicione um igrediente: '))

    case 'G':
        print(f'valor: {PIZZA_VALUE[size]}')
        for i in flavors:
            print(i)
        print('Escolha 5 igredientes')
        for i in range(0, 5):
            g = str(input('Adicione um igrediente: '))


print('Bordas')
for b in LIST_EDGE:
    print(b)

edge = str(input('Escolha o recheio da borda: ')).lower()
print(f'valor: {LIST_EDGE[edge]}')

chosen_additional = str(input('Igrediente adicional? [yes or no]')).lower()
if chosen_additional == 'yes':
    for i in LIST_ADDITIONALS:
        print(i)

    chosen_additional = str(input('Escolha um igrediente: ')).lower()
    print(f'valor: {LIST_ADDITIONALS[chosen_additional]}')

pizza = Pizza(size, flavors, edge, chosen_additional)

with open("pizzaria/arquivo.csv", 'a', newline='') as arquivo:
    campos_head = ['tamanho', 'igredientes', 'borda', 'adicional', 'total']
    writer = csv.DictWriter(arquivo, fieldnames=campos_head, delimiter=';')

    if arquivo.tell() == 0:
        writer.writeheader()

    writer.writerow({
                        'tamanho': size,
                        'igredientes': flavors,
                        'borda': edge,
                        'adicional': chosen_additional,
                        'total': pizza.calculate_value(),
                    })
    arquivo.close()















