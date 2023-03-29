#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
p = 't'
s = 0
c = 0
maior = 0
menor = 0
while p != 'N':
    n = int(input('Digite um valor: '))

    if p != 'N':
        s = s + 1
        c = c + n
        m = c / s

        if s == 1:
            maior = menor = n

        else:
            if n > maior:
                maior = n
                
            if n < menor:
                menor = n

    p = str(input('Deseja continuar? [S/N]')).upper()

print('{} números foram digitados'.format(s))

print('A soma é {}'.format(c))

print('A média é {:.1f}'.format(m))

print('O maior é {}'.format(maior))

print('O menor é {}'.format(menor))
