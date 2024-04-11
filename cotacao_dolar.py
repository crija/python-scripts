# Import request to use a get method
# Consult a API to find out the value of the dollar

import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes["USDBRL"]["bid"]
print(cotacoes_dolar)