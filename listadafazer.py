#Criar uma lista de tarefas;
tarefas = []
tar = ''
res = ''
eliminar = ''

while tar != 'nao':
    tarefas.append(str(input('Digite a tarefa: ')))
    tar = str(input('Deseja adicionar mais alguma tarefa? ')).lower()

    if tar != 'sim':
        for c, t in enumerate(tarefas):
            print(f'Tarefa n{c}: {t}')
        print('Essas são as tarefas do dia')

    '''    while eliminar != 'nao':
            for d, r in enumerate(tarefas):
                eliminar = str(input('Deseja eliminar alguma tarefa? '))
                if eliminar != 'nao':
                    nome = str(input('Digite o nome da tarefa: '))
                    tarefas.pop()
                    print(f'Tarefa n{d}: {r} - eliminada')   '''
