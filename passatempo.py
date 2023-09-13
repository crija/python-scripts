projetos = []

def linha():
    print('-'*30)

print('MANTENHA SEUS PROJETOS ORGANIZADOS')
linha()
while True:
    nome_projeto = str(input('Digite o nome do projeto:'))
    res = str(input('Deseja adicionar mais algum projeto? [s/n]: ')).lower()
    projetos.append(nome_projeto)
    if res == 'n':
        break
linha()
print('Projetos não terminados')
for count, value in enumerate(projetos):
    print(count+1, value)
print(f'Você tem {len(projetos)} projetos esperando por você :)')

