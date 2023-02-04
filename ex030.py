#Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo: ')).strip()

#>>> o nome com todas as letras minusculas;
print(' ')
print('O seu nome com todas as letras minusculas:')
print(nome.lower())
print('___')
#>>> o nome com todas maiusculas;
print('O seu nome com todas as letras maiusculas:')
print(nome.upper())
print('___')
#>>> quantas letras ao todo (sem considerar espaço);
print('A quantidade de letras no seu nome:')
print(len(nome) - nome.count(' '))
print('___')
#>>> quantas letras tem o primeiro nome.
print('A quantidades de letras no seu primeiro nome:')
print(nome.find(' '))
