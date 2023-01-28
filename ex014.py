#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta nescessária para pintá-la, sabendo que cada litro de tinta, pinta 2m²:

print('Vamos descobrir qual a área da sua parede e quanto de tinta é nescessária para pintá-la! ')

largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))

area = largura * altura

print('A sua parede é de {}x{} e a sua área é de {}m².'.format(largura, altura, area))

tinta = area / 2

print('Sendo assim, você precisa de {} litros de tinta para pintar a sua parede.'.format(tinta))
