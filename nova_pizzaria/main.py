import csv
from pizza import *
from constants import *

pizza = Pizza('', [], '', '')

print('Tamanho')
for i in TAMANHOS.items():
    print(i)

escolher_tamanho = input('Escolha o tamanho: ')
pizza.escolher_tamanho(escolher_tamanho)
print(pizza.tamanho)

print(SABORES)
if pizza.tamanho == 'p':
    print('Você pode escolher 2 sabores')
    for s in range(0, 2):
        escolher_sabor = input('Escolha o sabor: ')
        pizza.escolher_sabor(escolher_sabor)

elif pizza.tamanho == 'm':
    print('Você pode escolher 3 sabores')
    for s in range(0, 3):
        escolher_sabor = input('Escolha o sabor: ')
        pizza.escolher_sabor(escolher_sabor)

else:
    print('Você pode escolher 4 sabores')
    for s in range(0, 4):
        escolher_sabor = input('Escolha o sabor: ')
        pizza.escolher_sabor(escolher_sabor)

print('adicional')
for a in ADICIONAIS.items():
    print(a)
escolher_adicional = input('Escolha um adicional: ')
pizza.escolher_adicional(escolher_adicional)

print('Borda')
print(BORDAS)
escolher_borda = input('Escolha a borda: ')
pizza.escolher_borda(escolher_borda)
pizza.valor_total()

print(pizza.sabores)
print(pizza.borda)
print(pizza.adicional)

with open("nova_pizzaria/arquivo.csv", 'a', newline='') as arquivo:
    campos_head = ['tamanho', 'igredientes', 'borda', 'adicional', 'total']
    writer = csv.DictWriter(arquivo, fieldnames=campos_head, delimiter=';')

    if arquivo.tell() == 0:
        writer.writeheader()

    writer.writerow({
                        'tamanho': pizza.tamanho,
                        'igredientes': pizza.sabores,
                        'borda': pizza.borda,
                        'adicional': pizza.adicional,
                        'total': pizza.valor_total(),
                    })
    arquivo.close()
