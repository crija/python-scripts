#Faça a taboada de um número que o usuário escolher, usando o laço de repetição:

num = int(input('Digite um número: '))
for c in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, c, num*c))
