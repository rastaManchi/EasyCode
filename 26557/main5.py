# pip install requests

import requests, json


# payload = {
#     "text": "Question?"
# }
# r = requests.post('http://127.0.0.1:8000/questions/', data=payload)
r = requests.get('http://127.0.0.1:8000/questions/2/')
updata = json.loads(r.content)
print(updata)

payload = {
    "text": "Ответ1",
    "user_id": "user-123"
}
# r = requests.post('http://127.0.0.1:8000/questions/2/answers/', data=payload)
r = requests.get('http://127.0.0.1:8000/answers/4/')
print(json.loads(r.content))


r = requests.delete('http://127.0.0.1:8000/questions/2/')
