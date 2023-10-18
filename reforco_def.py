#Faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    print(f'Largura: {larg}, Comprimento: {comp}: Área = {larg * comp}')

#programa principal
largura = int(input('Largura: '))
comprimento = int(input('Comprimento: '))
area(largura, comprimento)