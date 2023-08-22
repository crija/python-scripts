from random import choice
import string
from time import sleep

while True:

    print('*** Gerador de senhas aleatórias ***')
    quantidade_caracter = 0

    while quantidade_caracter < 4:
        print('-'*53)
        print('Por questão de segurança escolha no mínimo 4 dígitos!')
        quantidade_caracter = int(input('Escolha a quantidade de dígitos da sua senha: '))
        print('*')

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''

    for i in range(quantidade_caracter):
        senha += choice(caracteres)

    print('Sua senha está sendo gerada. Aguarde!')
    sleep(3)
    print(f'senha: {senha}')
    print('Mantenha sua senha segura!')
    print('-'*53)

    escolha = str(input('Deseja gerar uma nova senha [sim/nao]? ')).lower()
    if escolha == 'sim':
        print('Aguarde...')
        sleep(2)
        print('')

    else:
        break