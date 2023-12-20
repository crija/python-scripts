igredientes = []
adicional = {1:'cheddar' , 2:'maionese verde', 3:'batata palha', 4:'milho verde'}
adicionais_elcolhidos = []

sair = ''
while sair != 'quit':
    escolha = str(input('Adicione um igrediente na pizza: '))
    igredientes.append(escolha)
    print(f'{escolha} adicionado')
    sair = str(input('Para sair digite quit: '))

igrediente_adicional = str(input('Igrediente adicional? ')).lower()
if igrediente_adicional == 'sim':
    for k, v in adicional.items():
        print(k, v)

selecionar_adicional = ''
while selecionar_adicional != 'nao':
    numero_adicional = int(input('Digite o número do adicional escolhido: '))
    adicionais_elcolhidos.append(numero_adicional)
    selecionar_adicional = str(input(f'Você escolheu {numero_adicional}. Escolher mais adicionais?[y or no] (Para sair digite sair.): ')).lower()
    if selecionar_adicional == 'sair':
        break


print('Igredientes adicionados')
for i in igredientes:
    print(i)
print('Número dos adicionais')
for a in adicionais_elcolhidos:
    print(a)




