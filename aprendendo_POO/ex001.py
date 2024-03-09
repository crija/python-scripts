# Definindo a classe
class Caneta:
# Define a função __init__ com os parâmetros. A função __init__ é chamada toda vez que um objeto é instanciado. O parâmetro self é o próprio objeto que está sendo criado
    def __init__(self, modelo, cor, ponta, carga, tampa):
# Seta os valores dos atributos do objeto. 'self.modelo' é o atributo e 'modelo' é o valor do atributo
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampa = tampa

# Definindo o método rabiscar. Passando o 'self' como parâmetro para acessar o objeto
    def rabiscar(self):
# Acessar o atributo ponta (self.ponta), para fazer a comparação de valores
        if self.ponta == 1.0:
            print('Pintar desenho')
        else:
            print('Escrever carta')

# Criar variável para definir um valor
marca = 'castelo'
# Instanciar um objeto. Usar o nome da classe para istanciar um objeto e definir os valores dos parâmetros da função __init__. Passar a variável anterior como um valor
caneta = Caneta(marca, 'preta', 1.0, 80, True)
# Chamar o método rabiscar
caneta.rabiscar()

#Instanciar o segundo objeto
caneta2 = Caneta('Bic', 'laranja', 0.75, 100, False)
# Chamar o método rabiscar. O método de uma classe pode ser usado em todos os objetos instanciados.
caneta2.rabiscar()
