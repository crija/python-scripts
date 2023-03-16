#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DA CONVERÇÃO:
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Digite um número para ser convertido em BINÁRIO ou OCTAL ou HEXADECIMAL: '))

print('''Escolha um dos conversores:
[1] Para BINÁRIO
[2] para OCTAL
[3] Para HEXADECIMAL
''')

escolha = int(input('- '))

if escolha == 1:
    print('{} convertido em BINÁRIO é {}.'.format(num, bin(num)[2:]))

elif escolha == 2:
    print('{} convertido em OCTAL é {}.'.format(num, oct(num)[2:]))

elif escolha == 3:
    print('{} convertido em  HEXADECIMAL é {}.'.format(num, hex(num)[2:]))

else:
    print('Opção não identificada.')
