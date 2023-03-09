#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('Digite seu nome completo:')
nome = str(input('')).strip()

n = nome.split()

print('Prazer em te conhecer!')

print('Seu primeiro nome é {}'.format(n[0]))

print('Seu último nome é {}'.format(n[len(n)-1]))
