#Crie um programa que leia nome e duas notas de vários alunos
#guarde tudo em uma lista composta
#no final, mostre um boletim contendo a média de cada um
#permita que o usuário possa mostrar as notas de cada aluno individualmente
lista = []
continuar = ''

print('*****BOLETIM ESCOLAR******')

while continuar != 'n':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota_1: '))
    nota2 = float(input('Nota_2: '))

    media = (nota1 + nota2) / 2

    continuar = str(input('Deseja continuar?[s/n]')).lower()[0]

    lista.append([nome, [nota1, nota2], media])

    if continuar == 'n':
        print('****BOLETIM GERADO COM SUCESSO****')
        print('-'*26)
        print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
        print('-'*26)
        for i, a in enumerate(lista):
            print(f'{i:<}{a[0]:<10}{a[2]:>8.1f}')
