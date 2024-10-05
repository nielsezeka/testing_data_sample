import requests
import html

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

# Example usage:
for x in range(2122):
    url = "https://www.xinmeitulu.com/page/"+str(x)
    file_path = "output/index"+str(x)+".html"

    if download_raw_html(url, file_path):
        print("HTML downloaded successfully!")
    else:
        print("Failed to download HTML.")