#Calcule a média de um aluno e diga se foi boa ou ruim:

print('CALCULE A SUA MÉDIA DE UM JEITO PRATICO *-*')

print('+-' *15)

print('Primeira nota:')
n1 = float(input('- '))

print('Segunda nota:')
n2 = float(input('- '))

média = (n1 + n2)/ 2

print('+-' *15)
print('')

if média == 6:
    print('({:.1f})'.format(média))
    print('')
    print('Você atingiu a média.MUITO BOM! ')

elif média < 6:
    print('({:.1f})'.format(média))
    print('')
    print('Que pena,você não atingiu a média!')

else:
    print('({:.1f})'.format(média))
    print('')
    print('Você passou da média.PARABÉNS')
