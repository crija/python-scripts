#Crie um programa onde o usuário possa digitar sete valores númericos
# e cadastre-os em uma lista única que mantenha separados os valores
#No final, mostre os valores pares e impares em ordem cresecente

v = 0
val = []
par = []
imp = []

for v in range(0, 7):
    v = int(input('Digite um valor: '))
    print('*')
    if v % 2 == 0:

        par.append(v)

    else:
        imp.append(v)

par.sort()
imp.sort()
val.append(par[:])
val.append(imp[:])

print('*'*53)
print(f'Os números digitados foram: \033[2;31m{val}\033[m')
print(f'Os números pares são: \033[2;31m{par}\033[m')
print(f'Os números ímpares são: \033[2;31m{imp}\033[m')
print('*'*53)
