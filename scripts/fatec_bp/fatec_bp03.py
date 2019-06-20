from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.fatecbpaulista.edu.br/eventos/'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

pag_buttons = soup.find('div', { 'class': 'content__pags' }).findAll('a')

for pag_button in pag_buttons:
    url = pag_button['href']
    html = urlopen(url)

    soup = BeautifulSoup(html.read(), 'html.parser')

    lista_divs = soup.findAll('div', { 'class': 'content__event'})

    for div in lista_divs:
        titulo = div.find('a', {'class': 'description__title' })

        print(titulo.text.strip())
