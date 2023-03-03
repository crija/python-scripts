#Criar um programa que rode o valor de um trasporte de classe economica, normal e alta:

print('Viagens interestaduais com o menor preço e maior conforto?')

print('')

print('NÃO PERCA TEMPO E GARANJA JÁ A SUA!')

print('')

print('*********** MAS CORRA QUE É POR TEMPO LIMITADO ***********')

print('Promoção imperdível para você!')

print('Deseja consultar a Promoção? ')

print('')

print('Digite (sim) ou (não)*')

pergunta = str(input('- ')).upper()

if pergunta == 'NAO' or pergunta == 'NÃO':
    print('Ok, temos outras opções de viagens para você.')

elif pergunta == '':
    print('Confira outras viagens semelhantes')

elif pergunta == 'SIM':
    print('')


    print('                      ----SUPER PROMOÇÃO DE CARNAVAL----      ')

    print('')

    print('OPÇÃO 1 :')

    print('Na compra de uma viagem com saída do (RS) para (SP) você ganha 15% de desconco na classe (normal).')

    print('')

    print('OPÇÃO 2 :')

    print('Na compra de uma viagem com saída de (SP) para (SC) você ganha 10% de desconto na classe (alta).')

    print('')

    print('Digite o número da opção escolhida. 1 ou 2:')
    opçao = int(input('- '))

    if opçao == 1 :

        valor = 679.56

        novo = valor - (valor * 15 / 100)

        print('O valor da viagem fora da Promoção é {:.2f}.'.format(valor))

        print('Com o desconto de 15% você pagará apenas {:.2f}'.format(novo))

        print('')

        compra = str(input('Deseja fazer essa compra? ')).upper()

        if compra == 'SIM':
            print('')

            print('Obrigada pela preferencia!')

        elif compra == 'NAO' or compra == 'NÃO':
            print('Temos outras opções de passagens para você! Da classe ecônomica à alta.')

    elif opçao == 2:

        valor = 787.78

        novo = valor - (valor * 10 / 100)

        print('O valor da viagem fora da Promoção é {:.2f}.'.format(valor))

        print('Com o desconto de 15% você pagará apenas {:.2f}'.format(novo))

        compra = str(input('Deseja fazer essa compra? ')).upper()

        if compra == 'SIM':
            print('Obrigada pela preferencia!')
            print('Temos outras opções de passagens para você! Da classe ecônomica à alta.')

        elif compra == 'NAO' or compra == 'NÃO':
            print('Temos  outras opções de passagens para você! Da classe ecônomica à alta.')
    else:
        print('Opçao {} não é considerada oferta de carnaval.Confira abaixo as viagens fora da promoção.'.format(opçao))

print('')

print('*VIAGENS*')

print('''-------------------------------------------------
                ORIGEM     X    DESTINO

(1)  São Paulo             X      Rio de Janeiro
(2)  Rio Grande do Sul     X      Santa Catarina
(3)  Bahia                 X      Minas Gerais
(4)  Ceará                 X      Tocantins
(5)  Rio de Janeiro        X      Paraná
------------------------------------------------- ''')

print('')

print('*VALORES*')

print('_' * 98)

print('       VIAGENS                         ECONÔMICA              NORMAL               ALTA')

print('')

print('São Paulo X Rio de Janeiro:            (1) R$ 497.68          (6) R$ 597.68       (11) R$ 697.68')
print('Rio Grande do Sul X Santa Catarina:    (2) R$ 389.99          (7) R$ 489.99       (12) R$ 589.99')
print('Bahia X Minas Gerais:                  (3) R$ 525.45          (8) R$ 625.45       (13) R$ 725.45')
print('Ceará X Tocantins:                     (4) R$ 634.15          (9) R$ 734.15       (14) R$ 834.15')
print('Rio de Janeiro X Paraná:               (5) R$ 575.67         (10) R$ 675.67       (15) R$ 775.67')

