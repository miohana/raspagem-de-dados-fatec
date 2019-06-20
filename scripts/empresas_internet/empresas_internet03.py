from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.worldatlas.com/articles/the-25-largest-internet-companies-in-the-world.html'
html = urlopen(url)

soup = BeautifulSoup(html.read(), 'html.parser')

tbody = soup.tbody

linhas = tbody.findAll('tr')

empresa_faturamento = {}

for linha in linhas:
    nome_da_empresa = linha.findAll('td')[1].text
    faturamento = linha.findAll('td')[3].text

    empresa_faturamento[nome_da_empresa] = faturamento

print('Faturamento anual do Twitter:')
print(empresa_faturamento['Twitter'])
