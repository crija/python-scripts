#Crie um programa que leia nome, sexo e idade de várias pessoas;

#Guarde os dados de cada pessoa em um dicionário e todos os dicionários e em uma lista.

#No final, mostre:

# - Quantas pessoas foram cadastradas;
# - A média de idade do grupo;
# - Uma lista com todas as mulheres;
# - Uma lista com todas as pessoas com idade acima da média.

pessoas = dict()
lista = list()
res = ''
num_pes = 0
tot_idade = 0
med_idade = 0
lista_mulheres = list()
idade_maior = list()

while True:
    pessoas['nome'] = str(input('Digite seu nome: '))
    num_pes += 1

    pessoas['sexo'] = str(input('Digite seu sexo [m/f]: '))
    if pessoas['sexo'] == 'f':
        lista_mulheres.append(pessoas['nome'])

    pessoas['idade'] = int(input('Quantos anos você tem? '))
    tot_idade = tot_idade + pessoas['idade']
    med_idade = tot_idade / num_pes

    
    lista.append(pessoas)

    while True:
        res = str(input('Deseja continuar [s/n]: ')).lower()[0]

        if res in 'sn':
            break

    if res == 'n':
        break
        
print('_'*45)
print(f'O total é de: {num_pes} pessoas')
print(f'A média de idade é de: {med_idade}')
print(f'Nome das mulheres cadastradas: {lista_mulheres}')
print('_'*45)