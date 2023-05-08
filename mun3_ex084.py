#Crie um programa que vai ler vários números e colocar em uma lista
#Quantos números foram digitados
#A lista de valores, ordenada de forma decrescente
#Se o valor 5 foi digitado e se está ou não na lista
r = 0
lista = []

while r != 'N':
    n = int(input('\033[1;32m Digite um número:\033[m '))
    r = input('Deseja continuar? [s/n] ').upper()
    if r != 'N':
        print('*')
    lista.append(n)
lista.sort(reverse = True)
print('\033[1;33m+=\033[m'*25)
print(f'Foram digitados \033[3;35m{len(lista)}\033[m números')
print(f'Os valores digitados de forma decrescente são \033[3;35m{lista}\033[m')
if 5 in lista:
    print('O número \033[3;35m5\033[m está na lista')
else:
    print('O número \033[3;35m5\033[m \033[4;31mnão\033[m foi encontrado')
print('\033[1;33m+=\033[m'*25)
a = str(input('Deseja acrescentar o número 5 na lista? [s/n] ')).lower()
if a == 's':
    lista.append(5)
print(lista)
if a != 's':
    print('ok')
