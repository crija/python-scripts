#Criar uma lista de tarefas;
tarefas = []
tar = res = eliminar = rem = ''

while tar != 'n':
    tarefas.append(str(input('Digite a tarefa: ')))
    tar = str(input('Deseja adicionar mais alguma tarefa?[s/n] ')).lower()[0]
    if tar != 's':
        for c, t in enumerate(tarefas):
            print(f'Tarefa n{c}: {t}')
        print('Essas são as tarefas do dia')
        rem = str(input('Deseja remover alguma tarefa?[s/n] '))
        if rem == 's':
            elemento = int(input('Digite o número da tarefa: '))
            del tarefas[elemento]
            for i, o in enumerate(tarefas):
                print(f'Tarefa n{i}: {o}')
