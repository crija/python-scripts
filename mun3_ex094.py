#Crie um programa que leia nome, ano de nascimento e carteira de trabalho;

#Cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário;

#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.(aposentadoria > 35 anos de contribuição).

import datetime
from time import sleep

worker = {}

worker['Nome'] = str(input('Name: '))
worker['Ano_Nascimento'] = int(input('Year of birth: '))
worker['Número_Carteira'] = int(input('Work card (0 it does not have): '))

if worker['Número_Carteira'] != 0:
    
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = int(date.strftime('%Y'))
    ano = worker['Ano_Nascimento']
    idade_atual = year - ano
    worker['Idade'] = idade_atual
    
    worker['Ano_Contratação'] = int(input('Year if hire: '))
    worker['Salário'] = int(input('Wage: '))
    aposentadoria = worker['Ano_Contratação'] + 35
    worker['Aposentar'] = aposentadoria

    print('carregando...')
    sleep(2)
    
    print('-'*25)
    for v, k in worker.items():
        print(f'{v}: {k}')
    print('-'*25)