#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, crie duas listas extras que vão conter apenas os valores pares pares e os valores impares digitados, respectivamenente
#Ao final, mostre o conteúdo das três listas geradas
res = ''
total = []
pares = []
impares = []
while res != 'n':
    n = int(input('Digite um número: '))
    res = input('Deseja continar?[s/n] ').lower()
    if res != 'n':
        print('')
    total.append(n)
total.sort()
for n in total:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Os valores digitados foram {total}')
print(f'Os números pares são {pares}')
print(f'Os númeos impares são {impares}')
