#EXEMPLOS;

'''
pessoas = {'nome': 'Carla', 'sexo': 'F', 'idade': 18}

print(pessoas)
#{'nome': 'Carla', 'sexo': 'F', 'idade': 18}

print(pessoas['nome'])
#Carla

print(pessoas['sexo'])
#F

print(pessoas['idade'])
#18

print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')
#A Carla tem 18 anos

print(pessoas.keys())
#dict_keys(['nome', 'sexo', 'idade'])

print(pessoas.items())
#dict_items([('nome', 'Carla'), ('sexo', 'F'), ('idade', 18)])

for k in pessoas.keys():
    print(k)
#nome
#sexo
#idade

for v in pessoas.values():
    print(v)
#Carla
#F
#18

for k, v in pessoas.items():
    print(f'{k} = {v}')
#nome = Carla
#sexo = F
#idade = 18

del pessoas['sexo']
#Apagar sexo

pessoas['nome'] = 'Leandro'
#Adicionar Leando no lugar de Carla

pessoas['peso'] = 57.5
#Adicionar peso
'''

'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
#Adicionar dois dicionários dentro de uma lista

print(brasil[0])
#Printar o dicionário 0 {estado1}

print(brasil[0]['uf'])
#Printar o uf do dicionário 0
'''

dict = []
brasil = []
for c in range[0, 3]:
    estado['uf'] = str(input('Universidade Federal: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
#Adicionar dicionários em uma lista
