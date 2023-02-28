#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da pessagem, cobrando R$ 0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

print('CALCULE O VALOR DA SUA VIAGEM COM O TRANSPORTE PÚBLICO.')

print('_' *31)

print('')

print('Qual a distância da sua viagem?')
viagem = float(input('KM: '))

print('')

if viagem <= 200:
    valor = viagem * 0.50
    print('Você irá pagar R${:.2f} '.format(valor))

else:
    taxa = viagem * 0.45

    print('Você irá pagar R${:.2f}'.format(taxa))

    print('')

    print('Tenha uma ótima viagem!')

print('_' *31)

print('')

print('------------ESSA PESQUISA FOI ÚTIL PRA VOCÊ?------------')

print('')

print('Digite (SIM) ou (NÃO) para nos ajudar a melhorar a página*')
resposta = str(input('- ')).upper()

if resposta == 'SIM':
    print('Obrigado pela colaboração.')

elif resposta == 'NÃO' or resposta == 'NAO':
    print('Indique algum ponto que podemos melhorar:')
    dica = str(input('- '))

    print('Obrigado pela colaboração.')

else:
    print('Tente novamente.')
