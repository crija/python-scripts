#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla;
#no final mostre:
#Quantas vezes aperece o valor 9;
#Em que posição foi digitado o primeiro valor 3;
#Quais foram os números pates.
cont = 0
soma = 0


n1 = int(input('Digite um número: '))
n2 = int(input('Digiten mais um número: '))
n3 =  int(input('Digiten mais um número: '))
n4 =  int(input('Digiten mais um número: '))

lista = (n1, n2, n3, n4)

print(f'Os números digitados foram{lista}')

print(f'O número 9 aparece {lista.count(9)} vez(es)')

print(f'O primeiro valor 3 digitado está na posição {(lista.index(3)+1)}')

print('Os números pares são ', end='')

for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
