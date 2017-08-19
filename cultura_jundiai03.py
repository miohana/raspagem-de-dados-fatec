from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://cultura.jundiai.sp.gov.br/'
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), 'html.parser')

tag = bsObj.find('div', { 'class': 'tagcloud' })
links = tag.findAll('a')

for link in links:
    url = link['href'] 
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), 'html.parser')

    lista_titulos = bsObj.findAll('a', { 'class': 'titulo-lista' })

    for titulo in lista_titulos:
        text = titulo.text
        if 'Arte' in text:
            print(text)
