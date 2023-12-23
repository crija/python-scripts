pizza_sizes = {'P:': '4 fatias', 'M:': '8 fatias', 'G:': '12 fatias'}
list_igredients = ['queijo', 'calabresa', 'carne', 'frango', 'brócolis', 'atum', 'cebola', 'presunto', 'molho vermelho']
list_additionals = {1:'cheddar' , 2:'maionese verde', 3:'batata palha', 4:'milho verde'}
chosen_igredients = []
chosen_additional = []

def igredients():
    print('Igredientes Disponíveis')
    for i in list_igredients:
        print(i)

print('Tamanhos')
for t, f in pizza_sizes.items():
    print(t, f)

choose_pizza_size = str(input('Digite o tamanho escolhido: ')).upper()

match choose_pizza_size:
    case 'P':
        igredients()
    case 'M':
        igredients()
    case 'G':
        igredients()

stop = ''
while stop != 'skip':
    escolha = str(input('Adicione um igrediente na pizza: '))
    chosen_igredients.append(escolha)
    print(f'{escolha} adicionado')
    stop = str(input('Para sair digite skip: '))

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

print('Igredientes adicionados')
for i in chosen_igredients:
    print(i)
print('Número dos adicionais')
for a in chosen_additional:
    print(a)




