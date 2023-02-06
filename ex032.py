#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'SANTO'.
cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[0:5].upper() == 'SANTO')
