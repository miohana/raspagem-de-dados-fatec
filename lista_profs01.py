from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.fatecjd.edu.br/site/a-fatec-jd/corpo-docente'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

body = soup.tbody
rows = body.findAll('tr')

for row in rows:
    print(row.text)
