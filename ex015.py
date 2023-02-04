 #Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:

print('Parabéns, você acaba de ganhar 70% de desconto em qualquer produto da lista abaixo!')
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
if valor != 4.999 and valor != 3.578 and valor != 2.670 and valor !=5.000 and valor != 4.899:
    print('NAO disponível')
else:
    desconto = valor - (valor * 70 /100)
    print('De R${:.5f} por R${:.3f}.'.format(valor, desconto))
    print('Para que o desconto seja efetuado, cadastre-se agora mesmo!')

    nome = input('Qual é seu nome completo? ')
if nome == '':
    print('Campo obrigatório ^')
else:
    gmail = input('Qual é seu gmail? ')

if gmail == '':
    print('Campo obrigatório ^')
else:
    idade = int(input('Quantos anos você tem? '))

if idade < 17:
    print('Cadastro não disponível para menores de 18 anos')
else:
    print('nome:{}, gmail:{} , idade:{} anos.'.format(nome, gmail, idade))
    print('Já está acabando!')
    print('Para manter sua conta segura digite seu nome e crie uma senha forte com caracteres, números e letras.')
    Nome = input('Digite apenas seu primeiro nome: ')
    senha = input('Crie uma senha de acesso: ')
    confirmar = input('Confirme sua senha: ')
if confirmar != senha:
        print('Senha incorreta:')
else:
    print('Tudo certo.')
    print('AGRADECEMOS A PREFERENCIA!')
