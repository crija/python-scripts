#Crie um programa onde o usuário possa digitar vários valores numéricos;
#cadastre-os em uma lista;
#Caso o número já exista lá dentro, ele não será adicionado;
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

from time import sleep

esc = ''
lista = []

print('-'*70)
print('CRIE UMA LISTA COM OS NÚMEROS DA SUA ESCOLHA'.center(70,))
print('-'*70)

while esc != 'n':
    num = int(input('Digite um número: '))
    esc = str(input('Deseja acrescentar mais um número na sua lista? [S/N] ')).lower()

    if esc != 'n':
        print('*')

    lista.append(num)
    lista.sort()
    lista_sem_repetiçao = list(set(lista))

print('carregando...')
sleep(3)

print(f'Sua lista de números está pronta: {lista_sem_repetiçao}')
