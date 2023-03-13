#Desenvolva uma lógica que leia o pesa e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade morbida.

print('_'*33)

print('\033[3;37m Indice de Massa Corporal (IMC).\033[m')

print('_'*33)

print('\033[1;35m Quantos kg você pesa? \033[m')

peso = float(input('- '))

print('\033[1;35m Qual é a sua altura? \033[m')

altura = float(input('- '))

quadrado = altura * altura

divisão = peso / quadrado

if divisão < 18.5:

    print('\033[0;31m IMC: {:.1f} (Abaixo do peso).\033[m'.format(divisão))

elif divisão >= 18.5 and divisão < 25:

    print('\033[0;34m IMC: {:.1f} (Peso ideal).\033m'.format(divisão))

elif divisão >= 25 and divisão < 30:

    print('\033[0;33m IMC: {:.1f} (Sobrepeso).\033m'.format(divisão))

elif divisão >= 30 and divisão <= 40:

    print('\033[0;33m IMC: {:.1f} (Obesidade).\033[m'.format(divisão))

elif divisão > 40:
    
    print('\033[0;31m IMC: {:.1f} (Obesidade morbida).\033[m'.format(divisão))
