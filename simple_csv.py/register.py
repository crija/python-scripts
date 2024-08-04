import csv

dados = []

nome = str(input('Informe seu nome: ')).upper()
dados.append(nome)

s = str(input('Informe seu sexo: [M/F] ')).strip().upper()

while s not in 'MmFf':

    s = str(input('Dados invalidos.Tente novamente: [F/M]'))
dados.append(s)
print(dados)

print('Dados registrados com sucesso')

with open("./arquivo.csv", 'a', newline='') as arquivo:
    campos_head = ['nome', 's']
    writer = csv.DictWriter(arquivo, fieldnames=campos_head, delimiter=';')

    if arquivo.tell() == 0:
        writer.writeheader()

    writer.writerow({
                        'nome': nome,
                        's': s
                    })
    arquivo.close()