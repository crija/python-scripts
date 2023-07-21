#Faça um programa que tenha função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
''' 
- Quantidade de notas 
- A maior nota
- A menor nota
- a média da turma 
- A situação (opcional)
'''

def notas(*num, sit=False):
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)
    if sit:
        if r['média'] >=7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r



#Programa principal
resp = notas(5.5, 9, 2, 7.5, sit=True)
print(resp)