import requests
import json
from bs4 import BeautifulSoup
import os

def parse_html_from_file(file_path):
  """Parses the HTML content of a file using BeautifulSoup.

  Args:
    file_path: The path to the HTML file.

  Returns:
    bs4.BeautifulSoup: The parsed BeautifulSoup object.
  """

  try:
    with open(file_path, 'r', encoding='utf-8') as f:
      html_content = f.read()
      return BeautifulSoup(html_content, 'html.parser')
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

# for x in range(2122):
#   page = x
file_path = f"testing_page.html"
soup = parse_html_from_file(file_path)
data = []
item_info = {}
if soup:
    title = soup.find('title')
    print(title.text)
    des = soup.find('meta', property='og:description')
    print(des['content'])
    images = soup.find_all('figure', class_='figure')
    images_string = []
    for image in images:
        images_string.append(image.find('a')['href'])
    item_info['title'] = title.text
    item_info['description'] = des['content']
    item_info['images'] = images_string
with open(f'out_test.json' , 'w', encoding='utf-8') as f:
    f.write(json.dumps(item_info))

arr = os.listdir("detail_page")
count = 0
for item in arr:
    print(f'process: {count}/{len(arr)}')
    file_to_check = f'detail_page/{item}'
    soup = parse_html_from_file(file_to_check)
    data = []
    item_info = {}
    if soup:
        title = soup.find('title')
        des = soup.find('meta', property='og:description')
        images = soup.find_all('figure', class_='figure')
        images_string = []
        for image in images:
            images_string.append(image.find('a')['href'])
        item_info['title'] = title.text
        item_info['description'] = des['content']
        item_info['images'] = images_string
    with open(f'full_result/{item.replace(".html", ".json")}' , 'w', encoding='utf-8') as f:
        count = count + 1
        f.write(json.dumps(item_info))

