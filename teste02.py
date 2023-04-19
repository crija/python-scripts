meunome = ''
nome = str(input('Qual seu nome? '))
print('Que nome bonito.')
while meunome != 'CARLA':
    meunome = str(input('Agora divinha meu o nome: ')).upper()
    if meunome == 'CARLA':
        print('Isso aí, você acertou!')
        print(f'Prazer em te conhecer, {nome}!')
    else:
        print('Ops...você errou')
        print('Tente de novo!')
