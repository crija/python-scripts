#Crie um programa que leia o ano de nascimento de sete pessoas.No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores;

var = 18
for c in range(0, 7):
    idade = int(input('Quantos anos você tem? '))
    if idade > 18:
        idade =+ 18
print('{} pessoas já completaram a maior idade:'.format(idade))
