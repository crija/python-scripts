'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas: aumentar(), diminuir(), dobro(), metade().
Faça também um programa que importe esses módulos e use algumas dessas funções.

'''
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'Aumentando 10%, temos um aumento de: {moeda.aumentar(p)}')
print(f'Reduzindo 13%, temos: {moeda.diminuir(p)}')