print('_' * 98)


eSP = 497.68
eRS = 389.99
eBH = 525.45
eCE = 634.15
eRJ = 575.67

nSP = 597.68
nRS = 489.99
nBH = 634.15
nCE = 734.15
nRJ = 675.67

aSP = 697.68
aRS = 589.99
aBH = 734.15
aCE = 834.15
aRJ = 775.67

print('Digite o número da classe escolhida: ')
viagem = int(input('- '))

if viagem != 1 and viagem != 2 and viagem != 3 and viagem != 4 and viagem != 5 and viagem != 6 and viagem != 7 and viagem != 8 and viagem != 9 and viagem != 10 and viagem != 11 and viagem != 12 and viagem != 13 and viagem != 14 and  viagem != 15:
    print('OPS... Viagem não disponível ')


elif viagem == 1:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: São Paulo')
    print('Destino: Rio de Janeiro')
    print('Classe: ECONÔMICA')
    print('Valor final: {}.'.format(eSP))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 2:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Rio Grande do Sul')
    print('Destino: Santa Catarina')
    print('Classe: ECONÔMICA')
    print('Valor final: {}.'.format(eRS))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 3:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Bahia')
    print('Destino: Minas Gerais ')
    print('Classe: ECONÔMICA')
    print('Valor final: {}.'.format(eBH))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 4:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Ceará')
    print('Destino: Tocantins  ')
    print('Classe: ECONÔMICA')
    print('Valor final: {}.'.format(eCE))
    print('')
    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 5:
    print('')
    print('CARREGANDO')
    print('')
    print('Origem: Rio de Janeiro ')
    print('Destino: Paraná  ')
    print('Classe: ECONÔMICA')
    print('Valor final: {}.'.format(eRJ))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 6:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: São Paulo ')
    print('Destino: Rio de Janeiro')
    print('Classe: NORMAL ')
    print('Valor final: {}.'.format(nSP))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 7:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Rio Grande do Sul')
    print('Destino: Santa Catarina')
    print('Classe: NORMAL')
    print('Valor final: {}.'.format(nRS))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 8:
    print('')
    print('CARREGANDO')
    print('')
    print('Origem: Bahia')
    print('Destino: Minas Gerais ')
    print('Classe: NORMAL')
    print('Valor final: {}.'.format(nBH))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 9:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Ceará')
    print('Destino: Tocantins  ')
    print('Classe: NORMAL')
    print('Valor final: {}.'.format(nCE))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 10:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Rio de Janeiro ')
    print('Destino: Paraná  ')
    print('Classe: NORMAL')
    print('Valor final: {}.'.format(nRJ))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

elif viagem == 11:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Rio de Janeiro ')
    print('Destino: São Paulo ')
    print('Classe: ALTA ')
    print('Valor final: {}.'.format(aRJ))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')


elif viagem == 12:
    print('')
    print('CARREGANDO')
    print('')
    print('Origem: Rio Grande do Sul')
    print('Destino: Santa Catarina')
    print('Classe: ALTA')
    print('Valor final: {}.'.format(aRS))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')


elif viagem == 13:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Bahia')
    print('Destino: Minas Gerais ')
    print('Classe: ALTA')
    print('Valor final: {}.'.format(aBH))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')


elif viagem == 14:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Ceará')
    print('Destino: Tocantins  ')
    print('Classe: ALTA')
    print('Valor final: {}.'.format(aCE))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')


elif viagem == 15:
    print('')
    print('CARREGANDO...')
    print('')
    print('Origem: Rio de Janeiro ')
    print('Destino: Paraná  ')
    print('Classe: ALTA')
    print('Valor final: {}.'.format(aRJ))

    print('')

    print('Sua passagem está sendo processada...')

    print('')

    print('OBRIGADA PELA PREFERERENCIA!')

else:
    print('OPS... Viagem não disponível.')
