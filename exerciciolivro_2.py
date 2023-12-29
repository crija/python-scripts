pizza_sizes = {'P:': '4 fatias - R$34,99', 'M:': '8 fatias - R$42,99', 'G:': '12 fatias - R$55,99'}
list_igredients = ['queijo', 'calabresa', 'carne', 'frango', 'brócolis', 'atum', 'cebola', 'presunto', 'molho vermelho']
list_additionals = {1:'cheddar' , 2:'maionese verde', 3:'batata palha', 4:'milho verde'}
list_edge = ['catupiry', 'cheddar', 'morango', 'chocolate branco', 'bombom']
chosen_igredients = []
chosen_additional = []

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
        selecionar_adicional = str(input(f'Você escolheu {igrediente_adicional}. Escolher mais adicionais?[yes or no]: ')).lower()
        if selecionar_adicional == 'no':
            break

print('Tamanho')
print(f'{choose_pizza_size}')
print('Borda')
print(f'{add_edge}')
print('Igredientes adicionados')
for i in chosen_igredients:
    print(i)
print('Número dos adicionais')
for a in chosen_additional:
    print(a)





