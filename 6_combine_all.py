import json
from os import walk
# Open and read the JSON file
all_item = []
for (dirpath, dirnames, filenames) in walk('./full_result'):
    for file in filenames:
        with open(f'{dirpath}/{file}', 'r', encoding='utf-8') as f:
            all_item.append(f.read().replace('https://cloud.xinmeitulu.com','<c>'))

with open(f'sum_all_export.json' , 'w', encoding='utf-8') as f:
        f.write(json.dumps(all_item))