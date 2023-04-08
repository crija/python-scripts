#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até dez
#Seu programa deverá ler um número pelo teclado(entre 0-10) e mostrá-lo por extenso
num = 0

extenso = ('ZERO','UM', 'DOIS','TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ')


while True:

    num = int(input('Digite um número de 0 a 10: '))
    if num < 10:
        break
    print('Tente novamente')
    
print(f'Você digitou o número {extenso[num]}')
