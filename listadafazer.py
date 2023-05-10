#Criar uma lista de tarefas;

from time import sleep

tarefas = []
tar = res = eliminar = rem = ''
titulo = '\033[4;33mCRIE A SUA LISTA DE TAREFAS!\033[m'
subtitulo = '\033[1;34mTAREFAS\033[m'

print(titulo.center(60, ' '))
print('')
while tar != 'n':
    tarefas.append(str(input('\033[2;37mDigite a tarefa:\033[m ')))
    tar = str(input('\033[2;37mDeseja adicionar mais alguma tarefa?[s/n]\033[m ')).lower()[0]
    print('')

    if tar != 's':
        print('\033[1;34m-\033[m'*30)
        print(subtitulo.center(30, '*'))
        for c, t in enumerate(tarefas):
            print(f'\033[2;35mTarefa n{c}:\033[m \033[2;34m{t}\033[m')

        print('\033[1;34m-\033[m'*30)
        print('')
        rem = str(input('\033[2;37mDeseja remover alguma tarefa?[s/n]\033[m '))

        if rem == 's':
            elemento = int(input('Digite o número da tarefa: '))
            print('')
            del tarefas[elemento]

            print('\033[1;31mcarregando...\033[m')
            sleep(3)

            print('Lista alterada com sucesso!')
            print('')
            print('\033[1;34m-\033[m'*30)
            print(subtitulo.center(30, '*'))


            for i, o in enumerate(tarefas):
                print(f'\033[2;35mTarefa n{i}:\033[m \033[2;34m{o}\033[m')
            print('\033[1;34m-\033[m'*30)
            break

        else:
            print('Programa encerrado!')
