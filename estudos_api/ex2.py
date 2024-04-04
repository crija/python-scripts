# Usando o método POST
# line 6: new user
# line 9: using the post method to send the new user's data to database

import requests

user = '{"name": "Gustavo"}'

criate_user = requests.post("https://test-ef3c3-default-rtdb.firebaseio.com/.json", data=user)

print(criate_user)
print(criate_user.json())



