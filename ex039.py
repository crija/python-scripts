#Escreva um programa que leia a velocidade de um carro.
print('A qual velocidade o carro está?')
velocidade = int(input('INSIRA A VELOCIDADE: KM '))

#Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
if velocidade > 80:
    print('Você foi multado por excesso de velocidade!')

#A multa vai custar R$7,00 por cada km acima do limite.
    multa = ((velocidade - 80) * 7)

    print('Por ter excedido o limite de velocidade você pagará uma multa de R$ {:.2f}.'.format(multa))

else:
    print('Você está dentro do limite de velocidade.')
    print('Tenha uma boa viagem.')

    print('_' *10)

    print('SE BEBER NÃO DIRIJA!')
