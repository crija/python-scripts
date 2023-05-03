#Crie um programa onde o usuário possa digitar vários valores numéricos;
#cadastre-os em uma lista;
#Caso o número já exista lá dentro, ele não será adicionado;
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

esc = ''
lista = []

while esc != 'nao':
    lista.append(int(input('Digite um número: ')))
    esc = str(input('Deseja acrescentar mais um número na sua lista? '))

    if esc != 'nao':
        print('*')
print(lista)
