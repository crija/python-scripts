#Crie um programa onde o usuário possa digitar sete valores númericos
# e cadastre-os em uma lista única que mantenha separados os valores
#No final, mostre os valores pares e impares em ordem cresecente

val = [[], []]
v = 0

for v in range(0, 7):
    v = int(input(f'Digite o {v}o número: '))
    print('*')
    if v % 2 == 0:
        val[0].append(v)
    else:
        val[1].append(v)

val[0].sort()
val[1].sort()

print(f'Os números pares digitos foram: {val[0]}')
print(f'Os números impares digitados foram: {val[1]}')
