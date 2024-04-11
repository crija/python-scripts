# API that provides requested phrases

import requests

msg = requests.get('https://api.kanye.rest')

print(msg)
print(msg.json())