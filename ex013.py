#Crie um programa que calcule o aumento e desconto de um valor (em porcentagem):

print()

titulo = 'NO PAGAMENTO A VISTA VOCÊ GANHA 5% DE DESCONTO:'

print(titulo.center(70))
print()

nome = input('Nome do produto desejado: ')
valor = float(input('Valor: '))

print(f'Valor a vista: R$ {valor - (valor * 5 / 100)}')
print('')
print('-' *70)
print('')
print('PARCELANDO EM 10x TEM ACRÉSCIMO DE 10% SOBRE O VALOR ATUAL:')

parcelar = str(input('Você deseja pagar em 10x? '))
if parcelar == 'sim':    

    print(f'Parcelando em até 10x você irá pagar: R$ {valor + (valor * 10 / 100)}')
    
else:
    print(f'{nome}: {valor - (valor * 5 / 100)}')
print('-' *70)