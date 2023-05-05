#Crie um programa onde o usuário possa digitar cinco valores numéricos
#cadastre-os em uma lista,já na posiçao correta de inserção (sem usar o sort())
#No final, mostre a lista ordenada na tela

lista = []

for c in range(0, 5):

    n = int(input('Digite um valor: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print(f'Os números digitados foram {lista}')
