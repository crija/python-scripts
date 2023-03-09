#Escreva programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar:
#o valor da casa;
#o salário do comprador;
#em quanotos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[2;30;47m Fazer um empréstimo para compra da casa própria.\033[m')

casa = float(input('\033[3;37m Qual o valor da casa que você deseja comprar? R$ \033[m'))

salário = float(input('\033[3;37m Qual é o valor da sua renda mensal? R$\033[m'))

tempo = int(input('\033[3;37m Em quantos anos você deseja pagar? \033[m'))

meses = tempo * 12

prestação = casa / meses

if prestação > salário * 0.3:

    print('')

    print('\033[4;31m Seu empréstimo não foi aprovado.\033[m')

    print('')

else:

    print('')

    print('\033[4;34m Seu empréstimo foi aprovado.\033[m')

    print('')

    print('\033[1;37m O valor da prestação mensal é:\033[m \033[1;31mR${:.2f}\033[m'.format(prestação))

print('\033[1;37m Valor da casa: R$\033[0;33m{:.3f}\033[m'.format(casa))

print('\033[1;37m Sua renda mensal: R$ \033[0;33m{:.3f}\033[m'.format(salário))

print('\033[1;37m Quantos anos você irá pagar: \033[0;33m{}\033[m'.format(tempo))
