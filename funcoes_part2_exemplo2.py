'''EXEMPLO 2'''
#Retornar False ou True:

#Função com o parâmetro 'n' recebendo '0', como padrão.
def par (n=0):

#Condição de retorno.
    if n % 2 == 0:
        return True 
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

