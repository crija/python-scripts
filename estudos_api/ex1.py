# Usando o método GET
# Criar um banco de dados no site Firebase para buscar informações
# linha 8: Importar o a bibliotéca requests para se comunicar com a API
# linha 10: Guardar em uma variável a requisição da informação contida no banco de dados
# linha 12: Mostrar a resposta na tela
# linha 13: Mostrar na tela a informação no formato json

import requests

requisicao = requests.get("https://test-ef3c3-default-rtdb.firebaseio.com/.json")

print(requisicao)
print(requisicao.json())