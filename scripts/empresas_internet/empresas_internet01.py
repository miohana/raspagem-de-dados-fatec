from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.worldatlas.com/articles/the-25-largest-internet-companies-in-the-world.html'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

tbody = soup.tbody

linhas = tbody.findAll('tr')

for linha in linhas:
    print(linha)
