import requests
from bs4 import BeautifulSoup as bs

domen = 'https://platform-easycode.ru'
url = 'https://platform-easycode.ru/login'
headers = {
    'cookie': 'XSRF-TOKEN=eyJpdiI6IkdJcnhGTGJ4Rmp3cDVQMnR6d251c1E9PSIsInZhbHVlIjoiTG1WTkJLNng2RHNvWDRhOGlRVE10dDMwai8vdXFkMEtMRE4reTZWcU42YXVZYnJ3dFgyWkNibms0VHlWQmdlVmpZVWZGdlF6eWNPUkk4cnBBNDVTUTkzcXdwWFlGQ1hNSnpGc1hVSU5RclhjbnNPYlRPYjJ0dDZ0b2lianRNZzUiLCJtYWMiOiJkNjM4NTNjYTczZmMzZGRjMWVhZTU2NTY2OGI4ODM4ODY5MzgzNzM1NjNmNWUwMmM1YmEzNjhiY2Y4OTNmMTIzIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6Iml4eVZRaDdKTDZsdHIzQ05iRWJ4cVE9PSIsInZhbHVlIjoiUE0wQ3RyRkxTK3k3OHh2aVRIdml0Q2ZYMXdOVzdkcWNObi80OXhvU1hMd3FsY2U1QlBOS0tFdGhtUGlrSUJDU1pJRDMzSW5raVdpUzE3V1QxNlVFMGdkVDBUbXBud0ZNT2FURFFzRFYrNzRxT1I3ME1ueDc4WG04WlB5anVYNkgiLCJtYWMiOiJlOTAwMWI5NWE3Njk1MWM1YjhmZTFmNGU2NWNiMTE1ZWIzNzIyZTNjY2MxNjcwMDVhNzcxYWMwNDA0ODE1MjI1IiwidGFnIjoiIn0%3D; _ym_uid=1746293333214766909; _ym_d=1746293333; _ym_isad=2; _ym_visorc=w',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
}

r = requests.get(url, headers=headers)

data = bs(r.content, 'lxml')

style = data.find('body').find('div').get('style')
style = style.split('(')[1].split(')')[0]
print(f'{domen}{style}')

