from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
  return """
      <html>
        <head></head>
        <body>
          <a href="/a.html">A</div>
          <a href="/b.html">B</div>
          <a href="/c.html">C</div>
          <a href="/d.html">D</div>
        </body>
      </html>
    """

def main():
  html_doc = generate_html()
  soup = BeautifulSoup(html_doc, 'html.parser')
  div_elements = soup.find_all('div')

  for div_element in div_elements:
    print(div_element.get_html())
  embed()

if __name__ == "__main__":
    main()
