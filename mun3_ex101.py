#app_aluguel de carro.
 
aluguel = {}


while True:
    aluguel['nome'] = str(input('Qual carro você deseja alugar? '))
    aluguel['retirada'] = int(input('Data de retirada do veículo: '))
    aluguel['retorno'] = int(input('Data de retorno do veículo: '))
    break
print(aluguel)


