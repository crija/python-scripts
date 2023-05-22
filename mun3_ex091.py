#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
#No final, mostre o conteúdo da estrutura na tela


aluno = {}

aluno['nome']= str(input('Nome: '))

aluno['media']= float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] < 6:
    print(f'Aluno {aluno["nome"]} está reprovado')
    print(f'Média: {aluno["media"]}')

else:
    print(f'Aluno(a) {aluno["nome"]} está aprovado(a)')
    print(f'Média: {aluno["media"]}')
