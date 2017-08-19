from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://cultura.jundiai.sp.gov.br/tag/jundiai/'
html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

lista_titulos = soup.findAll('a', { 'class': 'titulo-lista' })

for titulo in lista_titulos:
    print(titulo.text)
