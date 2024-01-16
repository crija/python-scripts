final_value = []
pizza_value = [34.99, 42.99, 55.99]
list_igredients = ['4 queijos', 'portuguesa', 'margarita', 'frango', 'brócolis', 'atum', 'escarola', 'toscana', 'vegetariana', 'coração', 'chocolate preto', 'prestigio', 'brigadeiro', 'nutella', 'sorvete']
chosen_flavor = []

def igredients_pizza_p():
    print(f'valor: {pizza_value[0]}')
    final_value.append(pizza_value[0])
    for i in list_igredients:
        print(i)
    print('Escolha 3 igredientes')
    for i in range(0, 3):
        p = str(input('Adicione um igrediente: '))
        chosen_flavor.append(p)

def igredients_pizza_m():
    print(f'valor: {pizza_value[1]}')
    final_value.append(pizza_value[1])
    for i in list_igredients:
        print(i)
    print('Escolha 4 igredientes')
    for i in range(0, 4):
        m = str(input('Adicione um igrediente: '))
        chosen_flavor.append(m)

def igredients_pizza_g():
    print(f'valor: {pizza_value[2]}')
    final_value.append(pizza_value[2])
    for i in list_igredients:
        print(i)
    print('Escolha 5 igredientes')
    for i in range(0, 5):
        g = str(input('Adicione um igrediente: '))
        chosen_flavor.append(g)