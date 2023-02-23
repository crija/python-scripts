 #Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 70% de desconto:
print('')
print('PARABÉNS, VOCẼ ACABA DE GANHAR 70% DE DESCONTO EM QUALQUER PRODUTO DA LISTA ABAIXO!')

print('\n')

print('**********************************')

print('\n')

print('Cadeira gamer: R$4.999')
print('Sofá 4 lugares: R$3.578')
print('Cama com baú: R$2.670')
print('Geladeira: R$5.000')
print('Mesa de jantar 6 lugares: R$4.899')

print('\n')

print('**********************************')

print('\n')

valor = float(input('Digite um dos valores a cima: R$'))

print('\n')

if valor != 4.999 and valor != 3.578 and valor != 2.670 and valor !=5.000 and valor != 4.899:
    print('Valor não encontrado, tente novamente!')
else:
    desconto = valor - (valor * 70 /100)

    print('( De R${:.3f} por R${:.3f} )'.format(valor, desconto))

    print('')

    print('Para que o desconto seja efetuado, cadastre-se agora mesmo!')

    print('')

    print('INFORMAÇÕES:')

    print('')
    print('_' *30)
    print('nome*')
    nome = input('- ')

    if nome == '':
        print('Campo obrigatório ^')

    else:
        print('e-mail*')
        gmail = input('- ')

        if gmail == '':
            print('Campo obrigatório ^')
        else:
            print('Idade*')
            idade = int(input('- '))

            print('_' *30)

            if idade < 17:
                print('Cadastro não disponível para menores de 18 anos')
            else:
                print('')

                print('nome:{}, gmail:{} , idade:{} anos.'.format(nome, gmail, idade))

                print('')

                print('SEGURANÇA:')

                print('Para manter sua conta segura siga as instruções abaixo.')

                print('')

                nome = str(input('Digite apenas seu primeiro nome: '))

                if nome == '':
                    print('Preenchimento obrigatório!')
                else:
                    senha = input('Crie uma senha de acesso: ')

                    if senha == '' or senha == ' ':
                        print('Crie uma senha para manter suas informações seguras!')
                    else:
                        confirmar = input('Confirme sua senha: ')

                        if confirmar != senha:
                            print('Senha incorreta:')
                        else:
                            print('Tudo certo.')
                            print('AGRADECEMOS A PREFERENCIA!')
