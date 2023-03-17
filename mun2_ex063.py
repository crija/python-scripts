#Crie um programa que leia uma frase qualquer e diga se é um PALINDROMO, desconsiderando os espaço.

frase = input('\033[0;1;34m Escreva uma frase qualquer para saber se é um palindromo:\003 ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('\033[0;2;35m O inverso de {} é {} \003'.format(junto, inverso))
if inverso == junto:
    print('\033[0;2;34m É um palíndromo! \033')
else:
    print('\033[0;2;31m {} não um palíndromo!\033[m'.format(frase))
