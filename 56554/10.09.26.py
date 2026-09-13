# users = []

# print(users)
# users.append({'name': 'Булат'})
import json

with open('data.json', 'r') as file:
    result = json.loads(file.read())
    print(result["name"])

with open('data.json', 'w') as file:
    new = {"name": "Булат"}
    file.write(json.dumps(new))
