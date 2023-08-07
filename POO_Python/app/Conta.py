class Conta:
    def __init__(self, titular, numero, saldo):
        
        self.saldo = 0
        self.numero = numero
        self.titular = titular

        @property
        def saldo(self):
            return self._saldo
        
        @saldo.setter
        def saldo(self, saldo):
            if (saldo < 0):
                print('Saldo não pode ser negativo')
            else:
                self._saldo = saldo

        