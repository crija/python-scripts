#Faça um programa que tenha uma função chamada escreva();
#Que receba um texto quelquer como parametro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print(len(msg)*'-')
    print(msg)
    print(len(msg)*'-')


escreva('Ola')
escreva('mundo')
