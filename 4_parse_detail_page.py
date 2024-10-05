import requests
import json
import html
import hashlib
import os.path
from bs4 import BeautifulSoup
def generate_unique_hash(data):
  """Generates a unique hash for the given data.

  Args:
    data: The data to be hashed.

  Returns:
    str: The unique hash.
  """

  hash_object = hashlib.sha256(data.encode('utf-8'))
  hash_value = hash_object.hexdigest()
  return hash_value

def download_raw_html(url, file_path):
  try:
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'w', encoding='utf-8') as f:
      f.write(html.unescape(response.text))

    return True
  except Exception as e:
    print(f"An error occurred: {e}")
    return False
  
file_path = f"sum_all.json"
counter = 0
with open(file_path, 'r') as file:
    data = json.load(file)
    
for item in data:
    counter = counter + 1
    url = item['link']
    file = f"detail_page/{item['name'].replace('/', '_')}.html"
   
    if not os.path.exists(file):
      if download_raw_html(url, file):
          print("HTML downloaded successfully!")
      else:
          print("Failed to download HTML.")
print(counter)