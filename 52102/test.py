import requests

payload = {
    'email': 'admin@admin',
    'password': 'qwerty'
}

result = requests.post("http://127.0.0.1:5000/api/login", json=payload)
data = result.json()
print(data)
token = data.get('auth_token')

headers = {
    'Authorization': token
}

result = requests.get("http://127.0.0.1:5000/api/posts", headers=headers)
data = result.json()
print(data)