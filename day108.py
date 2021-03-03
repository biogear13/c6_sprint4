from bs4 import BeautifulSoup
from IPython import embed
import re

def generate_html():
  return """
      <html>
        <head></head>
        <body>
          <a href="/a.html">A</div>
          <a href="/b.html">B</div>
          <a href="/c.html">C</div>
          <a href="/d.html">D</div>
          <script>
            var hello = "yoh";
            alert(hello);
        </script>
        </body>
      </html>
    """

def main():
  html_doc = generate_html()
  soup = BeautifulSoup(html_doc, 'html.parser')
  script_tag = soup.find('script')

  text = re.search(r'\var hello"(.?+)"";', script_tag).group(1)
  print(text)

if __name__ == "__main__":
    main()
