tamanho = {'P:': '4 fatias', 'M:': '8 fatias', 'G:': '12 fatias'}
igredientes_dis = ['queijo', 'calabresa', 'carne', 'frango', 'brócolis', 'atum', 'cebola', 'presunto', 'molho vermalho']
adicional = {1:'cheddar' , 2:'maionese verde', 3:'batata palha', 4:'milho verde'}
adicionais_escolhidos = []

def igredientes():
    print('Igredientes Disponíveis')
    for i in igredientes_dis:
        print(i)

print('Tamanhos')
for t, f in tamanho.items():
    print(t, f)

escolher_tamanho = str(input('Digite o tamanho escolhido: ')).upper()

match escolher_tamanho:
    case 'P':
        igredientes()
        p = str(input('Escolha até 3 iguedientes: '))
    case 'M':
        igredientes()
        m = str(input('Escolha até 4 iguedientes: '))
    case 'G':
        igredientes()
        g = str(input('Escolha até 5 igredientes: '))

'''
stop = ''
while stop != 'skip':
    escolha = str(input('Adicione um igrediente na pizza: '))
    igredientes.append(escolha)
    print(f'{escolha} adicionado')
    stop = str(input('Para sair digite skip: '))

igrediente_adicional = str(input('Igrediente adicional? ')).lower()
if igrediente_adicional == 'sim':
    for k, v in adicional.items():
        print(k, v)

selecionar_adicional = ''
while selecionar_adicional != 'nao':
    numero_adicional = int(input('Digite o número do adicional escolhido: '))
    adicionais_escolhidos.append(numero_adicional)
    selecionar_adicional = str(input(f'Você escolheu {numero_adicional}. Escolher mais adicionais?[y or no] (Para sair digite sair.): ')).lower()
    if selecionar_adicional == 'sair':
        break


print('Igredientes adicionados')
for i in igredientes:
    print(i)
print('Número dos adicionais')
for a in adicionais_escolhidos:
    print(a)

'''


