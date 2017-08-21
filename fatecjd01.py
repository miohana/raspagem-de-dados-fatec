from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.fatecjd.edu.br/'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

h2 = soup.find('h2')
print(h2)

print("---------------------------------")

lista_h2 = soup.findAll('h2')
print(lista_h2)
