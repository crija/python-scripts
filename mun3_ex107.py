# Tratamento de Erros e Exceções

try:
    a = int (input('Numerador: '))
    b = int(input('Denumerador: '))
    r = a/b
except:
    print('Ocorreu um erro :(')
print(f'O resultado é: {r}')