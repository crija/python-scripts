#Crie um programa que leia a ano idade de sete pessoas. No final, mostre quantas pessoas ainda são de menor:
'''soma = 0
cont = 0
for c in range(1, 8):
    idade = int(input('qual a idade da pessoa {}? '.format(c)))
    if idade < 18:
        soma = soma + 1
print('Das {} pessoas {} são MENORES de idade'.format(c, soma,))'''


#Modo 2:
from datetime import date

atual = date.today().year

totmaior = 0
totmenor = 0

for c in range(1, 8):

    ano = int(input('Qual ano a pessoa {} nasceu? '.format(c)))

    idade = atual - ano

    if idade >= 18:

        totmaior = totmaior + 1
    else:

        totmenor = totmenor + 1

print('Das {} pessoas {} são menores de idade e {} são maiores de idade'.format(c, totmenor, totmaior))
