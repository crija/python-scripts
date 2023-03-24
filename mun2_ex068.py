#Desenvolva um programa que leia o nome, idade e sexo de 3 pessoas. No final do programa, mostre:
# >A média de idade do grupo;
# >Qual é o nome do homem mais velho;
# >Quantas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1, 5):

    print('------------ PESSOA {} ------------'.format(c))

    nome = str(input('Qual é o nome da pessoa {}? '.format(c))).strip()

    idade = int(input('Qual é a idade da pessoa {}? '.format(c)))

    sexo = str(input('Qual é o sexo da pessoa {}? [M/F] '.format(c))).strip()

    somaidade += idade

    if c == 1 and sexo in 'Mm':

        maioridadehomem = idade

        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:

        maioridadehomem = idade

        nomevelho = nome

    if sexo in 'Ff' and idade < 20:

        totmulher20 += 1

mediaidade = somaidade / 4

print('A média da idade do grupo é {:.2f}'.format(mediaidade))

print('A idade do homem mais velho é {} e seu nome é {}'.format(maioridadehomem, nomevelho))

print('São {} mulheres com menos de 20 anos'.format(totmulher20))
