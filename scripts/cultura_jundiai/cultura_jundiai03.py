from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://cultura.jundiai.sp.gov.br/'
html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

tag = soup.find('div', { 'class': 'tagcloud' })
links = tag.findAll('a')

for link in links:
    url = link['href']
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')

    lista_titulos = soup.findAll('a', { 'class': 'titulo-lista' })

    for titulo in lista_titulos:
        text = titulo.text
        if 'Arte' in text:
            print(text)
