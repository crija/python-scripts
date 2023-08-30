# -Interactive help:
'''
- Posso rodar help() no terminal e logo em seguida pedir ajuda em algo específico:
ex:
>>>help()
help>print
- Em seguida retornará um documento com toda a explicação do que foi pedido
- Para retornar ao terminal do python, digite 'quit'.

- Ou eu posso criar um arquivo para chamar o help():
ex:
help(print)
- Estou pedindo para me explicar o que é o 'print'.
'''
# -Docstrings:
'''
- A docstrings é uma string de documentação, sendo similar ao 'help'.
ex:
- crie um arquivo e escreva:
print(input.__doc__)
- Vai rodar a explicação da função 'input'.

- Podemos usar docstrings  para documentar partes do código, por exempo: Usei 3 parâmetros em uma função e quero fazer um documento para deixa-las entendíveis. Para isso, eu posso criar uma documentação utilizando docstrings e explicar por etapas.
ex:
def contador(i, f, p):
    """
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem 
    :função criada por Carla Crija estudante de programação.
    """
- Documentação criada para explicar os parâmetros usados na função.
'''

# -Parâmetros opcionais
'''
- Parâmetros opcionais podem ser usados em uma função que tem como objetivo a soma de números aleatórios.
ex:
def soma(a, b, c):
    s = a+b+c
    print(s)
soma(3, 4, 9)
soma(5, 2) 
soma()

- Foram definidos 3 parâmetros que esperam receber 3 números, mas na linha 43 foi definido apenas 2 números. Para que o código não gere um erro, nós usamos o parâmetro opcional. 
ex:
def soma(a, b, c=0):
    s = a+b+c
    print(s)
soma(3, 4, 9)
soma(5, 2) 
soma()
-Assim, 'a' receberá o valor 5, 'b' receberá o valor '2' e 'c' receberá o valor 0.

-Na linha 53 o objetivo é o mesmo.
ex:
def soma(a=0, b=0, c=0):
    s = a+b+c
    print(s)
soma(3, 4, 9)
soma(5, 2) 
soma()
'''
# -Escopo de Variáveis:
'''
- Escopo é o local onde a variável vai existir e o local onde a variável não vai mais existir.
ex:
def teste():
    print(n)

# Programa principal:
n = 2
print(n)
- Nesse caso 'n' é uma variável que está sendo usada no programa principal e na função 'teste', nesse caso, 'n' recebe a definição de escopo global.

- No exemplo a seguir nós vamos ver 'x' funcionando somente na função 'teste', por não ter sido definida no programa principal. Sendo assim 'x', nesse caso, é definido como escopo local.
def teste():
    x = 8
    print(n)
    print(x)

# Programa principal:
n = 2
print(n)
'''
# -Retorno de valores:
'''
- Funções com retorno.
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(4, 8, 9)
r2 = somar(3, 9) 
r3 = somar(1, 4)

print(f'Os resultados foram {r1}, {r2}, {r3}')
- Retornará todos os valores dentro do format.

'''

