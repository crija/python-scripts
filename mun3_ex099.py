#Faça um programa que tenha uma função chamada contador()
#Que receba três parametros:início, fim e passo e realize a contagem
#Seu programa tem que realizar três contagens através da função criada
# A)De 1 até 10, de 1 em 1;
# B)De 10 até 0, de 2 em 2;
# Uma contagem personalizada pelo usuário.

from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i}, até {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

#programa principal
contador(1, 10, 1)
contador(10, 0, 2)


