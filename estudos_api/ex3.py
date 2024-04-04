# Using the pach method
# line 7: data to be updated
# line 9: updating the database using the patch method

import requests

user = '{"idade": 28}'

update_user = requests.patch("https://test-ef3c3-default-rtdb.firebaseio.com/-NudbFyXJMRcg-hqPPzk.json", data=user)

print(update_user)
print(update_user.json())