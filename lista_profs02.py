from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.fatecjd.edu.br/site/a-fatec-jd/corpo-docente'
html = urlopen(url)

bsObj = BeautifulSoup(html.read(), 'html.parser')

body = bsObj.tbody
rows = body.findAll('tr')

for row in rows:
    name = row.find('td').getText()

    if 'MARIA' in name:
        print(row.getText())
