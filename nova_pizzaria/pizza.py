import csv
adicionais = {'cheddar': 4.25, 'maionese verde': 2.50, 'morango': 5.15, 'chocolate preto': 8.90}
bordas = {'catupiry': 10.99, 'bombom': 15.90}
tamanhos = {'p': 34.99, 'm': 42.99, 'g': 55.99}

class Pizza:
    def __init__(self, tamanho, sabores, adicional, borda):
        self.tamanho = tamanho
        self.sabores = sabores
        self.adicional = adicional
        self.borda = borda

    def escolher_tamanho(self, tamanho):
        self.tamanho = tamanho

    def escolher_sabor(self, sabor):
        self.sabores.append(sabor)

    def escolher_adicional(self, adicional):
        self.adicional = adicional

    def escolher_borda(self, borda):
        self.borda = borda

    def valor_total(self):
        valor_tamanho = tamanhos[self.tamanho]
        valor_borda = bordas[self.borda]
        return valor_borda + valor_tamanho
