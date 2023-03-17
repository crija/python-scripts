#Desenvolva um programa que leia seis números inteiros

soma = 0
contador = 0

for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))

# mostre a soma apenas daqueles que forem pares

    if n % 2 == 0:
        contador = contador + 1
        soma = soma + c

print('Você informou {} valores PARES e a soma foi {}'.format(contador, soma))

#Se o valor digitado for impar, desconsidere-o.
