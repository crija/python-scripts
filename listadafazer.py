#Criar uma lista de tarefas;
tarefas = []

for cont in range(1, 4):
    tarefas.append(str(input('Digite a tarefa: ')))
for c, t in enumerate(tarefas):
    print(f'Tarefa n{c}: {t}')
print('Essas são as tarefas do dia')
