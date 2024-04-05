from constants import TAMANHOS, ADICIONAIS, BORDAS
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
        valor_tamanho = TAMANHOS[self.tamanho]
        valor_adicional = ADICIONAIS[self.adicional]
        valor_borda = BORDAS[self.borda]
        return valor_tamanho + valor_adicional + valor_borda




