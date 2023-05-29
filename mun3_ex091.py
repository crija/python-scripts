#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
#No final, mostre o conteúdo da estrutura na tela

from time import sleep
res = ''
aluno = {}

while True:
    print('*BOLETIM DO ALUNO*')
    print('')
    aluno['Nome_do_aluno'] = input('Nome completo do aluno: ').upper()
    aluno['Nota_atingida'] = float(input(f"Nota de {aluno['Nome_do_aluno']}: "))
    aluno['Matéria'] = input('Matéria: ')
    aluno['Média_para_aprovaçao'] = float(input('Média para ser aprovado: '))

    if aluno['Nota_atingida'] < aluno['Média_para_aprovaçao']:
        aluno['Situaçao'] = 'Reprovado'
    elif aluno['Nota_atingida'] > aluno['Média_para_aprovaçao']:
        aluno['Situaçao'] = 'Aprovado'
    else:
        aluno['Situaçao'] = 'Recuperaçao'


    print('')
    print('carregando boletim...')
    sleep(2)
    print('')

    print(f"BOLETIM DO ALUNO(A) {aluno['Nome_do_aluno']}")
    print('=-'*15)
    for c in aluno.items():
        print(f"{c[0]}: {c[1]}")

     
    print('=-'*15)
    
    res = int(input('Para sair digite 999: '))
    print('')
    if res == 999:
        break


        

