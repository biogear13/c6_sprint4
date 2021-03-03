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
  target_page = BASE_URL + "index.html"
  html_content=extract_html_content(target_page)
  soup = BeautifulSoup(html_content, 'html.parser')
  script_tag = soup.find_all('h2')
  for a in script_tag:
    print(a)

if __name__ == "__main__":
    main()
