#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250 , calcule um aumento de 10%.

salário = float(input('\033[1;32m Quanto você recebe? \033[m R$'))

if salário > 1250:

    aumento1 = salário + (salário *10 / 100)

    print('O seu novo salário com \033[31m 10% \033[m de aumento é:\033[1;31m R${:.2f} \033[m'.format(aumento1))


#Para os inferiores ou iguais, o aumento é de 15%.

elif salário <= 1250:

    aumento2 = salário + (salário *15 / 100)

    print('O seu novo salário com \033[31m 15% \033[m de aumento é:\033[1;31m R${:.2f}\033[m'.format(aumento2))
