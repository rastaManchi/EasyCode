import requests
import json
import logging

logging.getLogger("requests").setLevel(logging.ERROR)

def get_access_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': '75888c00-0636-4c8f-9f52-131f7cb08d98',
        'Authorization': 'Basic ODExMzk2ODktYjcxNi00ZGE1LWIzNTgtOGM0MDdjOGQ5MDI4OjMyMTZiM2I3LWZkMDgtNDYxMi05ZmUyLWQwOTA2ODlmYmIzZA==' 
    }

    payload = {
        'scope': 'GIGACHAT_API_PERS'
    }

    result = requests.post("https://ngw.devices.sberbank.ru:9443/api/v2/oauth", headers=headers, data=payload, verify=False)
    token = json.loads(result.content).get('access_token')
    return token


def get_response(token, msg):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {
        "model": "GigaChat-2",
        "messages": [
            {
            "role": "user",
            "content": msg
            }
        ],
        "stream": False,
        "repetition_penalty": 1
    }
    result = requests.post("https://api.giga.chat/v1/chat/completions", headers=headers, data=json.dumps(payload), verify=False)
    answer = json.loads(result.content)
    answer = answer['choices'][0]['message']['content']
    print(answer)
    
    
while True:
    msg = input('Задайте вопрос: ')
    token = get_access_token()
    get_response(token, msg)