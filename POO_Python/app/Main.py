class Main:
    pass

from POO_Python.app.Client import Client

from POO_Python.app.Account import Account

c1 = Client("João", "114444-2222")
account = Account(c1.get_name(), 1222)

account.deposit(100)
account.transfer(50)
account.extract()

