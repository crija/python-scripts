class Account:
    def __init__(self, holder, number, balance):
        
        self.balance = 0
        self.number = number
        self.holder = holder

        @property
        def balance(self):
            return self._balance
        
        @balance.setter
        def balance(self, balance):
            if (balance < 0):
                print('Your current balance are negative')
            else:
                self._saldo = balance

        def transfer(self, value):
            if (self.balance >= value):
                self.balance -= value
                print('Transfer made')
            else:
                print('Insufficient Balance')

        def deposit(self, value):
            self.balance += value

        def extract(self):
            print(f'Client: {self._holder}, Current Balance: {self._balance}')
            
        