#Faça um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador;
#O computador deverá escrever na tela se o usuário venceu ou perdeu.

import random
random.randint(0,5)

print('Tente adivinhar qual é o número.')
print('Escolha um número de 0 a 5.')
número = int(input('* '))

x = random.randint(0,5)
print('O número sorteado foi...{}'.format(x))

if número != x:
    print('Que pena, você errou.')
    print('Não desista, tente novamente!')

else:
    print('PARABÉNS, VOCÊ ACERTOU')
