#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
#No final, mostre o conteúdo da estrutura na tela

nome = str(input('Nome: '))
nota = float(input('Nota: '))
if nota < 6:
aluno = {nome: nota}
print(f'{aluno}')






