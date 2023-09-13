projetos_iniciados = []
projetos_finalizados =[]

def linha():
    print('-'*30)

print('MANTENHA SEUS PROJETOS ORGANIZADOS')
linha()
while True:
    print('*')
    nome_projeto = str(input('Digite o nome do projeto:'))
    escolha = str(input('O projeto foi finalizado? '))
    if escolha == 's':
        projetos_finalizados.append(nome_projeto)
    elif escolha == 'n':
        projetos_iniciados.append(nome_projeto)
    res = str(input('Deseja adicionar mais algum projeto? [s/n]: ')).lower()
    if res == 'n':
        break
linha()
print(f'Você tem {len(projetos_iniciados)} projetos esperando por você :)')
for count, value in enumerate(projetos_iniciados):
    print(count+1, value)
    
linha()
print(f'Parabéns! Você já tem {len(projetos_finalizados)} projetos finalizados :)')
for c, v in enumerate(projetos_finalizados):
    print(c+1, v)



