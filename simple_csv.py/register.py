import csv

def test_register_name_and_gender(n, g):
    dados = []

    g = g.upper()

    if g != 'F' and g != 'M':
        return 'invalid gender'
        
    dados.append(n)
    dados.append(g)

    with open("./arquivo.csv", 'a', newline='') as arquivo:
        campos_head = ['name', 'gender']
        writer = csv.DictWriter(arquivo, fieldnames=campos_head, delimiter=';')

        if arquivo.tell() == 0:
            writer.writeheader()

        writer.writerow({
                            'name': n,
                            'gender': g
                        })
        arquivo.close()

test_register_name_and_gender('ana', 'f')