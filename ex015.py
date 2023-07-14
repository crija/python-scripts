 #Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 70% de desconto:
produtos = {'Cadeira gamer': 4.999, 'Sofá 4 lugares': 3.578, 'Cama com baú' : 2.679, 'Geladeira': 5.688, 'Mesa de jantar 6 lugares': 4.899}

informacoes = {}

def line():
    print('**********************************')

def espaco():
    print()

espaco()
print('PARABÉNS, VOCÊ ACABA DE GANHAR 70% DE DESCONTO EM QUALQUER PRODUTO DA LISTA ABAIXO!')
espaco()
line()
espaco()

for k, v in produtos.items():
    print(f'{k}: R${v}')

espaco()
line()
espaco()


valor = 0
while valor not in produtos.values():
    valor = float(input('Digite o valor do produto desejado: '))
    print('valor não encontrado')
    
else:
    desconto = valor - (valor * 70 /100)

    print('( De R${:.3f} por R${:.3f} )'.format(valor, desconto))
    espaco()
    print('Para que o desconto seja efetuado, cadastre-se agora mesmo!')
    espaco()

    print('INFORMAÇÕES:')

    espaco()
    informacoes['name'] = ''
    while informacoes['name'] == '':
        print('_' *30)
        informacoes['name'] = str(input('Digite seu nome: '))
        if informacoes['name'] == '':
            print('Campo obrigatório ^')

    else:
        informacoes['email'] = ''
        while informacoes['email'] == '':
            informacoes['email'] = input('Digite seu email:')
            if informacoes['email'] == '':
                print('Campo obrigatório ^')
                
        else:            
            informacoes['idade'] = int(input('Digite sua idade: '))

        print('_' *30)

        if informacoes['idade'] < 17:
            print('Cadastro não disponível para menores de 18 anos')

        else:
            espaco()
            for k, v in informacoes.items():
                print(f'{k}: {v}')

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
