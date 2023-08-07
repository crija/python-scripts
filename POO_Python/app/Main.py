class Main:
    pass

print('Testando o objeto')

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.nome, 6565, 0)

print(f'{conta.titular} {conta.numero}, Seu Saldo: {conta.saldo}')

