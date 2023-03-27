#Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 1
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Qual é seu sexo [m/f]?')).upper()
    if sexo == 'F':
        print('O seu sexo é FEMININO.')
    else:
        print('O seu sexo é MASCULINO')
