import json 

def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_format = json.loads(file.read())
    file.close()
    return json_format


json_format = open_file('vadim.txt')

items = json_format['items']
count = 0

for item in items:
    print(f'{count}  -- {item['name']}')
    count += 1

