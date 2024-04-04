# Using the DELETE method
# line 7: serch for information in the database
# line 12: delete user using delete method

import requests

consult_banck = requests.get("https://test-ef3c3-default-rtdb.firebaseio.com/.json")

print(consult_banck)
print(consult_banck.json())

delete_user = requests.delete("https://test-ef3c3-default-rtdb.firebaseio.com/1.json")

