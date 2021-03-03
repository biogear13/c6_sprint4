from bs4 import BeautifulSoup
from IPython import embed
import requests
from IPython import embed
import time
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

time.sleep(2)

BASE_URL="https://albertyumol.github.io/"

def extract_html_content(target_url):
  response = requests.get(target_url, headers)
  return response.text

def main():
    for a in range(1,5):
        if x != 1:
            target_page = BASE_URL + 'page'+i+"index.html"
  target_page = BASE_URL + "index.html"
  html_content=extract_html_content(target_page)
  soup = BeautifulSoup(html_content, 'html.parser')
  bash = soup.find_all('div', 'list__item')
  for list_ in bash:
    print(list_.find('a').get_text('href'))

if __name__ == "__main__":
    main()
