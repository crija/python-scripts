#Criar uma lista de tarefas;
from time import sleep
tarefas = []
tar = res = eliminar = rem = ''
titulo = 'TAREFAS'

while tar != 'n':
    tarefas.append(str(input('Digite a tarefa: ')))
    tar = str(input('Deseja adicionar mais alguma tarefa?[s/n] ')).lower()[0]
    if tar != 's':
        print('-'*30)
        print(titulo.center(30, '*'))
        for c, t in enumerate(tarefas):
            print(f'Tarefa n{c}: {t}')
        print('-'*30)
        rem = str(input('Deseja remover alguma tarefa?[s/n] '))
        if rem == 's':
            elemento = int(input('Digite o número da tarefa: '))
            del tarefas[elemento]

            print('carregando...')
            sleep(3)

            print('Lista alterada com sucesso!')
            print('-'*30)
            print(titulo.center(30, '*'))
            for i, o in enumerate(tarefas):
                print(f'Tarefa n{i}: {o}')
            print('-'*30)
            break
        else:
            print('Programa encerrado')
