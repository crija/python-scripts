#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)

print('\033[35m Analisandor de \033 \033[1;35m TRIÂNGULO \033[m .')

print('-='*20)

r1 = float(input('\033[1;37m Primeiro segmento: \033[m '))
r2 = float(input('\033[1;37m Segundo segmento: \033[m '))
r3 = float(input('\033[1;37m Terceiro segmento: \033[m '))

if r1 < r2 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[34m PODEM FORMAR \033[m triângulo!')

else:
    print('Os segmento acima \033[31m NÃO PODEM FORMAR \033[m triângulo.')
