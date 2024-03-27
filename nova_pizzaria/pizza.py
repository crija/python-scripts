adicionais = {'cheddar': 4.25, 'maionese verde': 2.50, 'morango': 5.15, 'chocolate preto': 8.90}
bordas = {'catupiry': 10.99, 'bombom': 15.90}
tamanhos = {'P': 34.99, 'M': 42.99, 'G': 55.99}

class Pizza:
    def __init__(self, tamanho, sabores, borda):
        self.tamanho = tamanho
        self.sabores = sabores
        self.borda = borda

    def escolher_tamanho(self, tamanho):
        self.tamanho = tamanho

    def escolher_sabor(self, sabor):
        self.sabores.append(sabor)

    def escolher_borda(self, borda):
        self.borda = borda

    def valor_total(self):
        valor_tamanho = tamanhos[self.tamanho]
        valor_borda = bordas[self.borda]
        return valor_borda + valor_tamanho
