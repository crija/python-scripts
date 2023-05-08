#Crie um programa omde o usuário digite uma expressão quelquer que use parênteses
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

exp = str(input('Digite uma expressão: '))
pilha = []
for par in exp:
    if par == '(':
        pilha.append('(')
    elif par == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')
