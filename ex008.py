#Crie um programa que leia algo pelo teclado;
#teste = input('Digite algo')

#e mostre na tela o seu tipo primitivo;
#teste = str(input('Digite algo'))
#print(type(teste))

#e todas as informações possiveis sobre ele:
teste = str(input('Digite algo:'))

print(type(teste))

print(teste.isalpha(), teste.isalnum(), teste.isspace())

#-isalpha == alfabetico
#-isalnum == alfanumerico
#-isspace == espaço
