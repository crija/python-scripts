#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#A vista dinheito/ cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

produto = float(input('Qual o valor do produto? '))

print('''
1) A vista dinheito/ cheque: 10% de desconto
2) À vista no cartão: 5% de desconto
3) Em até 2x no cartão: preço normal
4) 3x ou mais no cartão: 20% de juros
''')

desconto1 = produto - (produto * 10 / 100)
desconto2 = produto - (produto * 5 / 100)
juros = produto + (produto * 20 / 100)


pagamento = int(input('Digite o número da forma de pagamento que você deseja: '))

if pagamento == 1:
    print('Total: {:.2f}'.format(produto))
    print('Valor final: {:.2f}'.format(desconto1))

elif pagamento == 2:
    print('Total: {:.2f}'.format(produto))
    print('Valor final: {:.2f}'.format(desconto2))

elif pagamento == 3:
    print('Valor final: {:.2f}'.format(produto))

elif pagamento == 4:
    print('Total: {:.2f}'.format(produto))
    print('Valor final: {:.2f}'.format(juros))
