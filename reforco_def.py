#Faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    print(f'Largura: {larg}, Comprimento: { comp }: Área ={larg * comp :.2f}')

#programa principal
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)