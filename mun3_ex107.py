# Tratamento de Erros e Exceções

try:
    a = int (input('Numerador: '))
    b = int(input('Denumerador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.2}')
finally:
    print('Volte sempre!')