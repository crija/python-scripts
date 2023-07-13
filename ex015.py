 #Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 70% de desconto:
produtos = {'Cadeira gamer': 'R$4.999', 'Sofá 4 lugares': 'R$3.578', 'Cama com baú' : 'R$2.670', 'Geladeira': 'R$5.000', 'Mesa de jantar 6 lugares': 'R$4.899'  }

def lin():
    print('**********************************')

def espaco():
    print()

espaco()
print('PARABÉNS, VOCẼ ACABA DE GANHAR 70% DE DESCONTO EM QUALQUER PRODUTO DA LISTA ABAIXO!')
espaco()
lin()
espaco()

for k, v in produtos.items():
    print(f'{k}: {v}')

espaco()
lin()
espaco()


valor = 0
while valor != 4.999 and valor != 3.578 and valor != 2.670 and valor !=5.000 and valor != 4.899:
    valor = float(input('Digite um dos valores a cima: R$'))
else:
    desconto = valor - (valor * 70 /100)

    print('( De R${:.3f} por R${:.3f} )'.format(valor, desconto))
    espaco()
    print('Para que o desconto seja efetuado, cadastre-se agora mesmo!')
    espaco()

    print('INFORMAÇÕES:')

    espaco()
    name = ''
    while name == '':
        print('_' *30)
        name = str(input('Digite seu nome: '))
        if name == '':
            print('Campo obrigatório ^')

    else:
        email = ''
        while email == '':
            email = input('Digite seu email:')
            if email == '':
                print('Campo obrigatório ^')
                
        else:            
            idade = int(input('Digite sua idade: '))

            print('_' *30)

            if idade < 17:
                print('Cadastro não disponível para menores de 18 anos')

            else:
                espaco()
                print('nome:{}, gmail:{} , idade:{} anos.'.format(name, email, idade))
                espaco()
                print('SEGURANÇA:')

                print('Para manter sua conta segura siga as instruções abaixo.')
                espaco()

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
