#Criar uma lista de tarefas;
tarefas = []
tar = ''

while tar != 'nao':
    tarefas.append(str(input('Digite a tarefa: ')))
    tar = str(input('Deseja adicionar mais alguma tarefa? ')).lower()
    if tar != 'sim':
        for c, t in enumerate(tarefas):
            print(f'Tarefa n{c}: {t}')
        print('Essas são as tarefas do dia')
    elif tar == 'nao':
        break
