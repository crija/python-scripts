#Faça a taboada de um número que o usuário escolher, usando o laço de repetição:

while True:

    num = int(input('Quer saber a tabuada de qual número? '))

    if num < 0:

        break

    for c in range(0, 11):

        if num > 0:

            print('{} x {:2} = {:2}'.format(num, c, num*c))

print('PROGRAMA ENCERRADO!')
