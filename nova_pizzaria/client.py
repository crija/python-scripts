class Cliente:
    def __init__(self, rua, numero, bairro):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro

    def definir_rua(self, rua):
        self.rua = rua

    def definir_numero(self, numero):
        self.numero = numero

    def definir_bairro(self,bairro):
        self.bairro = bairro