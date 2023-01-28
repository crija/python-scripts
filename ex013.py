#Crie um programa que calcule o aumento e desconto de um valor (em porcentagem):

print('NO PAGAMENTO A VISTA VOCÊ GANHA 5% DE DESCONTO:')

produto = float(input('Digite o valor do produto desejado para fazermos a simulação: R$'))
novo = produto - (produto * 5 / 100)

print('No pagamento a vista você vai pagar apenas R${:.2f}.'.format(novo))
print('')
print('________________________________________________')
print('')
print('PARCELANDO EM ATÉ 10* TEM ACRÉSCIMO DE 10% SOBRE O VALOR ATUAL:')

produto = float(input('Digite o valor do produto desejado para fazermos a simulação: R$'))
novo = produto + (produto * 10 / 100)

print('Parcelando em até 10* você irá pagar R${:.2f}:'.format(novo))
