print('Remédios ainda em estoque:')
print('¨'* 15)
print('''
Tilenol
Patanol
Ecofilm
camomila
Paracetamol
''')
print('¨'* 15)

remedio = str(input('Qual das opções você deseja? ')).split()

if remedio == 'Tilenol'  or remedio == 'Patanol':

    print('{} é indicado apenas para pessoas com mais de 18.'.format(remedio))

    idade = int(input('Quantos anos você tem? '))

    if idade < 18:

        print('{} NÃO é recomendado para menor de idade.'.format(remedio))

elif idade >= 18:

    nome = str(input('Qual é seu nome? '))

    print('Cliente: {}'.format(nome))

elif remedio != 'Tilenol' or remedio != 'Patanol':

    nome = str(input('Qual é seu nome? '))

    print('cliente: {}'.format(nome))






elif remedio == 'Ecofilm' or remedio == 'Camomila' or remedio == 'Paracetamol':
    print()
