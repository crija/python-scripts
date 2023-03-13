#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atinfida.
#Média abaixo de 5.0.REPROVADO
#Média entre 5.0 e 6.9.RECUPERAÇÃO
#Média 7.0 ou superior.APROVADO

nome = str(input('Nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('A média do aluno {} é {}. REPROVADO'.format(nome, media))

elif media == 5:
    print('A média do aluno {} é {}. RECUPERAÇÃO'.format(nome, media))

elif media > 5:
    print('A média do aluno {} é {}. APROVADO!'.format(nome, media))
