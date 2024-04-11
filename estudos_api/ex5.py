# Consult the API that gives you advice

import requests

consult_api = requests.get('https://api.adviceslip.com/advice')
print(consult_api)
print(consult_api.json())