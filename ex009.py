#Crie um sistema que mostre a média da nota do aluno:
#Pass.1 [De uma nota para aluno:]
#Pass.2 [De outra nota para o aluno:]
#Pass.3 [Calcule as notas:]
#Pass.4 [Calcule a media:]
#Pass.5 [Escreva uma string mostrando o resultado:]

num1 = float(input('Digite uma nota: '))
num2 = float(input('Digite outra nota: '))

s = num1 + num2
m = num1 / num2

print('A média de {} e {} vale {}'.format(num1, num2, m))
