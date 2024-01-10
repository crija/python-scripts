import csv
from limiters import *

pizza_sizes = {'P:': '4 fatias - R$34,99', 'M:': '8 fatias - R$42,99', 'G:': '12 fatias - R$55,99'}
list_additionals = {1:'cheddar' , 2:'maionese verde', 3:'batata palha', 4:'milho verde'}
list_edge = ['catupiry', 'cheddar', 'morango', 'chocolate branco', 'bombom']

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

print('Se preferir sem borda digite (sem)')
add_edge = str(input('Escolha o recheio da borda: ')).lower()
if add_edge == 'sem':
    print('ok')

igrediente_adicional = str(input('Igrediente adicional? [yes or no]')).lower()
if igrediente_adicional == 'yes':
    for k, v in list_additionals.items():
        print(k, v)

    while igrediente_adicional != 'no':
        igrediente_adicional = int(input('Digite o número do adicional escolhido: '))
        chosen_additional.append(igrediente_adicional)
        selecionar_adicional = str(input(f'Você escolheu {igrediente_adicional}. Escolher mais adicionais?[yes or no]: ')).clower()
        if selecionar_adicional == 'no':
            break

with open("pizzaria/aquivo.csv", 'a', newline='') as arquivo:
    escrever = csv.writer(arquivo)
    for i in chosen_igredients:
        escrever.writerow([i])















