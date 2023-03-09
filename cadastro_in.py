
print('*Indica item obrigatório')

print('')

print('Nome*')
nome = str(input('- '))

if nome == '':
    print('Nome é obrigatório')
else:
    print('_' *40)

    print('Sobrenome*')
    sobrenome = str(input('- '))

    if sobrenome == '':
        print('Sobrenome é obrigatório')
    else:
        print('_' *40)

        print('Nome adicional*')
        n_a = str(input('- '))

        print('_' *40)

        print('Informe as pessoas como elas devem se referir a você.')
        p_p = input('-  ')

        print('_' *40)
