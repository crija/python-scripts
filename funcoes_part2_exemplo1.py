'''EXEMPLO 1'''

#Calcular o fatorial de um número e retorna-lo para o programa principal.

#Função com o parâmetro 'num', que se não receber nenhum número, vai utilizar o número '1'.
def fatorial(num = 1):

#Variavel local, valendo '1'.
    f = 1

#Para fazer o fatorial utiliza-se uma estrutura de repetição, que começa no 'num', vai até 0, voltando de 1 em 1.
    for c in range(num, 0, -1):
        
#'f' recebe 'f' vezes 'c'.
        f *= c

#retornar o que está na variável 'f'.
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')