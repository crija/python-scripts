class Cliente:
    def __init__(self, n, fone):
        
        self._nome = n
        self._telefone = fone

    #método get
    def get_nome(self):
        return self._nome

    #método set
    def set_nome(self, nome):
        self._nome = nome