class Caneta:
    def __init__(self, modelo, cor, ponta, carga, tampa):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampa = tampa

    def rabiscar(ponta):
        if caneta.ponta == 1.0:
            print('Pintar desenho')
        else:
            print('Escrever carta')



caneta = Caneta('faber', 'preta', 0.75, 80, True)
caneta.rabiscar()