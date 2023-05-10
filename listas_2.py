#criar listas dentro de lista
galera = [['João', 34], ['Bia', 14], ['Guilherme', 23]]

#printar a lista
print(galera)

#printar item 1 dentro da lista
print(galera[0][1])

#printar toda a lista 2 dentro da lista
print(galera[2])

#printar todos os itens da posição 1
for p in galera:
    print(p[1])

#printar os itens das posições 0 e 1
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

#botar itens tendro de uma lista vazia
galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

#organizar com maior e menor de Idade
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'{totmaior} são maiores de idade e {totmenor} são menores de idade')
