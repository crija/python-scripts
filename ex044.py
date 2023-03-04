#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250 , calcule um aumento de 10%.

salário = float(input('Quanto você recebe? '))

if salário > 1250:

    aumento1 = salário + (salário *10 / 100)

    print('O seu novo salário com 10% de aumento é:R$ {:.2f}'.format(aumento1))


#Para os inferiores ou iguais, o aumento é de 15%.

elif salário <= 1250:

    aumento2 = salário + (salário *15 / 100)

    print('O seu novo salário com 15% de aumento é:R$ {:.2f}'.format(aumento2))
