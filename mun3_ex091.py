#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
#No final, mostre o conteúdo da estrutura na tela


aluno = {}

aluno['nome']= str(input('Nome: '))

aluno['media']= float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] < 6:
    aluno['situação'] = 'Reprovado'

else:
    aluno['situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
