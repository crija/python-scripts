import csv
from limiters import *

additionals_value = [4.25, 2.50, 5.15, 8.90,]
edge_value = [10.99, 15.90, 0]
pizza_sizes = {'P:': '4 fatias', 'M:': '8 fatias', 'G:': '12 fatias'}
list_additionals = ['cheddar', 'maionese verde', 'morango', 'chocolate preto']
list_edge = ['catupiry', 'bombom']
chosen_additional = []

print('Tamanhos')
for t, f in pizza_sizes.items():
    print(t, f)

choose_pizza_size = str(input('Digite o tamanho escolhido: ')).upper()
match choose_pizza_size:
    case 'P':
        igredients_pizza_p()
    case 'M':
        igredients_pizza_m()
    case 'G':
        igredients_pizza_g()

print('Bordas')
for b in list_edge:
    print(b)

add_edge = str(input('Escolha o recheio da borda: ')).lower()

if add_edge == list_edge[0]:
    final_value.append(edge_value[0])
elif add_edge == list_edge[1]:
    final_value.append(edge_value[1])
else:
    final_value.append(edge_value[2])

igrediente_adicional = str(input('Igrediente adicional? [yes or no]')).lower()
if igrediente_adicional == 'yes':
    for i in list_additionals:
        print(i)

    while igrediente_adicional != 'no':
        igrediente_adicional = str(input('Digite o nome do adicional escolhido: ')).lower()
        chosen_additional.append(igrediente_adicional)

        match igrediente_adicional:
            case 'cheddar':
                final_value.append(additionals_value[0])
            case 'maionese verde':
                final_value.append(additionals_value[1])
            case 'morango':
                final_value.append(additionals_value[2])
            case 'chocolate preto':
                final_value.append(additionals_value[3])

        selecionar_adicional = str(input(f'Você escolheu {igrediente_adicional}. Escolher mais adicionais?[yes or no]: ')).lower()

        if selecionar_adicional == 'no':
            break

with open("pizzaria/arquivo.csv", 'a', newline='') as arquivo:
    campos_head = ['tamanho', 'igredientes', 'borda', 'adicional', 'total']
    writer = csv.DictWriter(arquivo, fieldnames=campos_head, delimiter=';')

    if arquivo.tell() == 0:
        writer.writeheader()

    writer.writerow({
                        'tamanho': choose_pizza_size,
                        'igredientes': chosen_flavor,
                        'borda': add_edge,
                        'adicional': chosen_additional,
                        'total': sum(final_value),
                    })
    arquivo.close()















