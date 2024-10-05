import requests
import json
from bs4 import BeautifulSoup

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

for x in range(2122):
  page = x
  file_path = f"output/index{page}.html"
  soup = parse_html_from_file(file_path)
  data = []
  if soup:
      items = soup.find_all('div', class_='col-sm-12 col-md-4')
      # Print the titles
      for item in items:
          item_info = {}
          # Find all elements with the class 'article-title'
          title = item.find('article', class_='container')
          link = title.find('a')
          if link is not  None:
            img_tag = link.find('img')
            name = link.find('figcaption')
            data_original = img_tag.get('data-original'+'\n')

            tags = item.find_all('p',class_='mb-0')
            all_tags_save = []
            for tag in tags:
              infos = tag.find_all('a')
              for info in infos:
                # print(info)
                all_tags_save.append(info.text.strip())
            # print('name:' + str(name.text)) #name
            # print('thubmnail:' +img_tag['data-original-']+'\n')#thumnail
            # print('link:' +link['href']+'\n')#link to detail
            for tag_text in all_tags_save:
                print('tag:' + tag_text)
            item_info["name"] = str(name.text)
            item_info["thubmnail"] = img_tag['data-original-']
            item_info["link"] = link['href']
            item_info["tags"] = all_tags_save
            print("----")
            data.append(item_info)
      with open(f'parsed_info/parsed_page_{page}.json' , 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))

