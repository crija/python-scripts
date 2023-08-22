from random import choice
import string

quantidade_caracter = int(input('Quantos caracteres a senha deve ter? '))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(quantidade_caracter):
    senha += choice(caracteres)

print(f'Sua senha é: {senha}')