#App_aluguel de carro.

#O app vai conter: cidade de retirada, porte do carro, cor, data de retirada, data de devolução, promoção.

#Passar por todo o processo de cadastro: nome, idades +18, gmail, cpf, cnh.

#Aparecer todo o resultado, e se o usuário está apto para o aluguel.


#dicionários, título e subtítulo.
necessidades = {}
cadastro = {}
titulo = 'ALUGUEL DE CARROS DA SUA PREFERÊNCIA!'
cadastro2 = 'CADASTRE-SE'

#parte 1 do projeto: título centralizado.
print('')
print(titulo.center(50))

#laço de repetição comparando suas chaves do dicinário 'necessarios'.
while ['dia_devolução'] < ['dia_retirada']:

#indicandor de campo obrigatório.
    print()
    print('''campo obrigatório*''')
    print('_' * 50)

#perguntas para o usuário (que serão armazenadas no dicionário 'necessarios')
    necessidades['cidade_retirada'] = str(input('Cidade que deseja retirar o veículo: '))
    necessidades['dia_retirada'] = int(input('Dia de retirada: '))
    necessidades['dia_devoluçao'] = int(input('Dia de devolução: '))

#divisão do campo.
    print('_' * 50)

#condicional(1) comparando as duas chaves do laço de repetição.
    if necessidades['dia_devoluçao'] < necessidades['dia_retirada']:
        print()

#função criada para organização (explica para o usuário como deve responder a pergunta anterior, caso ele tenha respondido errado).
        def defin(msg):
            print(len(msg)*'-')
            print(msg)
            print(len(msg)*'-')
        defin('Por favor, escolha o dia da devolução de acordo com o dia da retirada!')
        defin('''ex: 
            Dia retirada: 04
            Dia devolução: 05 ''')

#linha em branco para manter a organização.
        print()

#fechamento da condicional(1), (começando um novo campo de pergunta)
    else:       
        print()

#mostrando para o usuário que não é obrigatório responder o campo a seguir.
        print('''campo opcional*''')
        print('_' * 50)

        necessidades['porte'] = str(input('Porte desejável: G, M, P: '))
        necessidades['cor'] = str(input('Cor de preferência: '))

        print('_' * 50)

#printar o dicionário 'necessidades' com todas as informações do pedidas para o usuário (as perguntas obrigatórias), as perguntas que o usuário escolher não responder estarão em branco, mostrando somente a chave.
        print(necessidades)
        print()

#subtítulo, definido no topo do código.
        print(cadastro2.center(50))

        print('''campo obrigatório*''')
        print('_' * 50)

#parte 2 do projeto: usando novo dicionário definido no topo do código como 'cadastro'. Esse dicionário vai conter todas os dados do usuário.
        cadastro['nome'] = str(input('Nome: '))
        cadastro['idade'] = int(input('Idade: '))

#condicional(2) para permitir o aluguel apenas para usuários 18+.
        if cadastro['idade'] >= 18:
            cadastro['cpf'] = int(input('CPF: '))
            cadastro['cnh'] = int(input('Número da CNH : '))
            cadastro['gmail'] = str(input('Gmail: '))
            print('_' * 50)

#printando o dicionário 'cadastro'.
            print(cadastro)
            
#fechamento da condicional(2), (não permitindo o aluguel para usuários com menos de 18 anos). Parando o código.
        else:
            print(f"{cadastro['nome']}, você não possui a idade minima para alugar uma carro")
            break
    

        





