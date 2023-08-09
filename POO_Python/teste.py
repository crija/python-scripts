class Pessoa:
    def __init__(self, nome, idade, sexo, ativo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


    def desativar(self):
        self.ativo = False
        print(f'{pessoa1} foi desafivada com sucesso')
        
pessoa1 = Pessoa('Eduardo', 27, 'M', True)
pessoa1.desativar()

