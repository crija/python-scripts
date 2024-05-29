import sys
print ('argument list', sys.argv)
valor = sys.argv[1]
desconto = sys.argv[2]


valor = int(valor)
desconto = int(desconto)
print(valor, desconto)


total_desconto = valor * desconto / 100
print(f'desconto R${total_desconto}')