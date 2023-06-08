#Faça um programa que tenha uma função chamada área();
#que receba as dimensões de um terreno retangular(largura e comprimento);
#mostre a área do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m2')

#Programa principal:
print('Controle de terrenos')
print('*' *20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)