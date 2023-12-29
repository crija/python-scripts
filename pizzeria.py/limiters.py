from main import list_igredients
from main import chosen_igredients

def igredients_pizza_p():
    for i in list_igredients:
        print(i)
    print('Escolha 3 igredientes')
    for i in range(0, 3):
        p = str(input('Adicione um igrediente: '))
        chosen_igredients.append(p)

def igredients_pizza_m():
    for i in list_igredients:
        print(i)
    print('Escolha 4 igredientes')
    for i in range(0, 4):
        m = str(input('Adicione um igrediente: '))
        chosen_igredients.append(m)

def igredients_pizza_g():
    for i in list_igredients:
        print(i)
    print('Escolha 5 igredientes')
    for i in range(0, 5):
        g = str(input('Adicione um igrediente: '))
        chosen_igredients.append(g)