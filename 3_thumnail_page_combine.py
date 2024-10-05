import json

# Open and read the JSON file
all_item = []
for x in range(2122):
    page = x
    file_path = f"parsed_info/parsed_page_{page}.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
    for item in data:
        all_item.append(item)

with open(f'sum_all.json' , 'w', encoding='utf-8') as f:
        f.write(json.dumps(all_item))