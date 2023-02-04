#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros:

me = float(input('Enter a number: '))

ce = me * 100
mi = me * 1000

print(' {} converted to centimeters {}.\n {} converted to millimeters {}.'.format(me, ce, me, mi))
