#Crie um programa que calcule o aumento salarial de um funcionario:

salario = float(input('Qual é o salario de um funcionario? R$'))

valor = salario + (salario * 15 /100)

print('Um funcionario que recebe R${:.2f}, com 15% de desconto vai receber R${:.2f}.'.format(salario, valor))
