# curl -L -X POST 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth' \
# -H 'Content-Type: application/x-www-form-urlencoded' \
# -H 'Accept: application/json' \
# -H 'RqUID: <уникальный_идентификатор_запроса>' \
# -H 'Authorization: Basic authorization_key' \
# --data-urlencode 'scope=GIGACHAT_API_PERS'

import requests


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '463812d2-96b1-4bf7-90d3-8c3ec00c39ac',
    'Authorization': 'Basic ODExMzk2ODktYjcxNi00ZGE1LWIzNTgtOGM0MDdjOGQ5MDI4Ojc4ZGVjMjY3LWUzZGQtNDRlMi05NDBhLTcyYzhkMjMwZDBkOA=='
}


payload = {
    'scope': 'GIGACHAT_API_PERS'
}


r = requests.post('https://ngw.devices.sberbank.ru:9443/api/v2/oauth', headers=headers, data=payload, verify=False)
print(r.content)