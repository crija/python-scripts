#Crie um programa que leia a ano idade de sete pessoas. No final, mostre quantas pessoas ainda são de menor:
soma = 0
cont = 0
for c in range(1, 8):
    idade = int(input('qual a idade da pessoa {}? '.format(c)))
    if idade < 18:
        soma = soma + 1
print('Das {} pessoas {} são MENORES de idade'.format(c, soma,))
